---
name: vibe-forge
description: Master AI skill orchestrator and autonomous engineering engine. Automatically routes tasks across 110+ specialized skills (AgentDB, Swarms, GitHub CI/CD, V3 Architecture, TDD & Full-Cycle Dev, UI/UX, Strix Security, Caveman & Headroom Token Optimization).
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## The Vibe Forge Protocol

**Invoke relevant or requested skills BEFORE any response or action** — including clarifying questions, exploring the codebase, or checking files. If it turns out wrong for the situation, you don't have to use it.

**Before entering plan mode:** if you haven't already brainstormed, invoke the `brainstorming` skill first.

Then announce:
`Using [skill] to [purpose]` (via Vibe Forge)
and follow the skill exactly. If it has a checklist, create a todo per item.

## Codebase-Memory Auto-Integration

**Codebase-Memory-MCP is automatically enabled** when Vibe Forge activates. This provides:
- 📊 **Instant Code Graph** — Architecture visualization
- 🔍 **Smart Search** — Find code elements across 158 languages
- 📈 **Impact Analysis** — See what breaks when you change code
- 🧩 **Dead Code Detection** — Find unused functions
- 🔗 **Call Tracing** — Follow execution paths

**Auto-activate for:**
- Code exploration tasks
- Architecture questions
- Refactoring analysis
- Dependency tracing
- Dead code detection

**You don't need to invoke it manually** — it's part of the framework.

## Skill Priority

When multiple skills apply, process skills come first — they set the approach, then implementation skills carry it out:

- "Let's build X" → vibe-forge:brainstorming first, then implementation skills.
- "Fix this bug" → vibe-forge:systematic-debugging first, then domain skills.
- "Understand the codebase" → codebase-memory:scout/auditor/default, with code graph queries.

## Tool Integration (Automatic)

These tools are built into the Vibe Forge ecosystem:

| Tool | Auto-Trigger | Purpose |
|------|--------------|---------|
| **codebase-memory-scout** | Code exploration | Quick code element lookup |
| **codebase-memory** | Architecture questions | Full analysis & tracing |
| **codebase-memory-auditor** | Code quality audit | Bounded-scope review |
| **headroom** | All responses | 60-95% token compression (auto) |
| **stop-slop** | Writing cleanup | Remove AI tells from prose |
| **claude-mem** | Persistent memory | Memory compression & management |
| **MCP Graph Tools** | Always ready | Search, trace, impact analysis, dead code |

## Quality & Optimization Suites

**Stop-Slop** — Removes AI writing patterns
- 🚫 Removes: throat-clearing openers, clichés, corporate buzzwords, filler
- ✅ Keeps: natural voice, authenticity, technical directness

**Claude-Mem & Headroom** — Context & Token Optimization
- 💾 Compresses conversation history & token load (60-95% fewer tokens)
- 🧠 Reversible, smart routing, keeps prompt cache fresh

**Ponytail Suite** — Anti-Over-Engineering
- Eliminates speculative abstractions, premature generalizations, and dependency bloat

---

## 🧭 Vibe Forge Skills Ecosystem (110+ Integrated Skills)

### 1. AgentDB & Knowledge Graph (7 skills)
Semantic database, vector search, learning patterns, optimization, intelligence frameworks:
- `agentdb-advanced`, `agentdb-learning`, `agentdb-memory-patterns`, `agentdb-optimization`, `agentdb-vector-search`, `reasoningbank-agentdb`, `reasoningbank-intelligence`

### 2. GitHub Automation & CI/CD (5 skills)
Intelligent GitHub Actions, PR management, issue automation, releases:
- `github-code-review`, `github-multi-repo`, `github-project-management`, `github-release-management`, `github-workflow-automation`

### 3. Multi-Agent Swarm & Orchestration (7 skills)
Flow-Nexus swarms, distributed neural coordination, SPARC:
- `flow-nexus-neural`, `flow-nexus-platform`, `flow-nexus-swarm`, `hive-mind-advanced`, `swarm-advanced`, `swarm-orchestration`, `sparc-methodology`

