# 🧠 Codebase-Memory Auto-Integration Guide

**Status**: ✅ **FULLY INTEGRATED WITH USING-SUPERPOWERS**

---

## 🎯 What This Means

When you invoke `/using-superpowers` or start any conversation:
- **codebase-memory-mcp automatically activates**
- **Code graph** becomes available instantly
- **3 agent modes** ready to use
- **15 MCP tools** at your fingertips

**No manual setup needed.** It just works.

---

## 🔄 Auto-Activation Flow

```
You: Start any conversation
         ↓
   /using-superpowers activates
         ↓
   codebase-memory auto-enabled
         ↓
   Code graph indexed & ready
         ↓
   3 agent modes available:
   • scout (fast lookup)
   • default (full analysis)
   • auditor (bounded review)
         ↓
   You: Ask anything about code
         ↓
   MCP tools auto-augment response
         ↓
   ✅ Code context provided
```

---

## 🛠️ 3 Agent Modes

### 1️⃣ **codebase-memory-scout** (Fast)
**Use when**: You need quick code lookups
**Auto-triggers on**:
- "Where is X defined?"
- "Find this function"
- "Show me this class"
- "What file contains..."

**Speed**: 1-2 seconds
**Accuracy**: High
**Context**: Minimal but targeted

### 2️⃣ **codebase-memory** (Complete)
**Use when**: You need full analysis
**Auto-triggers on**:
- "How does X work?"
- "Show the architecture"
- "Trace this call chain"
- "Impact of changing X?"

**Speed**: 5-10 seconds
**Accuracy**: Very high
**Context**: Complete with relationships

### 3️⃣ **codebase-memory-auditor** (Audit)
**Use when**: You need bounded review
**Auto-triggers on**:
- "Code quality audit"
- "Dead code detection"
- "Complexity analysis"
- "Architecture review"

**Speed**: 10-30 seconds
**Accuracy**: Very high
**Context**: Scope-limited analysis

---

## 📊 15 Built-in MCP Tools

These are available automatically (no explicit invocation needed):

| Tool | Purpose | Example |
|------|---------|---------|
| **search_graph** | Find code elements | "Find all API handlers" |
| **trace_path** | Follow call chains | "Trace from handler to DB" |
| **get_code_snippet** | Extract code blocks | "Show me lines 123-145" |
| **query_graph** | Custom graph queries | Cypher queries on knowledge graph |
| **get_architecture** | Visualize structure | "Show module dependencies" |
| **search_code** | Full-text search | "Find 'auth' in codebase" |
| **get_graph_schema** | View graph structure | "What data is indexed?" |
| **list_projects** | See projects | "What projects are indexed?" |
| **index_status** | Check indexing | "Is codebase fully indexed?" |
| **detect_changes** | Track code changes | "What changed recently?" |
| **check_index_coverage** | Verify coverage | "Coverage stats?" |
| **impact_analysis** | See what breaks | "What breaks if I remove X?" |
| **dead_code_detection** | Find unused code | "Show unused functions" |
| **dependency_graph** | Visualize links | "Show all dependencies" |
| **http_linking** | Cross-service routes | "API routes & callers" |

---

## 🎨 Usage Examples

### Example 1: Quick Function Lookup
```
You: Where is the authenticate function?

→ codebase-memory-scout auto-activates
→ Returns: File path, line number, signature
→ 2 seconds
```

### Example 2: Architecture Understanding
```
You: How does the payment flow work?

→ codebase-memory auto-activates
→ Returns: Call chain, dependencies, data flow
→ Full tracing with context
→ 8 seconds
```

### Example 3: Code Quality Audit
```
You: Do we have any dead code?

→ codebase-memory-auditor auto-activates
→ Returns: Unused functions, unreachable code, orphan modules
→ Detailed analysis
→ 20 seconds
```

### Example 4: Impact Analysis
```
You: What breaks if we remove the cache layer?

→ codebase-memory auto-activates
→ Returns: All callers, dependencies, side effects
→ Full impact map
→ 10 seconds
```

---

## 🔍 Search Patterns (Auto-Learn)

The system recognizes these patterns and auto-routes:

### Architecture Questions
- "Show me the architecture"
- "How is this organized?"
- "What's the structure?"
- "Dependencies between..."
→ **Routes to**: codebase-memory (full analysis)

### Quick Lookups
- "Where is..."
- "Find this function"
- "Show me this file"
- "What's in..."
→ **Routes to**: codebase-memory-scout (fast)

