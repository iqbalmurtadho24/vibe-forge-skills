---
name: claude-mem
description: Persistent memory compression and management across sessions. Use when handling long sessions, context preservation, memory compression, or cross-session state.
metadata:
  repository: https://github.com/thedotmack/claude-mem.git
---

# Claude-Mem — Persistent Memory Compression

Persistent memory management and context compression system for AI coding agents.

## What It Does

Manages conversation memory and context efficiently across sessions:
- 💾 **Compresses conversation history**: Reduces memory footprint by 60–95%
- 🧠 **Persistent memory across sessions**: Preserves project decisions, key variables, and context
- 📚 **Integrates with Headroom compression**: Layered context optimization
- 🔄 **Smart memory management**: Rehydrates context on demand
- 📊 **Tracks memory usage**: Monitors token footprint over long conversations

## When to Use

- Long conversations (15+ interaction turns)
- Multi-session continuity needs
- Memory management and compression requests
- "Remember this for later" or recording persistent state
- Preventing token exhaustion in large codebases

## Core Workflow

```
Session 1: Store compressed memory
     ↓
Session 2: Retrieve compressed memory
     ↓
Rehydrate: Expand to full context only when needed
     ↓
Continue: Same context with 60–95% fewer tokens
```

## Commands & Direct Invocation

- `/claude-mem` — Compress and persist the current session memory state
- `/claude-mem status` — View current memory statistics and stored checkpoints
- `/claude-mem retrieve` — Load prior session context into the current workspace

## Best Practices

1. Save milestones at major development checkpoints.
2. Store key architecture decisions in memory before clearing large scratchpads.
3. Combine with Headroom for end-to-end token optimization.
