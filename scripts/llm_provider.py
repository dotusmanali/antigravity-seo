#!/usr/bin/env python3
"""
LLM Provider abstraction for Antigravity SEO.
Supports NVIDIA NIM (OpenAI-compatible), KIE, and OpenAI.
"""

import json
import os
import time
from abc import ABC, abstractmethod
from typing import Any, Optional

import requests

class RateLimiter:
    """Simple token bucket rate limiter."""
    def __init__(self, rpm: int):
        self.rpm = rpm
        self.interval = 60.0 / rpm
        self.last_call = 0.0

    def wait(self):
        now = time.time()
        elapsed = now - self.last_call
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_call = time.time()

class LLMProvider(ABC):
    @abstractmethod
    def chat_completion(self, messages: list[dict[str, str]], **kwargs: Any) -> Optional[str]:
        pass

class NvidiaNimProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "nvidia/llama-3.1-405b-instruct"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://integrate.api.nvidia.com/v1"
        self.rate_limiter = RateLimiter(rpm=40)

    def chat_completion(self, messages: list[dict[str, str]], **kwargs: Any) -> Optional[str]:
        self.rate_limiter.wait()
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.3),
            "max_tokens": kwargs.get("max_tokens", 4096),
        }
        try:
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content")
        except Exception as exc:
            print(f"NVIDIA NIM call failed: {exc}")
            return None

class KieProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gemini-3.1-pro"):
        self.api_key = api_key
        self.model = model
        self.url = "https://api.kie.ai/gemini-3.1-pro/v1/chat/completions"

    def chat_completion(self, messages: list[dict[str, str]], **kwargs: Any) -> Optional[str]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.3),
            "max_tokens": kwargs.get("max_tokens", 8000),
        }
        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content")
        except Exception as exc:
            print(f"KIE call failed: {exc}")
            return None

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.openai.com/v1"

    def chat_completion(self, messages: list[dict[str, str]], **kwargs: Any) -> Optional[str]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.3),
            "max_tokens": kwargs.get("max_tokens", 4096),
        }
        try:
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content")
        except Exception as exc:
            print(f"OpenAI call failed: {exc}")
            return None

def get_provider() -> Optional[LLMProvider]:
    provider_name = os.environ.get("LLM_PROVIDER", "kie").lower()
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")

    if not api_key:
        # Fallback to provider-specific keys if LLM_API_KEY is not set
        if provider_name == "nvidia":
            api_key = os.environ.get("NVIDIA_API_KEY")
        elif provider_name == "kie":
            api_key = os.environ.get("KIE_API_KEY")
        elif provider_name == "openai":
            api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        # Final attempt to find KIE_API_KEY in .env files as per current logic
        for env_path in [".env", os.path.expanduser("~/.env")]:
            if os.path.isfile(env_path):
                with open(env_path) as fh:
                    for line in fh:
                        line = line.strip()
                        if line.startswith("KIE_API_KEY=") and not line.startswith("#"):
                            api_key = line.split("=", 1)[1].strip().strip("\"\'")
                            provider_name = "kie"
                            break
            if api_key:
                break

    if not api_key:
        return None

    if provider_name == "nvidia":
        return NvidiaNimProvider(api_key, model or "nvidia/llama-3.1-405b-instruct")
    elif provider_name == "openai":
        return OpenAIProvider(api_key, model or "gpt-4o")
    else:
        return KieProvider(api_key, model or "gemini-3.1-pro")