### 4. V3 Architecture & Systems Engineering (9 skills)
Domain-Driven Design, microservices, MCP transport optimization, security overhaul:
- `v3-cli-modernization`, `v3-core-implementation`, `v3-ddd-architecture`, `v3-integration-deep`, `v3-mcp-optimization`, `v3-memory-unification`, `v3-performance-optimization`, `v3-security-overhaul`, `v3-swarm-coordination`

### 5. Full-Cycle Development Workflow (24 skills)
Practical, disciplined software engineering:
- `api-and-interface-design`, `browser-testing-with-devtools`, `ci-cd-and-automation`, `code-review-and-quality`, `code-simplification`, `coding-standards`, `context-engineering`, `debugging-and-error-recovery`, `deprecation-and-migration`, `documentation-and-adrs`, `doubt-driven-development`, `frontend-ui-engineering`, `git-workflow-and-versioning`, `idea-refine`, `incremental-implementation`, `interview-me`, `observability-and-instrumentation`, `performance-optimization`, `planning-and-task-breakdown`, `security-and-hardening`, `shipping-and-launch`, `source-driven-development`, `spec-driven-development`, `test-driven-development`

### 6. Verification, Planning & Subagents (7 skills)
Strict execution discipline and multi-agent delegation:
- `verification-before-completion`, `verification-quality`, `writing-plans`, `executing-plans`, `dispatching-parallel-agents`, `subagent-driven-development`, `finishing-a-development-branch`

### 7. Creative, UI/UX & Design Systems (8 skills)
Modern visual engineering, tokens, components, assets:
- `ui-ux-pro-max`, `ui-styling`, `design`, `design-system`, `banner-design`, `brand`, `slides`, `impeccable`

### 8. Cybersecurity & Penetration Testing (4 skills - Strix)
Automated scanning, remediation, exploit validation:
- `penetration-testing-with-strix`, `managed-pentesting-with-strix`, `ci-security-scanning-with-strix`, `fix-security-vulnerabilities-with-strix`

### 9. Token Efficiency & Extreme Conciseness (13 skills)
- Caveman suite: `caveman`, `caveman-commit`, `caveman-compress`, `caveman-help`, `caveman-review`, `caveman-stats`, `cavecrew`
- Ponytail suite: `ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, `ponytail-review`

### 10. Web, Browser & Automation Tools (6 skills)
- `browser-use`, `cloud`, `open-source`, `remote-browser`, `playwright-cli`, `hooks-automation`, `stream-chain`, `agentic-jujutsu`

---

## ⚡ How to Invoke Vibe Forge

### 1. Primary Invocation
```bash
/vibe-forge
```
Activates the master Vibe Forge router, runs task discovery, and dispatches the most optimal skill pipeline.

### 2. Direct Skill Invocations
```bash
/vibe-forge api-design              # Routes to api-and-interface-design
/brainstorming                      # Explore ideas before code
/systematic-debugging               # Strict root-cause bug isolation
/test-driven-development           # TDD red-green-refactor cycle
/ui-ux-pro-max                      # High-tier UI/UX design intelligence
```

### 3. Automatic Keyword Routing

| Request Content | Auto-Routed Skill |
|-----------------|-------------------|
| "Design API / endpoints" | `api-and-interface-design` |
| "Debug error / test fail" | `systematic-debugging`, `debugging-and-error-recovery` |
| "Setup CI/CD / GitHub action" | `github-workflow-automation`, `ci-cd-and-automation` |
| "Semantic search / Vector DB" | `agentdb-vector-search`, `agentdb-advanced` |
| "Refactor / simplify bloat" | `code-simplification`, `ponytail-review` |
| "Architecture / DDD" | `v3-ddd-architecture`, `v3-core-implementation` |
| "Security / Pentest" | `security-and-hardening`, `penetration-testing-with-strix` |
| "UI design / Tailwind / CSS" | `ui-ux-pro-max`, `frontend-ui-engineering`, `ui-styling` |
| "Plan feature / Roadmap" | `writing-plans`, `planning-and-task-breakdown` |

---

## Ecosystem Information

- **Ecosystem:** Vibe Forge (Universal Autonomous Engineering Layer)
- **Engine Version:** 3.5.0
- **Total Skills:** 110+ integrated skills
- **Supported Harnesses:** Antigravity CLI / IDE, Claude Code, Cursor, OpenCode, Codex, Gemini CLI
