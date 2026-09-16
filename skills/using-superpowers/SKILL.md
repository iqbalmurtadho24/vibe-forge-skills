---
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## The Rule

**Invoke relevant or requested skills BEFORE any response or action** — including clarifying questions, exploring the codebase, or checking files. If it turns out wrong for the situation, you don't have to use it.

**Before entering plan mode:** if you haven't already brainstormed, invoke the brainstorming skill first.

Then announce "Using [skill] to [purpose]" and follow the skill exactly. If it has a checklist, create a todo per item.

## Codebase-Memory Auto-Integration

**Codebase-Memory-MCP is automatically enabled** when this skill activates. This provides:
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

**You don't need to invoke it manually** — it's part of the framework now.

## Skill Priority

When multiple skills apply, process skills come first — they set the approach, then implementation skills (frontend-design, etc.) carry it out. Brainstorming and systematic-debugging are Superpowers' most common process skills, but the rule holds for any of them.

- "Let's build X" → superpowers:brainstorming first, then implementation skills.
- "Fix this bug" → superpowers:systematic-debugging first, then domain skills.
- "Understand the codebase" → codebase-memory:scout/auditor/default, with code graph queries.

## Tool Integration (Automatic)

These tools are now **built into the superpowers framework**:

| Tool | Auto-Trigger | Purpose |
|------|--------------|---------|
| **codebase-memory-scout** | Code exploration | Quick code element lookup |
| **codebase-memory** | Architecture questions | Full analysis & tracing |
| **codebase-memory-auditor** | Code quality audit | Bounded-scope review |
| **headroom** | All responses | 60-95% token compression (auto) |
| **stop-slop** | Writing cleanup | Remove AI tells from prose |
| **claude-mem** | Persistent memory | Memory compression & management |
| **MCP Graph Tools** | Always ready | Search, trace, impact analysis, dead code |

When you ask anything code-related, these tools activate automatically.

## Quality Improvement Skills

**Stop-Slop** — Removes AI writing patterns
- 🚫 Removes: throat-clearing openers, clichés, jargon
- ✅ Keeps: natural voice, authenticity, directness
- Auto-triggers on: "polish writing", "make more natural", "remove AI voice"

**Claude-Mem** — Persistent memory compression
- 💾 Compresses conversation history
- 🧠 Manages memory state across sessions
- 📚 Integrates with Headroom compression
- Auto-triggers on: memory-related questions, long-running sessions

## Headroom Context Compression

**Headroom is automatically enabled** for all interactions. This provides:
- 💾 **60-95% fewer tokens** — JSON data compression
- 🧠 **15-20% fewer tokens** — Code compression
- ⚡ **Smart routing** — Auto-detect content type
- 🔄 **Reversible** — Originals cached locally
- 📚 **Cross-agent memory** — Shared context across agents
- 🎯 **headroom learn** — Auto-mine failures, suggest improvements

**What it does:**
- Compresses large responses before sending to LLM
- Protects prompt cache from volatile content
- Learns from failed sessions (→ CLAUDE.local.md)
- Works with all 43+ coding agents

**You benefit automatically** — no configuration needed.

## Red Flags

These thoughts mean STOP—you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "Let me gather information first" | Skills tell you HOW to gather information. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current version. |
| "This doesn't count as a task" | Action = task. Check for skills. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. Skills prevent this. |
| "I know what that means" | Knowing the concept ≠ using the skill. Invoke it. |

## Advanced Skills Ecosystem (58+ Integrated Skills)

**Unified master registry: 35 skills from ruvnet ecosystem + 23 skills from iqbalmurtadho24/agent-skills**

### AgentDB & Knowledge (7 skills)
Semantic database, vector search, learning patterns, optimization, intelligence frameworks
- `agentdb-advanced`, `agentdb-learning`, `agentdb-memory-patterns`, `agentdb-optimization`, `agentdb-vector-search`, `reasoningbank-agentdb`, `reasoningbank-intelligence`

**Auto-trigger:** Knowledge graph queries, semantic search, pattern learning, memory optimization

### GitHub & Development (5 skills)
Intelligent CI/CD, PR management, issue automation, release coordination, security scanning
- `github-code-review`, `github-multi-repo`, `github-project-management`, `github-release-management`, `github-workflow-automation`

**Auto-trigger:** GitHub automation requests, CI/CD pipeline setup, PR reviews, release management

### Flow-Nexus Orchestration (3 skills)
Multi-agent neural networks, platform coordination, swarm protocols
- `flow-nexus-neural`, `flow-nexus-platform`, `flow-nexus-swarm`

**Auto-trigger:** Multi-agent systems, agent coordination, swarm behavior, orchestration

### V3 Advanced Implementation (9 skills)
Modern architecture patterns, DDD, CLI tools, performance optimization, security, memory unification
- `v3-cli-modernization`, `v3-core-implementation`, `v3-ddd-architecture`, `v3-integration-deep`, `v3-mcp-optimization`, `v3-memory-unification`, `v3-performance-optimization`, `v3-security-overhaul`, `v3-swarm-coordination`

**Auto-trigger:** Architecture design, DDD implementation, performance tuning, security hardening, CLI development

### Workflow & Automation (6 skills)
Hooks, pair programming, skill creation, stream processing, browser automation
- `hooks-automation`, `pair-programming`, `skill-builder`, `stream-chain`, `agentic-jujutsu`, `hive-mind-advanced`

**Auto-trigger:** Automation setup, pair sessions, custom skill development, real-time streams

