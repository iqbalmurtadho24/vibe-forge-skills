# Using-SuperPowers: Setup & Installation Guide

**Master ecosystem with 35+ integrated skills from ruvnet ecosystem**

---

## Quick Start

### Option 1: Via Git Submodule (Recommended)
```bash
cd ~/.claude/skills/using-superpowers/

# Add agentic-flow as submodule
git submodule add https://github.com/ruvnet/agentic-flow.git external/agentic-flow

# Initialize and update
git submodule update --init --recursive
```

### Option 2: Via Direct Clone
```bash
cd ~/.claude/skills/using-superpowers/

# Clone each source repository
git clone https://github.com/ruvnet/agentic-flow.git external/agentic-flow
git clone https://github.com/ruvnet/agentdb.git external/agentdb
git clone https://github.com/ruvnet/flow-nexus.git external/flow-nexus
```

### Option 3: Via Skills CLI
```bash
# Search for individual skills
npx skills find github-workflow
npx skills find agentdb
npx skills find flow-nexus

# Install individual skills
npx skills add ruvnet/agentic-flow@github-workflow-automation
npx skills add ruvnet/agentdb@agentdb-advanced
npx skills add ruvnet/flow-nexus@flow-nexus-platform
```

---

## Directory Structure After Setup

```
~/.claude/skills/
├── using-superpowers/              (main skill)
│   ├── SKILL.md                    (main router)
│   ├── INTEGRATION_PLAN.md          (planning doc)
│   ├── skills-manifest.json         (central registry)
│   ├── skill-orchestrator.md        (routing logic)
│   ├── SETUP_GUIDE.md              (this file)
│   │
│   └── external/                   (external skill sources)
│       ├── agentic-flow/           (35+ skills)
│       │   └── .claude/skills/
│       │       ├── agentdb-advanced/
│       │       ├── agentdb-learning/
│       │       ├── github-workflow-automation/
│       │       ├── flow-nexus-neural/
│       │       ├── v3-core-implementation/
│       │       └── ... (30+ more)
│       │
│       ├── agentdb/                (AgentDB suite source)
│       └── flow-nexus/             (Flow-Nexus source)
```

---

## Accessing Skills

### Method 1: Direct Invocation
```bash
/github-workflow-automation
/agentdb-vector-search
/flow-nexus-platform
/v3-ddd-architecture
# ... any of 35+ skills
```

### Method 2: Via using-superpowers Router
```bash
/using-superpowers
# → Presents ecosystem overview
# → Auto-suggests relevant skills based on task
```

### Method 3: Search
```bash
/find-skills github               # Find all GitHub-related
/find-skills vector               # Find vector/knowledge skills
/find-skills performance          # Find optimization skills
```

---

## Verification Checklist

After setup, verify installation:

```bash
# 1. Check main skill loads
[ ] /using-superpowers shows ecosystem

# 2. Verify manifest
[ ] skills-manifest.json exists
[ ] Contains all 35+ skills

# 3. Test routing
[ ] /find-skills github returns matches
[ ] /find-skills vector returns matches

# 4. Test sample skills
[ ] /github-workflow-automation works
[ ] /agentdb-vector-search works
[ ] /v3-ddd-architecture works
[ ] /flow-nexus-platform works

# 5. Auto-routing
[ ] Request: "set up GitHub CI/CD" → suggests github-workflow-automation
[ ] Request: "design microservices" → suggests v3-ddd-architecture
[ ] Request: "semantic search" → suggests agentdb-vector-search
```

---

## Configuration

### Via CLAUDE.md
```yaml
# Define custom routing rules
skills:
  using-superpowers:
    priority: true
    auto_route: true
    excluded_skills: []          # Remove skills if needed
    preferred_skills:            # Prefer these if multiple match
      - github-workflow-automation
      - v3-core-implementation

# Lock certain tasks to specific skills
github_tasks:
  skill: github-workflow-automation
  keywords: [github, ci/cd, workflow, action]
```

### Via settings.json
```json
{
  "skills": {
    "using-superpowers": {
      "enabled": true,
      "auto_routing": true,
      "ecosystem_mode": "35+",
      "external_sources": [
        "external/agentic-flow",
        "external/agentdb",
        "external/flow-nexus"
      ]
    }
  }
}
```

---

## Troubleshooting

### Skills not appearing
```bash
# Verify they exist
find ~/.claude/skills/using-superpowers -name "SKILL.md"

# Check manifest
cat ~/.claude/skills/using-superpowers/skills-manifest.json | jq '.total_skills'

# Re-index if needed
npx skills update
```

### Routing not working
```bash
# Check Claude Code is using latest version
claude --version

# Verify using-superpowers skill loads
/using-superpowers --list

# Check keyboard shortcuts
claude config show | grep superpowers
```

### External repository not syncing
```bash
# If using submodules
cd ~/.claude/skills/using-superpowers
git submodule update --remote

# If using direct clone
cd external/agentic-flow
git pull origin main
```

---

## Maintaining Skills

### Update all skills
```bash
# Via submodules
cd ~/.claude/skills/using-superpowers
git submodule update --remote --recursive

# Via direct clones
for dir in external/*; do
  cd $dir && git pull origin main && cd ../..
done

# Via skills CLI
npx skills update
```

### Adding new skills to ecosystem
1. Create skill folder in `.claude/skills/`
2. Add `SKILL.md` with metadata
3. Update `skills-manifest.json`
4. Update skill-orchestrator.md keyword mapping
5. Test routing

### Removing skills
1. Remove from `skills-manifest.json`
2. Update SKILL.md categories
3. Update skill-orchestrator.md
4. Delete skill folder if local

---

## Performance Optimization

### Lazy Loading Skills
- Skills are only loaded when invoked
- Manifest cached in-memory
- Routing decision: ~50ms average

### Caching
- Keyword mappings cached
- Manifest pre-loaded on session start
- Recent skill invocations cached

---

## Integration with Other Tools

### With codebase-memory-mcp
- Auto-enabled for code exploration skills (v3-*, github-*)
- Provides architecture visualization
- Enables impact analysis

### With code-review skill
- github-code-review integrates with main code-review
- Provides specialized GitHub-aware review

### With brainstorming skill
- AgentDB suite provides knowledge base integration
- Supports semantic search during brainstorming

---

## Support & Documentation

- **Manifest Registry:** `skills-manifest.json`
- **Routing Logic:** `skill-orchestrator.md`
- **Integration Status:** `INTEGRATION_PLAN.md`
- **Main Router:** `SKILL.md`

---

## Next Steps

1. **Install external sources** (choose Option 1, 2, or 3 above)
2. **Run verification checklist**
3. **Test sample workflows** in each category
4. **Customize routing** via CLAUDE.md if needed
5. **Keep updated** via `git submodule update` or `npx skills update`

---

**Version:** 2.0  
**Date:** 2026-08-15  
**Total Skills:** 35+  
**Ecosystem:** ruvnet (agentic-flow, agentdb, flow-nexus)
