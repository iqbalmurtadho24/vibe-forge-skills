# ⚙️ Auto-Trigger Setup Guide - 48 Global Skills

## 🎯 Cara Kerja Auto-Trigger

Skills di-load secara **otomatis** ketika:
1. **Keyword Match** — Anda menyebut kata kunci yang relevan
2. **Context Detection** — Claude Code mendeteksi tipe pekerjaan
3. **Explicit Call** — Anda mengetik `/skill-name`

**NO NEED** untuk memanggil satu-satu atau konfigurasi manual!

---

## 🔄 Auto-Trigger Scenarios

### Scenario 1: Mulai Development Baru

**Anda:** "Saya mau build fitur login dengan multi-factor authentication"

**Auto-triggers:**
- `/using-superpowers` ← Framework
- `/brainstorming` ← Explore requirements
- `/writing-plans` ← Design approach
- `/test-driven-development` ← Test-first mindset

**Hasil:** Semua context sudah disiapkan, tinggal mulai code!

---

### Scenario 2: Bug dalam Code

**Anda:** "Ada error di authentication module, status 401 tidak konsisten"

**Auto-triggers:**
- `/systematic-debugging` ← Debug methodology
- `/receiving-code-review` ← Code examination
- `/verification-before-completion` ← Verify fix

**Hasil:** Debugging sudah terstruktur dengan sistematis!

---

### Scenario 3: Code Review PR

**Anda:** "Review PR ini sebelum merge"

**Auto-triggers:**
- `/requesting-code-review` ← Review framework
- `/ponytail-review` ← Check over-engineering
- `/receiving-code-review` ← Process feedback
- `/verification-before-completion` ← Final check

**Hasil:** Review komprehensif tanpa manual setup!

---

### Scenario 4: UI Needs Improvement

**Anda:** "Design ini terasa membosankan, gimana cara improve-nya?"

**Auto-triggers:**
- `/impeccable` ← UI polish
- `/ui-ux-pro-max` ← Design reference
- `/design-system` ← Token & specs
- `/ui-styling` ← Implementation

**Hasil:** Design guidance langsung tersedia!

---

### Scenario 5: Save Tokens

**Anda:** "Token usage saya tinggi, gimana cara hemat?"

**Auto-triggers:**
- `/caveman` ← Compressed mode (65% savings!)
- `/caveman-compress` ← Compress memory files
- `/cavecrew` ← Delegate dengan compression
- `/caveman-stats` ← Show metrics

**Hasil:** Token usage instantly optimized!

---

### Scenario 6: Security Testing

**Anda:** "Saya perlu penetration test untuk API ini"

**Auto-triggers:**
- `/penetration-testing-with-strix` ← Run pentest
- `/fix-security-vulnerabilities-with-strix` ← Patch findings
- `/ci-security-scanning-with-strix` ← Add to CI/CD

**Hasil:** Full security workflow!

---

## 🎯 Explicit Skill Calls

Kapan pun Anda butuh skill spesifik:

```bash
/using-superpowers              # Start with framework
/brainstorming                  # Explore ideas
/writing-plans                  # Create plan
/test-driven-development        # TDD approach
/systematic-debugging           # Debug issues
/verification-before-completion # Verify work
/requesting-code-review         # Get feedback
/receiving-code-review          # Process feedback

/penetration-testing-with-strix     # Security
/fix-security-vulnerabilities-with-strix
/ci-security-scanning-with-strix

/browser-use         # Browser control
/playwright-cli      # Testing
/remote-browser      # Remote automation

/impeccable          # Polish UI
/ui-ux-pro-max       # Design reference
/design              # Full design suite
/design-system       # Tokens & specs
/ui-styling          # Components

/caveman             # Compressed mode
/caveman-compress    # Compress files
/cavecrew            # Delegate+compress
/caveman-stats       # Token metrics

/ponytail            # Lazy mode
/ponytail-review     # Review cleanup
/ponytail-audit      # Full audit
/ponytail-debt       # Track shortcuts

/find-skills         # Discover more
/gstack              # GStack suite

/agent-eval          # CodeGraph benchmark
/add-lang            # Add language support
```

---

## 📊 Permission Configuration

### File: `~/.claude/settings.json`