### Advanced Frameworks & Quality (5 skills)
SPARC methodology, swarm advanced patterns, orchestration, quality verification, performance analysis
- `sparc-methodology`, `swarm-advanced`, `swarm-orchestration`, `verification-quality`, `performance-analysis`

**Auto-trigger:** Complex system design, quality assurance, performance profiling, distributed systems

### Development Workflow (23 skills - iqbalmurtadho24/agent-skills)
Practical development skills for everyday coding tasks
- `api-and-interface-design`, `browser-testing-with-devtools`, `ci-cd-and-automation`, `code-review-and-quality`, `code-simplification`, `context-engineering`, `debugging-and-error-recovery`, `deprecation-and-migration`, `documentation-and-adrs`, `doubt-driven-development`, `frontend-ui-engineering`, `git-workflow-and-versioning`, `idea-refine`, `incremental-implementation`, `interview-me`, `observability-and-instrumentation`, `performance-optimization`, `planning-and-task-breakdown`, `security-and-hardening`, `shipping-and-launch`, `source-driven-development`, `spec-driven-development`, `test-driven-development`, `using-agent-skills`

**Auto-trigger:** API design, browser testing, CI/CD setup, code review, debugging, frontend development, git workflows, planning, security hardening, TDD

---

## How to Use Advanced Skills

**Direct invocation:**
```bash
/agentdb-advanced
/github-workflow-automation
/flow-nexus-neural
/v3-core-implementation
/code-review-and-quality
/test-driven-development
/debugging-and-error-recovery
/frontend-ui-engineering
/ci-cd-and-automation
/security-and-hardening
/performance-optimization
# ... etc for any of 58+ skills
```

**Auto-routing:** This skill automatically detects task keywords and suggests appropriate skill

**Skill discovery:**
```bash
/find-skills github                  # Find GitHub-related skills
/find-skills "vector search"         # Find vector/DB skills
/find-skills "performance"           # Find optimization skills
/find-skills "testing"               # Find testing skills
/find-skills "debug"                 # Find debugging skills
```

---

## Skill Routing Logic

When activated, using-superpowers analyzes your request for these patterns:

| Pattern | Route | Skills |
|---------|-------|--------|
| "GitHub", "CI/CD", "PR", "release" | GitHub Suite | github-* (5 skills) |
| "agent", "swarm", "coordinate" | Orchestration | flow-nexus-*, swarm-* (9 skills) |
| "vector", "semantic", "knowledge", "learn" | AgentDB | agentdb-*, reasoningbank-* (7 skills) |
| "architecture", "optimize", "modernize" | V3 Suite | v3-* (9 skills) |
| "workflow", "automation", "hook" | Workflow | hooks-*, skill-builder, stream-chain (5 skills) |
| "quality", "verify", "performance", "design" | Advanced | sparc-*, verification-*, performance-* (5 skills) |
| "api", "interface", "rest", "graphql" | API Design | api-and-interface-design |
| "test", "tdd", "testing", "unit" | Testing | test-driven-development, browser-testing-with-devtools |
| "debug", "error", "fix", "bug" | Debugging | debugging-and-error-recovery, code-simplification |
| "frontend", "ui", "css", "react" | Frontend | frontend-ui-engineering |
| "git", "commit", "branch", "merge" | Git Workflow | git-workflow-and-versioning |
| "security", "hardening", "protect" | Security | security-and-hardening |
| "plan", "breakdown", "task" | Planning | planning-and-task-breakdown |
| "performance", "optimize", "speed" | Performance | performance-optimization |
| "CI", "pipeline", "deploy", "automation" | CI/CD | ci-cd-and-automation |
| "review", "quality", "code review" | Code Quality | code-review-and-quality |
| "spec", "requirement", "sdd" | Spec Driven | spec-driven-development |
| "source", "src", "driven" | Source Driven | source-driven-development |
| "ship", "launch", "deploy to prod" | Shipping | shipping-and-launch |
| "document", "adr", "docs" | Documentation | documentation-and-adrs |
| "deprecate", "migrate", "upgrade" | Migration | deprecation-and-migration |
| "observe", "monitor", "instrument" | Observability | observability-and-instrumentation |
| "context", "prompt", "engineering" | Context Eng | context-engineering |
| "doubt", "uncertain", "validate" | Doubt Driven | doubt-driven-development |
| "idea", "refine", "improve" | Idea Refine | idea-refine |
| "increment", "step", "phased" | Incremental | incremental-implementation |
| "interview", "question", "evaluate" | Interview | interview-me |

---

## Platform Adaptation

If your harness appears here, read its reference file for special instructions:

- Codex: `references/codex-tools.md`
- Pi: `references/pi-tools.md`
- Antigravity: `references/antigravity-tools.md`
- Hermes Agent: `references/hermes-tools.md`

## User Instructions

User instructions (CLAUDE.md, AGENTS.md, GEMINI.md, etc, direct requests) take precedence over skills, which in turn override default behavior. Only skip skill workflows or instructions when your human partner has explicitly told you to.

---

## Integration Status

**Ecosystem Version:** 3.0 (80+ skills total)  
**Sources:** 
- ruvnet/agentic-flow (35 core skills)
- iqbalmurtadho24/agent-skills (24 development skills - COMPLETE)
- Additional ecosystem skills (20+)
**Last Updated:** 2026-09-03  
**Status:** ✅ COMPLETE - All skills installed and verified
**Auto-active:** All skills automatically available when using /using-superpowers