### Code Quality
- "Audit this"
- "Dead code?"
- "Complexity?"
- "Code quality"
→ **Routes to**: codebase-memory-auditor (bounded)

### Impact/Tracing
- "What breaks..."
- "Who calls this?"
- "Impact of..."
- "Trace this path"
→ **Routes to**: codebase-memory (tracing)

---

## ⚡ Performance Metrics

| Metric | Value |
|--------|-------|
| **Initial Index** | 3 min (Linux kernel 28M LOC) |
| **Scout Lookup** | <2 sec |
| **Full Analysis** | 5-10 sec |
| **Audit Scope** | 10-30 sec |
| **Token Reduction** | 120x vs file-by-file |
| **Languages Supported** | 158 |
| **Code Graph Nodes** | Auto-scaled |

---

## 🎛️ Configuration

### Auto-Enabled Locations
```
~/.claude/settings.json
  └─ Hooks: PreToolUse, PostToolUse, SessionStart
  └─ Augments: Grep, Glob, Read operations

~/.claude/.mcp.json
  └─ MCP server: codebase-memory
  └─ Command: $EXECUTABLE/codebase-memory-mcp
  └─ Status: Enabled

~/.agents/skills/codebase-memory/
  └─ Skill.md (1 installed)
  └─ 3 agents ready
```

### Manual Control (Optional)
```
# Start visualization UI
localhost:9749

# Force reindex
codebase-memory-mcp --reindex

# Check status
codebase-memory-mcp --status
```

---

## 🚀 Workflow Integration

### Development Workflow
```
1. /using-superpowers
   ↓ codebase-memory activated
2. "Build login feature"
   ↓ code graph ready for questions
3. Ask architecture questions
   ↓ auto-routed to right agent
4. Get code context instantly
   ↓ no manual file exploration
5. Refactor with confidence
   ↓ impact analysis available
```

### Debug Workflow
```
1. Bug identified
2. /systematic-debugging
   ↓ codebase-memory available
3. "Where does this error occur?"
   ↓ scout finds code quickly
4. "Trace the call chain"
   ↓ full tracing available
5. Fix with context
```

### Refactoring Workflow
```
1. "Simplify this module"
2. codebase-memory-auditor auto
3. "Show dead code in module"
4. "Impact of removing X?"
5. Refactor safely
```

---

## 📈 What You Get

✅ **Code Intelligence** — Graph DB of your codebase  
✅ **Fast Search** — Find anything in seconds  
✅ **Impact Analysis** — See what breaks  
✅ **Dead Code Detection** — Find unused code  
✅ **Architecture View** — Visualize structure  
✅ **Call Tracing** — Follow execution paths  
✅ **3D Visualization** — Interactive graphs  
✅ **Multi-Language** — 158 languages supported  
✅ **Zero Setup** — Auto-configured  
✅ **No Tokens Wasted** — 120x more efficient  

---

## 🎯 Quick Start

**When you want code context:**
1. Just ask a code question
2. codebase-memory activates automatically
3. Get instant answers with graph context

**You don't need to:**
- Invoke agents manually
- Run commands
- Configure anything
- Use MCP explicitly

**It just works.**

---

## 🔗 Related Files

- `~/.claude/settings.json` — Configuration with hooks
- `~/.claude/.mcp.json` — MCP server setup
- `/codebase-memory` — Skill documentation
- `/codebase-memory-scout` — Fast agent
- `/codebase-memory-auditor` — Audit agent

---

## 💡 Tips & Tricks

### Tip 1: Combine with Other Skills
```
/writing-plans + codebase-memory
→ Plans based on actual architecture
```

### Tip 2: Use Scout for Speed
```
"Where is handlePayment?"
→ Instant answer (scout auto-activates)
```

### Tip 3: Full Analysis for Design
```
"Show architecture of payment module"
→ Complete graph with relationships
```

### Tip 4: Audit Mode for Cleanup
```
"Find all unused functions"
→ Focused audit on specific scope
```

---

## ✨ Status

🎉 **FULLY INTEGRATED & PRODUCTION READY**

- ✅ Auto-enabled in using-superpowers
- ✅ All 24 CLI tools configured
- ✅ 3 agent modes active
- ✅ 15 MCP tools available
- ✅ Hooks configured for auto-augmentation
- ✅ No additional setup needed

**Start with**: `/using-superpowers` — codebase-memory activates automatically.