```json
{
  "model": "haiku",
  "theme": "dark",
  "permissions": {
    "additionalDirectories": [
      "~/.agents/skills/add-lang",
      "~/.agents/skills/agent-eval",
      "~/.agents/skills/banner-design",
      "~/.agents/skills/brainstorming",
      "~/.agents/skills/brand",
      "~/.agents/skills/browser-use",
      "~/.agents/skills/cavecrew",
      "~/.agents/skills/caveman",
      "~/.agents/skills/caveman-commit",
      "~/.agents/skills/caveman-compress",
      "~/.agents/skills/caveman-help",
      "~/.agents/skills/caveman-review",
      "~/.agents/skills/caveman-stats",
      "~/.agents/skills/ci-security-scanning-with-strix",
      "~/.agents/skills/cloud",
      "~/.agents/skills/design",
      "~/.agents/skills/design-system",
      "~/.agents/skills/dispatching-parallel-agents",
      "~/.agents/skills/executing-plans",
      "~/.agents/skills/find-skills",
      "~/.agents/skills/finishing-a-development-branch",
      "~/.agents/skills/fix-security-vulnerabilities-with-strix",
      "~/.agents/skills/gstack",
      "~/.agents/skills/impeccable",
      "~/.agents/skills/managed-pentesting-with-strix",
      "~/.agents/skills/open-source",
      "~/.agents/skills/penetration-testing-with-strix",
      "~/.agents/skills/playwright-cli",
      "~/.agents/skills/ponytail",
      "~/.agents/skills/ponytail-audit",
      "~/.agents/skills/ponytail-debt",
      "~/.agents/skills/ponytail-gain",
      "~/.agents/skills/ponytail-help",
      "~/.agents/skills/ponytail-review",
      "~/.agents/skills/receiving-code-review",
      "~/.agents/skills/remote-browser",
      "~/.agents/skills/requesting-code-review",
      "~/.agents/skills/slides",
      "~/.agents/skills/subagent-driven-development",
      "~/.agents/skills/systematic-debugging",
      "~/.agents/skills/test-driven-development",
      "~/.agents/skills/ui-styling",
      "~/.agents/skills/ui-ux-pro-max",
      "~/.agents/skills/using-git-worktrees",
      "~/.agents/skills/using-superpowers",
      "~/.agents/skills/verification-before-completion",
      "~/.agents/skills/writing-plans",
      "~/.agents/skills/writing-skills"
    ]
  }
}
```

---

## ✨ Best Practices

### 1. Start Dengan `/using-superpowers`
Setiap session baru, mulai dengan skill ini:
```bash
/using-superpowers
```
Ini establish framework dan enable semua skills lainnya.

### 2. Follow Natural Workflow
Development workflow yang optimal:
```
brainstorming → writing-plans → test-driven-development 
→ subagent-driven-development → systematic-debugging 
→ verification-before-completion → requesting-code-review
```

### 3. Use Token Compression Proactively
Jika token usage tinggi:
```bash
/caveman              # Switch to compressed mode
/caveman-compress     # Compress old context/memory
/cavecrew             # Delegate dengan compression
```

### 4. Security by Default
Untuk production code:
```bash
/penetration-testing-with-strix
/ci-security-scanning-with-strix
/fix-security-vulnerabilities-with-strix
```

### 5. Code Quality Always
Code review sebelum merge:
```bash
/requesting-code-review   # Formal review
/ponytail-review          # Simplification check
/verification-before-completion  # Final verification
```

---

## 🔧 Troubleshooting

### Skills tidak auto-trigger?

**Check:**
1. Pastikan `settings.json` sudah update:
   ```bash
   cat ~/.claude/settings.json
   ```

2. Verify skills directory:
   ```bash
   ls ~/.agents/skills/ | wc -l
   ```
   Harus ada 48 direktori

3. Restart Claude Code setelah update `settings.json`

### Skill error saat triggered?

1. Pastikan Git installed:
   ```bash
   git --version
   ```

2. Refresh skills cache:
   ```bash
   rm -rf ~/.agents/skills/[skill-name]/.cache
   ```

3. Reinstall skill jika perlu:
   ```bash
   npx skills add [owner/repo@skill] -g -y
   ```

### Memory/Permission issues?

Check permissions di `settings.json`:
- Semua path harus dengan `~/`
- Gunakan `.agents/skills/` untuk global
- Harus lowercase dengan hyphen

---

## 📱 Available Everywhere

Skills berjalan di:
- ✅ Claude Code (CLI & IDE)
- ✅ Cursor
- ✅ OpenCode
- ✅ OpenHands
- ✅ Continue
- ✅ Cline
- ✅ CodeBuddy
- ✅ Windsurf
- ✅ Roo Code
- ✅ Zed
- ✅ JetBrains IDEs
- ✅ +65 more agents/CLIs

**Tidak perlu setup ulang di setiap tool!** ✨

---

## 🎓 Learning Resources

### Quick Start (5 minutes)
1. `/using-superpowers` — Understand framework
2. `/find-skills` — Explore available skills
3. `/caveman-help` — Learn compression

### Deep Dive (1 hour)
1. `/writing-plans` — Learn planning
2. `/test-driven-development` — TDD approach
3. `/systematic-debugging` — Debug methodology
4. `/requesting-code-review` — Review process

### Advanced (ongoing)
1. Explore skill combinations
2. Create custom workflows
3. Optimize token usage
4. Master UI/UX, Security, Browser automation

---

## 📞 Quick Help

| Need | Skill | Command |
|------|-------|---------|
| Start session | Using Superpowers | `/using-superpowers` |
| Plan feature | Writing Plans | `/writing-plans` |
| Debug issue | Systematic Debugging | `/systematic-debugging` |
| Review code | Requesting Code Review | `/requesting-code-review` |
| Polish UI | Impeccable | `/impeccable` |
| Test security | Strix Pentesting | `/penetration-testing-with-strix` |
| Save tokens | Caveman | `/caveman` |
| Simplify code | Ponytail | `/ponytail` |
| Find more | Find Skills | `/find-skills` |

---

**🚀 Setup Complete! All 48 skills ready for auto-triggering across all CLI tools!**
