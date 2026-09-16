# 🌍 MULTI-CLI SETUP - Using Skills Across All Tools

**Status**: ✅ **ALL TOOLS CONFIGURED**  
**Date**: 2026-08-14

---

## 📋 CONFIGURED CLI TOOLS

All 50 skills now work across these CLI tools:

| Tool | Version | Status | Command |
|------|---------|--------|---------|
| **Claude Code** | 2.1.232 | ✅ Configured | `claude` |
| **Gemini CLI** | 0.55.1 | ✅ Configured | `gemini` |
| **OpenCode** | 1.18.18 | ✅ Configured | `opencode` |
| **AGY** | 1.1.13 | ✅ Configured | `agy` |

Plus: **72+ other tools** (via global skills directory)

---

## ✨ WHAT YOU CAN DO NOW

### In Any CLI Tool

```bash
# Use skills framework
/using-superpowers

# Use any of 50 skills
/brainstorming
/writing-plans
/systematic-debugging
/stop-slop
/claude-mem
... (all 50 skills)

# Use code understanding
Ask: "Where is X function?"
Ask: "Show me architecture"
Ask: "What's the impact?"
→ Codebase-memory activates automatically

# Get compression
Responses auto-compressed by headroom
Token savings: 60-95%
```

---

## 🚀 QUICK START BY TOOL

### 1️⃣ CLAUDE CODE
```bash
# Type in Claude Code
/using-superpowers

# Then ask
"Where is authenticate function?"
```

### 2️⃣ GEMINI CLI
```bash
# Open gemini
gemini

# Type
/using-superpowers

# Then ask
"Build user profiles"
```

### 3️⃣ OPENCODE
```bash
# Open opencode
opencode

# Type
/using-superpowers

# Then ask
"Debug this error"
```

### 4️⃣ AGY
```bash
# Open agy
agy

# Type
/using-superpowers

# Then ask
"Show me the architecture"
```

---

## 📊 CONFIGURATION DETAILS

### Global Skills Directory
```
~/.agents/skills/
├── using-superpowers/         ← Framework
├── stop-slop/                 ← New
├── claude-mem/                ← New
├── codebase-memory/           ← Auto-integrated
├── (47 more skills)
└── ... (50 total)
```

### Claude Code Configuration
```
~/.claude/
├── settings.json              ← 50 skills configured
├── .mcp.json                  ← MCP servers (codebase-memory, headroom)
└── (documentation)
```

### Gemini Configuration
```
~/.gemini/
├── settings.json              ← Points to global skills
├── agents/
│   └── using-superpowers.md   ← Accessible here
└── (other config)
```

### OpenCode Configuration
```
~/.config/opencode/
├── settings.json              ← Points to global skills
├── agents/
│   └── using-superpowers.md   ← Accessible here
└── (other config)
```

### AGY Configuration
```
~/.agy/
├── settings.json              ← Points to global skills
├── agents/
│   └── using-superpowers.md   ← Accessible here
└── (other config)
```

---

## 🔄 HOW IT WORKS

### Unified Skills Access

```
All CLI Tools
    ↓
~/.agents/skills/ (global directory)
    ├── 50 skills (all available)
    ├── using-superpowers (framework)
    ├── codebase-memory (code graph)
    ├── headroom (compression) [Claude only]
    └── ...more
    ↓
Each tool:
    ├── claude: All features + headroom + MCP
    ├── gemini: All features (via settings.json)
    ├── opencode: All features (via settings.json)
    └── agy: All features (via settings.json)
```

### Key Points

✅ **Single Source of Truth**  
→ All skills stored in `~/.agents/skills/`  
→ All tools reference same location  

✅ **Auto-Triggering**  
→ Works across all tools  
→ Detects keywords and activates appropriate skill  

✅ **Consistent Experience**  
→ Same skills, same behavior  
→ Same auto-triggers across tools  

✅ **Easy Maintenance**  
→ Update once, works everywhere  
→ No per-tool duplication  

