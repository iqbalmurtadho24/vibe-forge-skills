# 🧠 Headroom Context Compression Integration

**Status**: ⏳ **INSTALLATION IN PROGRESS**

---

## 🎯 What is Headroom?

**Headroom** is a context compression layer for AI agents that:
- **Saves 60-95% tokens** (for JSON data)
- **Saves 15-20% tokens** (for coding agents)
- Works as **library, proxy, agent wrapper, or MCP server**
- Supports **43+ coding agents** (Claude, Cursor, Codex, Grok, etc)
- **Reversible compression** — originals cached locally
- **Smart learning** — mines failed sessions, writes corrections to CLAUDE.local.md

---

## 📊 Key Features

| Feature | Benefit |
|---------|---------|
| **ContentRouter** | Auto-detect JSON/code/prose, pick best compressor |
| **SmartCrusher** | Compress JSON structures |
| **CodeCompressor** | AST-based code compression |
| **Kompress-v2-base** | ML-based text compression (Hugging Face) |
| **CacheAligner** | Protect prompt cache from volatile content |
| **CCR** | Reversible compression with local cache |
| **headroom learn** | Auto-mine failed sessions for corrections |

---

## 🛠️ Installation Methods

### Method 1: Global CLI Tool (Recommended)
```bash
uv tool install --python 3.13 "headroom-ai[all]"
# Or
pip install "headroom-ai[all]"
```

### Method 2: Python Library
```python
from headroom import compress
result = compress(messages)
```

### Method 3: TypeScript SDK
```typescript
import { compress } from 'headroom-ai';
const result = await compress(messages);
```

### Method 4: Proxy Server
```bash
headroom proxy --port 8787
# Then point your agent to http://localhost:8787
```

### Method 5: Agent Wrapper
```bash
headroom wrap claude      # Claude Code
headroom wrap cursor      # Cursor
headroom wrap codex       # Codex
headroom wrap grok        # Grok
headroom wrap cline       # Cline
headroom wrap continue    # Continue
```

### Method 6: MCP Server
```bash
headroom deploy  # Turnkey local deployment + config
```

---

## 💾 Modes of Operation

### 1. **Inline Library**
Use in your own code:
```python
from headroom import compress

messages = [...]
compressed = compress(messages)
# Send compressed to LLM
```

### 2. **Drop-in Proxy**
No code changes:
```bash
headroom proxy --port 8787
# Point any HTTP client to localhost:8787
```

### 3. **Agent Wrapper**
Wrap existing agent:
```bash
headroom wrap claude      # Wraps Claude Code
# Changes automatically applied
# Undo with: headroom unwrap claude
```

### 4. **MCP Server**
```bash
headroom deploy
# Provides:
# - headroom_compress
# - headroom_retrieve  
# - headroom_stats
```

---

## 🔗 Integration with using-superpowers

When headroom is active:

```
Your code question
      ↓
/using-superpowers + codebase-memory
      ↓
Response (code context + architecture)
      ↓
Headroom compresses output
      ↓
Send to LLM (60-95% fewer tokens!)
```

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **JSON Compression** | 60-95% |
| **Code Compression** | 15-20% |
| **Tool Output Reduction** | 50-70% |
| **Log Compression** | 60-80% |
| **Reversibility** | 100% (cached) |
| **Languages Supported** | Python, TypeScript, Go, Rust, Java, C++, etc |
| **Setup Time** | 2-5 minutes |

---

## 🎯 Use Cases

### Case 1: Large Codebase Context
```
Normal: 50,000 tokens for large file + code context
With Headroom: 5,000-10,000 tokens
```

### Case 2: API Response Handling
```
Normal: 10,000 tokens for JSON response
With Headroom: 1,000-4,000 tokens
```

### Case 3: Conversation History
```
Normal: 30,000 tokens for 100-turn conversation
With Headroom: 5,000-15,000 tokens
```

### Case 4: Tool Outputs
```
Normal: 20,000 tokens for test results + logs
With Headroom: 3,000-8,000 tokens
```

---

## 🔄 Cross-Agent Memory

Headroom provides **shared memory across agents**:

