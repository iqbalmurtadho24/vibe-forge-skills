import json, os

with open('skills-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

categories = {
    "Orchestrator and Meta-Workflows (13 Skills)": [
        'vibe-forge', 'using-superpowers', 'brainstorming', 'writing-plans',
        'executing-plans', 'subagent-driven-development', 'dispatching-parallel-agents',
        'finishing-a-development-branch', 'verification-before-completion',
        'using-agent-skills', 'using-git-worktrees', 'skill-builder', 'writing-skills',
    ],
    "Full-Cycle Software Engineering Workflow (26 Skills)": [
        'api-and-interface-design', 'browser-testing-with-devtools', 'ci-cd-and-automation',
        'code-review-and-quality', 'code-simplification', 'coding-standards', 'context-engineering',
        'debugging-and-error-recovery', 'deprecation-and-migration', 'documentation-and-adrs',
        'doubt-driven-development', 'frontend-ui-engineering', 'git-workflow-and-versioning',
        'idea-refine', 'incremental-implementation', 'interview-me', 'observability-and-instrumentation',
        'performance-optimization', 'planning-and-task-breakdown', 'receiving-code-review',
        'requesting-code-review', 'security-and-hardening', 'shipping-and-launch',
        'source-driven-development', 'spec-driven-development', 'test-driven-development',
    ],
    "AgentDB and Vector Intelligence Ecosystem (24 Skills)": [
        'agentdb-advanced', 'agentdb-causal-explain', 'agentdb-causal-link', 'agentdb-cypher',
        'agentdb-explainable-recall', 'agentdb-feedback', 'agentdb-hierarchical-store',
        'agentdb-hybrid-search', 'agentdb-hyperedge', 'agentdb-init', 'agentdb-learn',
        'agentdb-learning', 'agentdb-memory-patterns', 'agentdb-mmr', 'agentdb-optimization',
        'agentdb-recall', 'agentdb-remember', 'agentdb-route', 'agentdb-skill-create',
        'agentdb-status', 'agentdb-traverse', 'agentdb-vector-search',
        'reasoningbank-agentdb', 'reasoningbank-intelligence',
    ],
    "Multi-Agent Swarm and Orchestration (7 Skills)": [
        'flow-nexus-neural', 'flow-nexus-platform', 'flow-nexus-swarm',
        'hive-mind-advanced', 'swarm-advanced', 'swarm-orchestration', 'sparc-methodology',
    ],
    "V3 Advanced Architecture and Systems (9 Skills)": [
        'v3-cli-modernization', 'v3-core-implementation', 'v3-ddd-architecture',
        'v3-integration-deep', 'v3-mcp-optimization', 'v3-memory-unification',
        'v3-performance-optimization', 'v3-security-overhaul', 'v3-swarm-coordination',
    ],
    "GitHub Automation and CI/CD (5 Skills)": [
        'github-code-review', 'github-multi-repo', 'github-project-management',
        'github-release-management', 'github-workflow-automation',
    ],
    "Creative UI/UX and Design Systems (8 Skills)": [
        'ui-ux-pro-max', 'ui-styling', 'design', 'design-system',
        'banner-design', 'brand', 'slides', 'impeccable',
    ],
    "Cybersecurity and Penetration Testing - Strix (4 Skills)": [
        'penetration-testing-with-strix', 'managed-pentesting-with-strix',
        'ci-security-scanning-with-strix', 'fix-security-vulnerabilities-with-strix',
    ],
    "Token Efficiency and High-Signal Compression (15 Skills)": [
        'caveman', 'caveman-commit', 'caveman-compress', 'caveman-help',
        'caveman-review', 'caveman-stats', 'cavecrew',
        'ponytail', 'ponytail-audit', 'ponytail-debt', 'ponytail-gain',
        'ponytail-help', 'ponytail-review', 'stop-slop', 'claude-mem',
    ],
    "Browser Automation and Web Tools (8 Skills)": [
        'browser-use', 'cloud', 'open-source', 'remote-browser',
        'playwright-cli', 'hooks-automation', 'stream-chain', 'agentic-jujutsu',
    ],
    "Code Graph, Analysis and Meta-Tools (9 Skills)": [
        'codebase-memory', 'performance-analysis', 'verification-quality',
        'add-lang', 'agent-eval', 'find-skills', 'gstack',
        'pair-programming', 'systematic-debugging',
    ],
}

# Find uncategorized
all_cat_skills = []
for sks in categories.values():
    all_cat_skills.extend(sks)
uncat = [s for s in catalog.keys() if s not in all_cat_skills]
print("Uncategorized skills:", uncat)

lines = []
lines.append("# Vibe Forge\n")
lines.append("\n")
lines.append("> **Universal Autonomous Engineering and Skill Orchestration Ecosystem for AI Coding Agents**  \n")
lines.append("> *128+ Integrated Enterprise Skills - Intelligent Auto-Routing - Code Graph Memory - Context Token Optimization*\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("[![Skills Count](https://img.shields.io/badge/Skills-128%2B%20Verified-blueviolet.svg?style=flat-square)](#full-skills-catalog-128-skills)\n")
lines.append("[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)\n")
lines.append("[![Compatible With](https://img.shields.io/badge/AI%20Harnesses-Antigravity%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Codex-orange?style=flat-square)](#cross-platform-compatibility)\n")
lines.append("[![Version](https://img.shields.io/badge/Version-3.5.0-blue?style=flat-square)](#)\n")
lines.append("[![Token Savings](https://img.shields.io/badge/Token%20Savings-60--95%25-brightgreen?style=flat-square)](#embedded-optimization-engines)\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## What is Vibe Forge?\n")
lines.append("\n")
lines.append("**Vibe Forge** is a production-grade orchestration engine and standardized skill repository for AI coding agents. Compatible with **Google Antigravity (AGY)**, **Claude Code**, **Cursor**, **Codex**, **OpenCode**, and other AI harnesses.\n")
lines.append("\n")
lines.append("Traditional AI prompts often produce unverified code, speculative abstractions, and token-heavy responses. Vibe Forge solves this by enforcing an **autonomous engineering pipeline**:\n")
lines.append("\n")
lines.append("1. **Explore intent** via `brainstorming` and `interview-me`\n")
lines.append("2. **Draft rigorous specs** via `spec-driven-development` and `writing-plans`\n")
lines.append("3. **Execute with verification** via `test-driven-development` (TDD)\n")
lines.append("4. **Audit and harden** via `code-review-and-quality`, `ponytail-review`, and Strix pentesting\n")
lines.append("5. **Streamline context** with `codebase-memory-mcp`, `headroom`, and `caveman` compression (60-95% token savings)\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Master Invocation: /vibe-forge\n")
lines.append("\n")
lines.append("Activate the entire orchestration engine with a single slash command:\n")
lines.append("\n")
lines.append("```bash\n")
lines.append("/vibe-forge\n")
lines.append("```\n")
lines.append("\n")
lines.append("Or invoke with a specific goal:\n")
lines.append("\n")
lines.append("```bash\n")
lines.append("/vibe-forge Build a real-time WebSocket notification server with TDD\n")
lines.append("/vibe-forge Audit our microservices codebase for speculative complexity\n")
lines.append("/vibe-forge Design a high-conversion landing page using Tailwind and Radix UI\n")
lines.append("/vibe-forge Run an autonomous security pentest against the auth endpoints\n")
lines.append("```\n")
lines.append("\n")
lines.append("Vibe Forge automatically parses your objective, selects the appropriate skill chain, announces `Using [skill] to [purpose] (via Vibe Forge)`, and executes with full architectural discipline.\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## The Three-Layer Intelligence Stack\n")
lines.append("\n")
lines.append("```\n")
lines.append("Layer 1: CODE UNDERSTANDING (Codebase-Memory MCP)\n")
lines.append("  - AST Code Graph across 158 languages\n")
lines.append("  - Full Call-Chain Tracing and Cypher Graph Queries\n")
lines.append("  - Impact Analysis and Dead-Code Detection\n")
lines.append("\n")
lines.append("Layer 2: SKILL ORCHESTRATION (Vibe Forge Engine)\n")
lines.append("  - 128+ Enterprise Engineering Skills\n")
lines.append("  - Autonomous Keyword Auto-Routing\n")
lines.append("  - Subagent Task Fan-out and Red-Green-Refactor TDD Cycle\n")
lines.append("\n")
lines.append("Layer 3: CONTEXT AND TOKEN OPTIMIZATION\n")
lines.append("  - Headroom, Claude-Mem, Caveman, Stop-Slop\n")
lines.append("  - 60%-95% JSON and Code Token Savings\n")
lines.append("  - Zero AI Cliches, High-Signal Lean Responses\n")
lines.append("  - Persistent Cross-Session Episodic Memory\n")
lines.append("```\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Full Skills Catalog (128 Skills)\n")
lines.append("\n")

emoji_map = {
    "Orchestrator": "🚦",
    "Full-Cycle": "🏗️",
    "AgentDB": "🧠",
    "Multi-Agent": "🌐",
    "V3": "🏛️",
    "GitHub": "🐙",
    "Creative": "🎨",
    "Cybersecurity": "🛡️",
    "Token": "🗜️",
    "Browser": "🌍",
    "Code Graph": "📊",
}

for cat_name, skill_list in categories.items():
    lines.append(f"### {cat_name}\n")
    lines.append("\n")
    lines.append("| Skill | Description | Invoke |\n")
    lines.append("|:------|:------------|:-------|\n")
    for s in skill_list:
        desc = catalog.get(s, 'Integrated Vibe Forge skill.')
        desc = desc.replace('|', '-').replace('\n', ' ').strip()
        if len(desc) > 120:
            desc = desc[:120] + '...'
        lines.append(f"| [{s}](skills/{s}/SKILL.md) | {desc} | `/{s}` |\n")
    lines.append("\n")

if uncat:
    lines.append("### Additional Skills\n\n")
    for s in uncat:
        desc = catalog.get(s, '')[:80]
        lines.append(f"- [{s}](skills/{s}/SKILL.md): {desc}\n")
    lines.append("\n")

lines.append("---\n")
lines.append("\n")
lines.append("## Keyword-to-Skill Routing Table\n")
lines.append("\n")
lines.append("| User Task Keywords | Primary Skill | Complementary Skills |\n")
lines.append("|:---|:---|:---|\n")
routing = [
    ("API, REST, GraphQL, endpoint, contract", "api-and-interface-design", "coding-standards, documentation-and-adrs"),
    ("Bug, error, failed test, crash, regression", "systematic-debugging", "debugging-and-error-recovery, doubt-driven-development"),
    ("Feature, build, implement, create module", "brainstorming", "writing-plans, test-driven-development"),
    ("TDD, unit test, integration test, mock", "test-driven-development", "browser-testing-with-devtools, verification-quality"),
    ("UI, UX, frontend, Tailwind, CSS, layout", "ui-ux-pro-max", "ui-styling, frontend-ui-engineering"),
    ("Security, pentest, exploit, vulnerability, CVE", "penetration-testing-with-strix", "fix-security-vulnerabilities-with-strix, security-and-hardening"),
    ("Vector, AgentDB, semantic search, embedding", "agentdb-vector-search", "agentdb-advanced, agentdb-hybrid-search"),
    ("Swarm, multi-agent, coordinate, parallel agents", "flow-nexus-platform", "swarm-orchestration, hive-mind-advanced"),
    ("Clean code, simplify, refactor, remove bloat", "code-simplification", "ponytail-review, ponytail-audit"),
    ("Git, release, PR, merge, changelog, version", "git-workflow-and-versioning", "github-release-management, caveman-commit"),
    ("Architecture, DDD, microservices, bounded context", "v3-ddd-architecture", "v3-core-implementation, sparc-methodology"),
    ("Performance, optimize, speed, profiling, bottleneck", "performance-optimization", "v3-performance-optimization, performance-analysis"),
    ("Memory, patterns, semantic recall, learning", "agentdb-memory-patterns", "agentdb-recall, agentdb-remember"),
    ("Document, ADR, architecture decision, spec", "documentation-and-adrs", "spec-driven-development, writing-plans"),
    ("Deploy, ship, production, launch, rollout", "shipping-and-launch", "ci-cd-and-automation, verification-before-completion"),
]
for keywords, primary, complementary in routing:
    lines.append(f"| `{keywords}` | `{primary}` | `{complementary}` |\n")

lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Embedded Optimization Engines\n")
lines.append("\n")
lines.append("| Engine | Role | Impact |\n")
lines.append("|:---|:---|:---|\n")
lines.append("| **Codebase-Memory MCP** | Structural AST code knowledge graph | Instantaneous search and call-path tracing across 158 languages without reading thousands of file lines |\n")
lines.append("| **Headroom Compression** | Context token optimization | Reduces tokens by 60-95% on large JSON datasets and code snippets while keeping cached context reversible |\n")
lines.append("| **Stop-Slop** | AI prose filter | Strips verbose conversational filler, throat-clearing openers, corporate cliches, and repetitive apologetic phrasing |\n")
lines.append("| **Claude-Mem** | Cross-session memory | Maintains persistent episodic and semantic memory across multiple AI agent sessions |\n")
lines.append("| **Ponytail Suite** | Bloat eliminator | Detects unnecessary abstractions, premature generalizations, and dependency sprawl before they compound |\n")
lines.append("| **Caveman Suite** | Extreme compression | Ultra-compressed response mode saving 65%+ tokens while maintaining full technical accuracy |\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Cross-Platform Compatibility\n")
lines.append("\n")
lines.append("Vibe Forge conforms to the universal **Agent Skills Specification** and is fully validated on:\n")
lines.append("\n")
lines.append("| AI Harness | Install Path | Status |\n")
lines.append("|:---|:---|:---|\n")
lines.append("| Google Antigravity (AGY) | `~/.agents/skills/` | Fully Active |\n")
lines.append("| Claude Code (Anthropic) | `~/.claude/skills/` | Fully Active |\n")
lines.append("| Cursor / OpenCode | Project-level `.cursor/rules/` | Compatible |\n")
lines.append("| Codex / Gemini CLI | System prompt injection | Compatible |\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Installation\n")
lines.append("\n")
lines.append("### Option A: Skills CLI\n")
lines.append("\n")
lines.append("```bash\n")
lines.append("npx skills add iqbalmurtadho24/vibe-forge -g -y\n")
lines.append("```\n")
lines.append("\n")
lines.append("### Option B: Manual Clone\n")
lines.append("\n")
lines.append("```bash\n")
lines.append("# Windows (PowerShell)\n")
lines.append('git clone https://github.com/iqbalmurtadho24/vibe-forge.git "$env:USERPROFILE\\.agents\\skills\\vibe-forge"\n')
lines.append("\n")
lines.append("# macOS / Linux\n")
lines.append("git clone https://github.com/iqbalmurtadho24/vibe-forge.git ~/.agents/skills/vibe-forge\n")
lines.append("```\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## Repository Structure\n")
lines.append("\n")
lines.append("```\n")
lines.append("vibe-forge/\n")
lines.append("├── .gitignore\n")
lines.append("├── LICENSE                      # MIT License\n")
lines.append("├── package.json                 # Package metadata\n")
lines.append("├── README.md                    # This file - comprehensive documentation\n")
lines.append("├── SKILL.md                     # Root master skill entrypoint for /vibe-forge\n")
lines.append("├── skills-manifest.json         # Machine-readable registry (128 skills)\n")
lines.append("├── skills-catalog.json          # Per-skill descriptions from SKILL.md frontmatter\n")
lines.append("├── docs/                        # In-depth architectural guides:\n")
lines.append("│   ├── AUTO-TRIGGER-GUIDE.md\n")
lines.append("│   ├── CODEBASE-MEMORY-INTEGRATION.md\n")
lines.append("│   ├── FULL-ECOSYSTEM-SUMMARY.md\n")
lines.append("│   ├── HEADROOM-INTEGRATION.md\n")
lines.append("│   ├── MULTI-CLI-SETUP.md\n")
lines.append("│   ├── SKILL-ECOSYSTEM-REGISTRY.md\n")
lines.append("│   └── START-HERE-FINAL.md\n")
lines.append("└── skills/                      # 128 individual skill packages\n")
lines.append("    ├── vibe-forge/              # Master Orchestrator (/vibe-forge)\n")
lines.append("    ├── agentdb-advanced/\n")
lines.append("    ├── api-and-interface-design/\n")
lines.append("    ├── test-driven-development/\n")
lines.append("    ├── ui-ux-pro-max/\n")
lines.append("    └── ... (all 128 skills, each with SKILL.md)\n")
lines.append("```\n")
lines.append("\n")
lines.append("---\n")
lines.append("\n")
lines.append("## License\n")
lines.append("\n")
lines.append("MIT License (c) 2026 Iqbal Murtadho. Free to use, adapt, and distribute for personal and commercial AI workflows.\n")

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("SUCCESS: README.md generated with", len(catalog), "skills across", len(categories), "categories")
print("Total lines:", len(lines))