---

## 💡 USAGE EXAMPLES

### Example 1: Code Understanding (All Tools)

**Claude Code:**
```
/using-superpowers
→ "Where is PaymentProcessor?"
→ codebase-memory activates
→ Response compressed by headroom
```

**Gemini CLI:**
```
/using-superpowers
→ "Where is PaymentProcessor?"
→ codebase-memory activates
→ (same result, no headroom compression)
```

**OpenCode:**
```
/using-superpowers
→ "Show me the architecture"
→ codebase-memory activates
→ Full analysis available
```

### Example 2: Writing Polish (All Tools)

```
Any tool:
/using-superpowers
→ "Polish this documentation"
→ /stop-slop activates
→ Removes AI tells
→ More authentic prose
```

### Example 3: Memory Management (All Tools)

```
Any tool in long session:
/using-superpowers
→ "Compress memory"
→ /claude-mem activates
→ Memory compressed 60-95%
```

---

## 🔧 TECHNICAL SETUP

### File Locations Verified

✅ **Global Skills**  
```
~/.agents/skills/              → 50 skills installed
  ├── using-superpowers/       → Framework
  ├── codebase-memory/         → Code graph
  ├── headroom/                → (Claude only)
  ├── stop-slop/               → Writing quality
  ├── claude-mem/              → Memory compression
  └── (45 more)
```

✅ **Per-Tool Configuration**
```
~/.claude/settings.json        → Claude Code
~/.gemini/settings.json        → Gemini CLI
~/.config/opencode/settings.json → OpenCode
~/.agy/settings.json           → AGY
```

✅ **Agent Access**
```
~/.gemini/agents/using-superpowers.md
~/.config/opencode/agents/using-superpowers.md
~/.agy/agents/using-superpowers.md
```

---

## 📱 SUPPORTED FEATURES BY TOOL

| Feature | Claude | Gemini | OpenCode | AGY |
|---------|--------|--------|----------|-----|
| **50 Skills** | ✅ | ✅ | ✅ | ✅ |
| **using-superpowers** | ✅ | ✅ | ✅ | ✅ |
| **Codebase-Memory** | ✅ | ✅ | ✅ | ✅ |
| **Headroom Compression** | ✅ | ❌ | ❌ | ❌ |
| **Auto-Triggering** | ✅ | ✅ | ✅ | ✅ |
| **MCP Tools** | ✅ | Limited | Limited | Limited |

*Note: Headroom is Claude-specific for context compression*

---

## 🎯 RECOMMENDED WORKFLOWS

### Claude Code (Most Complete)
```
Recommended for:
  • Large projects
  • Complex analysis
  • Token optimization (headroom)
  • Full MCP support

Features:
  ✅ All 50 skills
  ✅ Codebase-memory
  ✅ Headroom compression
  ✅ MCP tools
  ✅ Max capabilities
```

### Gemini CLI (Fast)
```
Recommended for:
  • Quick questions
  • Fast iteration
  • Code exploration

Features:
  ✅ All 50 skills
  ✅ Codebase-memory
  ✅ Using-superpowers
  ✅ Lightweight
```

### OpenCode (Multi-Language)
```
Recommended for:
  • Multi-language support
  • IDE integration
  • Complex workflows

Features:
  ✅ All 50 skills
  ✅ Codebase-memory
  ✅ Using-superpowers
  ✅ IDE-aware
```

### AGY (Flexible)
```
Recommended for:
  • Custom workflows
  • Experimentation
  • Learning

Features:
  ✅ All 50 skills
  ✅ Codebase-memory
  ✅ Using-superpowers
  ✅ Flexible
```

---

## 🚀 GETTING STARTED

### Step 1: Verify Installation
```bash
# Check skills exist
ls ~/.agents/skills/ | grep -E "using-superpowers|codebase-memory|stop-slop|claude-mem"

# Expected output:
# using-superpowers
# codebase-memory
# stop-slop
# claude-mem
```

