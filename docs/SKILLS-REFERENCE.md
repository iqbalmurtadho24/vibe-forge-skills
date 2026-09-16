# 🎯 Complete Skills Reference - 48 Global Skills

**Setup Date**: 2026-08-14  
**Total Skills**: 48  
**CLI Tools Supported**: 76+  
**Installation Location**: `~/.agents/skills/`

---

## ✅ Auto-Setup Status

- [x] Git installed ✓
- [x] 48 skills installed globally ✓
- [x] Permissions configured in `~/.claude/settings.json` ✓
- [x] Available across all 76+ CLI tools ✓

---

## 📋 Skills Categories & Auto-Triggers

### 🧠 Development & Planning (14 skills)
Auto-triggers on: `coding task`, `feature request`, `implementation plan`

- `/brainstorming` — Explore requirements before coding
- `/writing-plans` — Create implementation plans
- `/test-driven-development` — Write tests first
- `/using-superpowers` — Establish skill framework
- `/subagent-driven-development` — Multi-agent task delegation
- `/systematic-debugging` — Debug any issue methodically
- `/verification-before-completion` — Verify work before closing
- `/receiving-code-review` — Process review feedback
- `/requesting-code-review` — Request peer review
- `/finishing-a-development-branch` — Merge strategy
- `/using-git-worktrees` — Isolated workspace setup
- `/dispatching-parallel-agents` — Run 2+ independent tasks
- `/executing-plans` — Execute multi-step plans
- `/writing-skills` — Create new skills

### 🔍 Code Quality & Optimization (7 skills)
Auto-triggers on: `code review`, `refactor`, `simplify`, `optimize`

- `/ponytail` — Lazy/minimal solution mode
- `/ponytail-review` — Review for over-engineering
- `/ponytail-audit` — Audit entire codebase
- `/ponytail-debt` — Track deferred work
- `/ponytail-gain` — Show ponytail impact metrics
- `/ponytail-help` — Command reference
- `/impeccable` — Polish UI/UX design

### 🔐 Security Testing (4 skills)
Auto-triggers on: `security`, `penetration test`, `vulnerability scan`

- `/penetration-testing-with-strix` — AI-powered pentesting
- `/fix-security-vulnerabilities-with-strix` — Patch exploits
- `/ci-security-scanning-with-strix` — CI/CD security gates
- `/managed-pentesting-with-strix` — Managed service

### 🌐 Browser Automation (5 skills)
Auto-triggers on: `browser`, `automation`, `scraping`, `testing`

- `/browser-use` — Direct browser control via CDP
- `/remote-browser` — Remote browser from sandbox
- `/playwright-cli` — Playwright test automation
- `/open-source` — Browser-use library docs
- `/cloud` — Browser-use Cloud API

### 🎨 UI/UX Design (8 skills)
Auto-triggers on: `design`, `UI`, `UX`, `interface`

- `/ui-ux-pro-max` — Complete UI/UX design reference
- `/impeccable` — Polish & refine interfaces
- `/design` — Logo, CIP, mockups, banners
- `/design-system` — Token architecture & specs
- `/ui-styling` — Accessible Tailwind components
- `/banner-design` — Social media & web banners
- `/brand` — Brand voice & visual identity
- `/slides` — Strategic HTML presentations

### 📊 Code Analysis (2 skills)
Auto-triggers on: `codebase analysis`, `language support`

- `/agent-eval` — Benchmark CodeGraph quality
- `/add-lang` — Add language support to CodeGraph

### ⚡ Token Efficiency (7 skills)
Auto-triggers on: `compress`, `token`, `save tokens`, `efficiency`

- `/caveman` — Ultra-compressed mode (65% token reduction)
- `/caveman-commit` — Compressed commit messages
- `/caveman-review` — Compressed code review
- `/caveman-compress` — Compress memory files
- `/caveman-help` — Caveman command reference
- `/cavecrew` — Delegate to compressed subagents
- `/caveman-stats` — Token usage statistics

### 🛠️ Utilities (2 skills)
Always available

- `/find-skills` — Discover & install new skills
- `/gstack` — Router for gstack suite

---

## 🚀 Usage Patterns

### Pattern 1: New Feature Development
```bash
/using-superpowers          # Start with skill framework
/brainstorming              # Explore requirements
/writing-plans              # Design implementation
/test-driven-development    # Write tests first
/subagent-driven-development # Delegate tasks
/systematic-debugging       # Fix issues
/verification-before-completion # Verify work
/requesting-code-review     # Get feedback
```

### Pattern 2: Security Review
```bash
/using-superpowers                      # Start
/penetration-testing-with-strix         # Find vulnerabilities
/fix-security-vulnerabilities-with-strix # Patch exploits
/ci-security-scanning-with-strix        # Add to CI/CD
```

### Pattern 3: UI Improvement
```bash
/impeccable          # Audit design
/ui-ux-pro-max       # Reference design system
/design-system       # Define tokens
/ui-styling          # Implement components
```

### Pattern 4: Code Cleanup
```bash
/ponytail         # Find over-engineering
/ponytail-review  # Review findings
/ponytail-audit   # Full codebase scan
/ponytail-debt    # Track shortcuts
```

### Pattern 5: Token Efficiency
```bash
/caveman         # Switch to compressed mode
/caveman-compress # Compress memory files
/cavecrew        # Delegate with compression
/caveman-stats   # Show savings
```

---

## 🎯 Auto-Trigger Hints

Skills auto-trigger when you mention keywords in context:

