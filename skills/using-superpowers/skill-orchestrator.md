# Using-SuperPowers: Skill Orchestrator

**Intelligent routing engine untuk 35+ integrated skills**

---

## How It Works

1. **User provides task/request**
2. **Orchestrator analyzes keywords** (see mapping table below)
3. **Route to primary skill** + suggest alternatives
4. **Execute skill with context**

---

## Keyword-to-Skill Mapping

### AgentDB Suite (7 skills)
**Primary Keywords:** `vector`, `semantic`, `knowledge`, `learn`, `embedding`, `similarity`, `database`

```
"vector search" → agentdb-vector-search
"semantic similarity" → agentdb-vector-search
"knowledge graph" → agentdb-advanced
"learning pattern" → agentdb-learning
"memory optimization" → agentdb-memory-patterns
"optimization strategy" → agentdb-optimization
"intelligence framework" → reasoningbank-intelligence
```

### GitHub Suite (5 skills)
**Primary Keywords:** `github`, `ci/cd`, `pull request`, `workflow`, `release`, `pr`, `action`

```
"github workflow" → github-workflow-automation
"ci/cd pipeline" → github-workflow-automation
"code review" → github-code-review
"multi-repo" → github-multi-repo
"project management" → github-project-management
"release" → github-release-management
"github action" → github-workflow-automation
```

### Flow-Nexus Suite (3 skills)
**Primary Keywords:** `agent`, `swarm`, `coordinate`, `orchestration`, `multi-agent`, `neural`

```
"agent coordination" → flow-nexus-platform
"swarm protocol" → flow-nexus-swarm
"neural network" → flow-nexus-neural
"multi-agent system" → flow-nexus-platform
"agent orchestration" → flow-nexus-platform
```

### V3 Suite (9 skills)
**Primary Keywords:** `architecture`, `optimize`, `ddd`, `modernize`, `security`, `performance`, `cli`, `mcp`

```
"architecture design" → v3-core-implementation
"ddd pattern" → v3-ddd-architecture
"performance tuning" → v3-performance-optimization
"security hardening" → v3-security-overhaul
"cli modernization" → v3-cli-modernization
"deep integration" → v3-integration-deep
"mcp optimization" → v3-mcp-optimization
"memory management" → v3-memory-unification
"swarm coordination" → v3-swarm-coordination
```

### Workflow Suite (6 skills)
**Primary Keywords:** `workflow`, `automation`, `hook`, `pair`, `stream`, `skill`, `jujutsu`

```
"workflow automation" → hooks-automation
"pair programming" → pair-programming
"skill creation" → skill-builder
"stream processing" → stream-chain
"continuous automation" → hooks-automation
"agentic patterns" → agentic-jujutsu
"collaborative coding" → hive-mind-advanced
```

### Advanced Frameworks (5 skills)
**Primary Keywords:** `sparc`, `swarm`, `quality`, `verify`, `performance`, `analysis`, `design`

```
"sparc methodology" → sparc-methodology
"advanced swarm" → swarm-advanced
"swarm orchestration" → swarm-orchestration
"quality verification" → verification-quality
"performance profiling" → performance-analysis
"system design" → sparc-methodology
```

---

## Routing Algorithm

```
1. Extract keywords from user input
2. Score match against each skill's keyword list (see above)
3. If score > threshold (0.7):
   - Invoke highest-scoring skill
   - Show alternatives with similar scores
4. Else if multiple low-scoring matches:
   - Show 3-5 candidate skills
   - Ask user to select
5. Else:
   - Suggest running /find-skills <domain>
```

---

## Auto-Routing Examples

### Example 1: GitHub Request
```
User: "Set up GitHub Actions for automated testing"
Keywords detected: github, actions, automated, testing, ci/cd
Primary match: github-workflow-automation (score: 0.95)
Alternatives: github-code-review (score: 0.65)

→ Invoke /github-workflow-automation
```

### Example 2: Architecture Design
```
User: "Design microservices using Domain-Driven Design"
Keywords detected: design, architecture, ddd, microservices
Primary match: v3-ddd-architecture (score: 0.92)
Alternatives: v3-core-implementation (score: 0.78), sparc-methodology (score: 0.68)

→ Invoke /v3-ddd-architecture
```

### Example 3: Knowledge Management
```
User: "Build semantic search for our codebase"
Keywords detected: semantic, search, knowledge, vector
Primary match: agentdb-vector-search (score: 0.94)
Alternatives: agentdb-advanced (score: 0.75), agentdb-learning (score: 0.62)

→ Invoke /agentdb-vector-search
```

### Example 4: Agent Coordination
```
User: "Coordinate 10 AI agents in parallel"
Keywords detected: coordinate, agents, parallel, orchestration
Primary match: flow-nexus-platform (score: 0.90)
Alternatives: flow-nexus-swarm (score: 0.85), swarm-orchestration (score: 0.78)

→ Invoke /flow-nexus-platform
```

---

## Fallback Strategies

### When No Clear Match
- Show top 3-5 most relevant skills
- Allow user to select
- Remember selection for future similar requests

### When Skill Not Available Locally
- Offer to install from ecosystem
- Provide installation command: `npx skills add <repo/skill>`
- Fallback to general `find-skills` command

---

## Integration with Claude Code

**In SKILL.md (using-superpowers):**
- Orchestrator runs automatically when skill is invoked
- Analyzes user's task in the prompt
- Routes to most appropriate of 35+ skills
- Maintains context across skill transitions

**In CLAUDE.md:**
- Can define custom routing rules
- Can lock certain tasks to specific skills
- Can exclude certain skills from routing

---

## Performance Optimization

- Cache keyword mappings in-memory
- Pre-tokenize common phrases
- Score calculation: O(n) where n=keyword count
- Typical response time: <50ms for routing decision

---

## Extensibility

To add new skills to ecosystem:
1. Add skill folder to `.claude/skills/`
2. Include SKILL.md with metadata
3. Update `skills-manifest.json` with keywords
4. Update keyword mapping table above
5. Test with sample inputs

---

## Maintenance Notes

- Last updated: 2026-08-15
- Manifest version: 2.0
- Skills count: 35+
- Sync frequency: Manual (tracked in INTEGRATION_PLAN.md)
