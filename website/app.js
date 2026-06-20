/* ==============================================================================
   Antigravity SEO & Blog Suite - Premium Showcase Logic
   ============================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  setupTerminalSimulator();
  setupTabSwitcher();
  setupCopyButtons();
});

// 1. Terminal Simulator Setup
const COMMAND_RESPONSES = {
  'seo:run': {
    input: '/seo:run "Find SEO trends on our domain and outline a series"',
    output: [
      { text: '[supervisor] Initializing Master Supervisor Orchestrator...', type: 'system' },
      { text: '[supervisor] Checking cache for trend key: domain-trends__trends__2026-06-19.json', type: 'system' },
      { text: '[cache] Cache hit (age: 1.2 hours). Reusing google-trends data.', type: 'success' },
      { text: '[supervisor] Unified cached data: Top Queries:\n - "local seo tips 2026" (Index popularity: 95)\n - "geo generative search optimization" (Index popularity: 82)', type: 'default' },
      { text: '[supervisor] Delegating tasks to Blog Subsystem router (skills/blog/SKILL.md)...', type: 'system' },
      { text: '[blog] Generating series outline with blog-cluster agent...', type: 'system' },
      { text: '[blog] Layout created successfully! Saved series roadmap inside output/trends_outline_2026.md', type: 'success' },
      { text: '✓ [supervisor] Run complete. Total steps: 4/5. Execution time: 0.82 seconds.', type: 'success' }
    ]
  },
  'seo:audit': {
    input: '/seo:audit https://example.com --full',
    output: [
      { text: '[audit] Crawling target: https://example.com...', type: 'system' },
      { text: '[audit] Verifying Core Web Vitals targets (INP, LCP, CLS)...', type: 'system' },
      { text: ' - INP (Interaction to Next Paint): 120ms (GOOD)', type: 'default' },
      { text: ' - LCP (Largest Contentful Paint): 1.8s (GOOD)', type: 'default' },
      { text: ' - CLS (Cumulative Layout Shift): 0.04 (GOOD)', type: 'default' },
      { text: '[audit] Validating Schema.org markup objects...', type: 'system' },
      { text: ' - Found: WebSite schema, Organization schema, LocalBusiness schema.', type: 'default' },
      { text: '[audit] Scanning content readability and keyword authority...', type: 'system' },
      { text: ' - Flesch Reading Ease: 68.2 (Standard)', type: 'default' },
      { text: '[audit] Compiling final premium PDF report deliverable...', type: 'system' },
      { text: '✓ [audit] Done! Client report compiled to: pdf/example_com__audit__2026-06-19.pdf', type: 'success' }
    ]
  },
  'seo:create': {
    input: '/seo:create "local-seo" --brief',
    output: [
      { text: '[writer] Launching content generation for keyword: "local-seo"', type: 'system' },
      { text: '[writer] Pulling search intent cluster from cached keywords memory...', type: 'system' },
      { text: '[writer] Generating comprehensive brief via blog-brief (agent: content-brief-expert)...', type: 'system' },
      { text: ' - Primary Keyword: local-seo\n - Target Wordcount: 1,800 words\n - Recommended headings structure: H1, 4x H2, 3x H3\n - Secondary Semantics: local search console, map pack optimization, schema markup', type: 'default' },
      { text: '[writer] Constructing schema configurations...', type: 'system' },
      { text: '✓ [writer] Brief generated. Saved payload to: output/brief__local_seo.json', type: 'success' }
    ]
  }
};

function setupTerminalSimulator() {
  const terminalBody = document.getElementById('terminal-body');
  const triggerTags = document.querySelectorAll('.trigger-tag');
  let isTyping = false;

  if (!terminalBody) return;

  // Clear function
  function clearTerminal() {
    terminalBody.innerHTML = '';
  }

  // Type animation simulation
  async function typeCommand(commandKey) {
    if (isTyping) return;
    isTyping = true;
    clearTerminal();

    // Select active tag
    triggerTags.forEach(t => t.classList.remove('active'));
    const targetTag = Array.from(triggerTags).find(t => t.dataset.command === commandKey);
    if (targetTag) targetTag.classList.add('active');

    const cmdData = COMMAND_RESPONSES[commandKey];
    if (!cmdData) {
      isTyping = false;
      return;
    }

    // Create prompt line
    const promptLine = document.createElement('div');
    promptLine.className = 'prompt-line';
    terminalBody.appendChild(promptLine);

    // Type text animation
    const textToType = cmdData.input;
    for (let i = 0; i < textToType.length; i++) {
      promptLine.textContent += textToType[i];
      requestAnimationFrame(() => {
        terminalBody.scrollTop = terminalBody.scrollHeight;
      });
      await new Promise(resolve => setTimeout(resolve, 35));
    }

    await new Promise(resolve => setTimeout(resolve, 200));

    // Print outputs line by line
    for (const output of cmdData.output) {
      const line = document.createElement('div');
      line.className = `output-line ${output.type}`;
      
      // Formatting text representation (converts newlines to <br>)
      line.innerHTML = output.text.replace(/\n/g, '<br>');
      
      terminalBody.appendChild(line);
      requestAnimationFrame(() => {
        terminalBody.scrollTop = terminalBody.scrollHeight;
      });
      await new Promise(resolve => setTimeout(resolve, output.type === 'system' ? 300 : 150));
    }

    isTyping = false;
  }

  // Bind tags click events
  triggerTags.forEach(tag => {
    tag.addEventListener('click', () => {
      const cmd = tag.dataset.command;
      typeCommand(cmd);
    });
  });

  // Start with default typing
  typeCommand('seo:run');
}

// 2. Tabs Switcher Setup
function setupTabSwitcher() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.dataset.tab;

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetContent = document.getElementById(`tab-${targetTab}`);
      if (targetContent) {
        targetContent.classList.add('active');
      }
    });
  });
}

// 3. Copy Button Utility
function setupCopyButtons() {
  const copyBtns = document.querySelectorAll('.copy-btn');

  copyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.copy;
      let targetElement = document.getElementById(targetId);
      
      if (!targetElement) return;

      let textToCopy = '';
      if (targetElement.tagName === 'PRE' || targetElement.tagName === 'CODE') {
        textToCopy = targetElement.textContent;
      } else {
        textToCopy = targetElement.innerText || targetElement.textContent;
      }

      navigator.clipboard.writeText(textToCopy).then(() => {
        // Toggle icon visual
        const originalSVG = btn.innerHTML;
        btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg>`;
        btn.style.color = '#22c55e';
        btn.style.borderColor = '#22c55e';
        
        setTimeout(() => {
          btn.innerHTML = originalSVG;
          btn.style.color = '';
          btn.style.borderColor = '';
        }, 1500);
      }).catch(err => {
        console.error('Failed to copy to clipboard:', err);
      });
    });
  });
}