| Keyword | Skills | Use When |
|---------|--------|----------|
| `plan` | brainstorming, writing-plans | Need design before code |
| `test` | test-driven-development | Building new features |
| `debug` | systematic-debugging | Bug encountered |
| `review` | requesting-code-review | PR ready |
| `security` | penetration-testing-with-strix | Need security scan |
| `design` | ui-ux-pro-max, impeccable | UI/UX work |
| `simplify` | ponytail, ponytail-review | Code too complex |
| `token` | caveman, caveman-compress | Need shorter outputs |
| `browser` | browser-use, playwright-cli | Web automation |

---

## 📁 Skill Locations

All skills installed to:
```
~/.agents/skills/
├── add-lang/
├── agent-eval/
├── banner-design/
├── brainstorming/
├── brand/
├── browser-use/
├── cavecrew/
├── caveman/
├── caveman-commit/
├── caveman-compress/
├── caveman-help/
├── caveman-review/
├── caveman-stats/
├── ci-security-scanning-with-strix/
├── cloud/
├── design/
├── design-system/
├── dispatching-parallel-agents/
├── executing-plans/
├── find-skills/
├── finishing-a-development-branch/
├── fix-security-vulnerabilities-with-strix/
├── gstack/
├── impeccable/
├── managed-pentesting-with-strix/
├── open-source/
├── penetration-testing-with-strix/
├── playwright-cli/
├── ponytail/
├── ponytail-audit/
├── ponytail-debt/
├── ponytail-gain/
├── ponytail-help/
├── ponytail-review/
├── receiving-code-review/
├── remote-browser/
├── requesting-code-review/
├── slides/
├── subagent-driven-development/
├── systematic-debugging/
├── test-driven-development/
├── ui-styling/
├── ui-ux-pro-max/
├── using-git-worktrees/
├── using-superpowers/
├── verification-before-completion/
├── writing-plans/
└── writing-skills/
```

---

## 🔧 Configuration Files

### `~/.claude/settings.json`
Contains all 48 skills in `permissions.additionalDirectories`

```json
{
  "permissions": {
    "additionalDirectories": [
      "~/.agents/skills/add-lang",
      "~/.agents/skills/agent-eval",
      ...
      "~/.agents/skills/writing-skills"
    ]
  }
}
```

### `~/.claude/skills-configuration.json`
Master reference with categories and auto-trigger patterns

---

## 📊 Statistics

- **Total Skills**: 48
- **Development Skills**: 14
- **Code Quality Skills**: 7
- **Security Skills**: 4
- **Browser Skills**: 5
- **Design Skills**: 8
- **Analysis Skills**: 2
- **Token Efficiency Skills**: 7
- **Utility Skills**: 2

**CLI Tools Supported**: 76+ (Claude Code, Cursor, OpenHands, OpenCode, Continue, Cline, CodeBuddy, Windsurf, Roo Code, Zed, and 66+ more)

---

## ✨ Quick Reference

### Most Used Skills
1. `/using-superpowers` — Start any session
2. `/brainstorming` — Before coding
3. `/systematic-debugging` — When stuck
4. `/caveman` — Save tokens
5. `/ponytail` — Simplify code

### Emergency Skills
1. `/systematic-debugging` — Debug any issue
2. `/receiving-code-review` — Process feedback
3. `/verification-before-completion` — Double-check
4. `/caveman-compress` — Free up tokens
5. `/find-skills` — Find more tools

### High-Value Combinations
- Design: `/impeccable` + `/ui-ux-pro-max` + `/design-system`
- Security: `/penetration-testing-with-strix` + `/fix-security-vulnerabilities-with-strix` + `/ci-security-scanning-with-strix`
- Development: `/writing-plans` + `/test-driven-development` + `/subagent-driven-development` + `/verification-before-completion`
- Efficiency: `/caveman` + `/caveman-compress` + `/cavecrew` + `/caveman-stats`

---

## 🎓 Learning Path

**Day 1**: Setup & Basics
- [ ] `/using-superpowers` — Understand skill framework
- [ ] `/caveman-help` — Learn caveman modes
- [ ] `/ponytail-help` — Learn optimization

**Day 2**: Development Workflow
- [ ] `/brainstorming` — Plan feature
- [ ] `/writing-plans` — Design approach
- [ ] `/test-driven-development` — Write tests
- [ ] `/subagent-driven-development` — Delegate work

**Day 3**: Quality & Review
- [ ] `/systematic-debugging` — Fix issues
- [ ] `/ponytail-review` — Optimize code
- [ ] `/requesting-code-review` — Get feedback
- [ ] `/verification-before-completion` — Final check

**Day 4+**: Specialized Skills
- [ ] Security: Strix pentesting
- [ ] Design: UI/UX suite
- [ ] Browser: Automation tools
- [ ] Efficiency: Token compression

---

## 📞 Support & Commands

### Help Commands
- `/find-skills [query]` — Search for more skills
- `/caveman-help` — Caveman mode reference
- `/ponytail-help` — Ponytail mode reference
- `/using-superpowers` — Skill framework guide

### Configuration
- Settings file: `~/.claude/settings.json`
- Reference: `~/.claude/SKILLS-REFERENCE.md` (this file)
- Config doc: `~/.claude/skills-configuration.json`

### Status Check
- List all skills: `ls ~/.agents/skills/`
- Verify permissions: Check `settings.json`
- Test skill: `/find-skills` (always available)

---

**Setup Complete! 🎉 All 48 skills are ready to use across 76+ CLI tools.**