### Step 2: Start with Claude Code
```bash
# First, test in Claude Code
claude
# Type: /using-superpowers
# Ask any code question
```

### Step 3: Try Other Tools
```bash
# Try Gemini
gemini
# Type: /using-superpowers

# Try OpenCode
opencode
# Type: /using-superpowers

# Try AGY
agy
# Type: /using-superpowers
```

### Step 4: Use in Workflows
Each tool now has access to all 50 skills!

---

## 📚 DOCUMENTATION BY TOOL

### For Claude Code Users
→ `~/.claude/START-HERE-FINAL.md`  
→ `~/.claude/INSTALLATION-COMPLETE.md`

### For All Tools
→ `~/.claude/FULL-ECOSYSTEM-SUMMARY.md` (shared)  
→ `~/.claude/CODEBASE-MEMORY-INTEGRATION.md` (shared)  
→ `~/.claude/HEADROOM-INTEGRATION.md` (shared)  
→ `~/.claude/NEW-SKILLS-ADDED.md` (shared)

### For This Setup
→ This file: `MULTI-CLI-SETUP.md`

---

## ✅ VERIFICATION CHECKLIST

Run these to verify setup:

```bash
# 1. Check skills exist
ls ~/.agents/skills/ | wc -l
# Expected: 50+ (showing 50 skills)

# 2. Check global skills are accessible
ls ~/.agents/skills/using-superpowers/
# Expected: SKILL.md, references/

# 3. Check tool configurations
cat ~/.claude/settings.json | grep additionalDirectories
cat ~/.gemini/settings.json | grep additionalDirectories
cat ~/.config/opencode/settings.json | grep additionalDirectories
cat ~/.agy/settings.json | grep additionalDirectories

# 4. Check using-superpowers available in all tools
ls ~/.gemini/agents/using-superpowers.md
ls ~/.config/opencode/agents/using-superpowers.md
ls ~/.agy/agents/using-superpowers.md

# All should return paths (files exist)
```

---

## 🎉 YOU NOW HAVE

✅ **50 Professional Skills** in 4 CLI tools  
✅ **Code Intelligence** (codebase-memory) in all tools  
✅ **Skill Orchestration** (using-superpowers) in all tools  
✅ **Writing Quality** (stop-slop) in all tools  
✅ **Memory Compression** (claude-mem) in all tools  
✅ **Context Compression** (headroom) in Claude Code  
✅ **Unified Access** across all tools  
✅ **Single Skills Directory** for easy maintenance  

---

## 📞 TROUBLESHOOTING

### Skills Not Loading?
1. Restart the CLI tool
2. Verify: `ls ~/.agents/skills/using-superpowers/`
3. Check: `cat ~/.gemini/settings.json | grep additionalDirectories`

### Commands Not Working?
1. Ensure you have `/using-superpowers` loaded first
2. Try: `/using-superpowers`
3. Then: `/stop-slop` or other skill

### Codebase-Memory Not Found?
1. Restart CLI tool
2. Check: `.mcp.json` is configured (Claude only)
3. Verify: Executable at `~/.agy/Local/Programs/codebase-memory-mcp/`

### Headroom Not Working?
1. Claude Code only feature
2. Verify: `headroom --version`
3. Check: Port 8787 accessible

---

## 🎯 NEXT STEPS

1. **Restart all CLI tools** (pick up configurations)
2. **Try in each**: `/using-superpowers`
3. **Ask code questions**: "Where is X?"
4. **Use skills**: `/stop-slop`, `/claude-mem`, etc
5. **Enjoy**: Unified ecosystem across all tools!

---

## ✨ STATUS

🎉 **MULTI-CLI SETUP COMPLETE**

- All 4 CLI tools configured
- All 50 skills accessible everywhere
- Consistent experience across tools
- Documentation complete
- Production ready

**Go use your skills across all tools!** 🚀