```
Claude Code uses Headroom
     ↓
Stores compressed context in shared store
     ↓
Cursor also uses Headroom
     ↓
Accesses same store, auto-deduplicates
     ↓
All agents have consistent context
```

---

## 🧠 headroom learn

Auto-correct from failed sessions:

```bash
headroom learn

# Reads: failed Claude Code sessions
# Mines: what went wrong
# Writes: corrections to CLAUDE.local.md
# Auto: prevents same failure next time
```

---

## 🚀 Recommended Setup

### For Claude Code + using-superpowers:

```bash
# 1. Install
pip install "headroom-ai[all]"

# 2. Wrap Claude
headroom wrap claude

# 3. Verify
headroom status
```

### Configuration (Optional)
```yaml
# ~/.headroom/config.yaml
compression:
  level: high           # high / medium / low
  preserve: ["important", "api_keys"]
  
mcp:
  enabled: true
  port: auto
  
learning:
  enabled: true
  output_file: CLAUDE.local.md
```

---

## 🔌 Integration Points

### With codebase-memory-mcp
```
codebase-memory → returns architecture/code context
         ↓
    Headroom → compresses for LLM
         ↓
    LLM → gets full context, fewer tokens
```

### With caveman mode
```
caveman (token-aware) → needs compression anyway
         ↓
    Headroom → provides additional savings
         ↓
    Result: 65% (caveman) + 20-60% (headroom) = best compression
```

---

## 📊 Compression Comparison

| Input Type | Before | After | Savings |
|-----------|--------|-------|---------|
| Large JSON | 50K tokens | 5K tokens | 90% |
| Code file | 30K tokens | 5K tokens | 83% |
| API response | 10K tokens | 1.5K tokens | 85% |
| Test output | 20K tokens | 3K tokens | 85% |
| Log file | 15K tokens | 3K tokens | 80% |
| Conversation | 30K tokens | 8K tokens | 73% |

---

## 🎨 Architecture

```
┌─────────────────────────────────────────┐
│          Your Claude Code                │
│       (or any coding agent)              │
└────────────────┬────────────────────────┘
                 │ prompts, tool outputs
                 ▼
    ┌──────────────────────────────┐
    │     Headroom Compress        │
    ├──────────────────────────────┤
    │  ContentRouter               │
    │  ├─ SmartCrusher (JSON)      │
    │  ├─ CodeCompressor (AST)     │
    │  └─ Kompress-v2 (text/prose) │
    │                              │
    │  CacheAligner → CCR          │
    │  (reversible + local cache)  │
    └────────────┬─────────────────┘
                 │ 60-95% fewer tokens
                 ▼
    ┌──────────────────────────────┐
    │      LLM (Anthropic, etc)    │
    │   Gets full context, reduced │
    │        token cost            │
    └──────────────────────────────┘
```

---

## 🔐 Privacy & Security

- ✅ **Local-first** — runs on your machine
- ✅ **No data sent to external services**
- ✅ **Cache stored locally** — you control it
- ✅ **Reversible** — always access originals
- ✅ **Open-source** — audit everything
- ✅ **Privacy-preserving** — doesn't expose internals

---

## 📚 Quick Reference

```bash
# Install
pip install "headroom-ai[all]"

# Wrap agent (automatic)
headroom wrap claude

# Check status
headroom status

# Manual compression
headroom compress --file large_output.json

# Learn from failures
headroom learn

# Unwrap agent (if needed)
headroom unwrap claude

# Start MCP server
headroom deploy

# Proxy mode
headroom proxy --port 8787
```

---

## ✨ Status

🔄 **Installation in progress** via pip...

Once complete, we'll:
1. ✅ Wrap Claude Code automatically
2. ✅ Configure with codebase-memory-mcp
3. ✅ Enable headroom learn
4. ✅ Add to using-superpowers workflow
5. ✅ Test combined token savings

---

## 🎯 Next Steps

1. Wait for pip installation to complete
2. Run: `headroom wrap claude`
3. Update `.mcp.json` to include headroom server
4. Integrate with using-superpowers
5. Enable `headroom learn` for auto-corrections

