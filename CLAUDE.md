# Claude Code Configuration for ubl-examples

This document describes the development environment setup, tools, and workflows for the `ubl-examples` project.

## Project Overview

`ubl-examples` is a repository for validated sample documents for UBL (Universal Business Language), an ISO/IEC 19845 standard that defines standardized electronic business documents for supply chain, procurement, and transportation.

---

## Development Tools

### GitHub CLI (gh) Installation

The project is configured to automatically install GitHub CLI on session start, with security verification and automatic version checking.

#### Installation Setup

- **Location**: `.claude/scripts/install-gh-with-version-check.sh`
- **Hook Configuration**: `.claude/settings.json`
- **Automatic Trigger**: Runs on every Claude Code session start

#### Features

- **Secure Downloads**: Downloads from official GitHub releases with HTTPS and TLS 1.2+
- **Checksum Verification**: Performs mandatory SHA256 verification of downloaded binaries
- **Version Management**:
  - Default behavior: **AUTO mode** fetches the latest stable release
  - Override: Set `GH_SETUP_VERSION` environment variable to pin a specific version (e.g., `GH_SETUP_VERSION=2.87.0`)
- **Update Checks**: Non-blocking periodic checks for newer versions (cached for 24 hours)
- **Installation**: Installs to `~/.local/bin/gh` and updates your PATH automatically

#### Using GitHub CLI in Commands

Most gh commands that work with repositories use the `-R` or `--repo` flag:

```bash
# List pull requests
gh pr list --repo kduvekot/ubl-examples

# List issues
gh issue list --repo kduvekot/ubl-examples

# View repository info
gh repo view kduvekot/ubl-examples

# Create a PR
gh pr create --repo kduvekot/ubl-examples --title "..." --body "..."
```

#### Version Management

To check the current installed version:
```bash
gh --version
```

To force installation of a specific version, set the environment variable:
```bash
export GH_SETUP_VERSION=2.87.0
```

To always use the latest stable release (default):
```bash
export GH_SETUP_VERSION=AUTO
```

---

## Session Memory Tool

A session data extraction tool is available at `.claude/scripts/claude-memory` for analyzing conversation history and session metadata.

### Usage

```bash
.claude/scripts/claude-memory <command> [options]
```

### Commands

- **`conversation`** - Structured JSON of user/assistant exchanges (no tool results)
  - Use to reconstruct decisions and agreements from a session
  - `--last N` - Show only last N entries
  - `--user-only` - Show only user messages
  - `--truncate N` - Truncate each entry to N characters

- **`search <query>`** - Case-insensitive search across all conversation content
  - Returns matching entries as a JSON array with count

- **`topics`** - Index of sessions by first user message
  - Shows what was discussed across different `.jsonl` files

- **`tokens`** - Token usage totals and estimated cost (USD)
  - Provides API call counts, tokens used, and cost breakdown

- **`full`** - All conversation entries including tool results
  - Same options as `conversation` command

### Examples

```bash
# Summarize the conversation
.claude/scripts/claude-memory conversation

# Search for a specific topic
.claude/scripts/claude-memory search "invoice"

# Get last 10 user messages
.claude/scripts/claude-memory conversation --user-only --last 10

# Check session costs
.claude/scripts/claude-memory tokens
```

### When to Use

- **After context compression**: Use `conversation` or `search` to reconstruct important decisions
- **Finding specific discussions**: Use `search` with relevant keywords
- **Cost tracking**: Use `tokens` to see session spending
- **Session indexing**: Use `topics` to see what was worked on across files

---

## Git Workflow

This project uses feature branches for all development work.

### Branch Naming

- Format: `claude/<descriptive-name>-<session-id>`
- Example: `claude/research-ubl-samples-3IuwR`
- All development must occur on these designated branches

### Commit Strategy

- Create clear, descriptive commit messages
- Keep commits focused on specific changes
- Include session reference in commit messages when applicable

### Push to Remote

Always push to the correct branch:
```bash
git push -u origin <branch-name>
```

The branch name must start with `claude/` and include the session ID to authorize the push.

---

## UBL Sample Documents

The `ubl-examples` repository should contain validated sample XML documents for various UBL document types.

### Common Document Types to Include

**Core Business Process:**
- Invoice (most common)
- Purchase Order
- Order Response
- Despatch Advice
- Receipt Advice
- Credit Note
- Debit Note

**Sourcing:**
- Quotation
- Request for Quotation
- Catalogue

**Fulfillment:**
- Packing List
- Bill of Lading
- Waybill

**Billing:**
- Reminder
- Self-Billed Invoice

### Reference Resources

- [OASIS UBL 2.3 Standard](https://docs.oasis-open.org/ubl/UBL-2.3.html)
- [Peppol UBL Invoice Documentation](https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/)
- [Tradeshift UBL Examples](https://github.com/Tradeshift/tradeshift-ubl-examples)

---

## Environment Variables

Optional environment variables for customizing behavior:

```bash
# GitHub CLI version (default: AUTO for latest)
GH_SETUP_VERSION=2.87.0        # or "AUTO"

# Version checking
GH_CHECK_UPDATES=true          # Enable/disable update checks
GH_VERSION_CHECK_CACHE_HOURS=24 # Cache duration for version checks
```

---

## Security Notes

- All GitHub CLI downloads are verified with SHA256 checksums
- Installation uses HTTPS with TLS 1.2+ enforcement
- Binary is installed to a user-accessible directory with proper permissions
- Installation method is deterministic and auditable via logs
- Never run with `--no-verify` flags unless explicitly authorized

---

## Session Workflow

1. **Session Start**:
   - GitHub CLI is automatically installed/verified
   - Scripts in `.claude/scripts/` are available for use

2. **Development**:
   - All changes committed to the designated feature branch
   - Use `gh` CLI for repository operations

3. **Context Management**:
   - Use `.claude/scripts/claude-memory` to track session progress
   - After compression, run `search` for specific topics to recover detail

4. **Documentation**:
   - Keep this file updated as new tools or workflows are added
   - Record important decisions and agreements

---

## Quick Reference

| Tool | Location | Purpose |
|------|----------|---------|
| gh CLI | `~/.local/bin/gh` | GitHub operations |
| gh installer | `.claude/scripts/install-gh-with-version-check.sh` | Auto-install gh CLI |
| Session memory | `.claude/scripts/claude-memory` | Extract & analyze session history |
| Config | `.claude/settings.json` | Hook configurations |

---

## Troubleshooting

### gh CLI not found
- The installation script runs on session start
- Check `.claude/settings.json` is configured with the SessionStart hook
- Verify `~/.local/bin` is in your PATH

### Session memory script not working
- Ensure it's executable: `chmod +x .claude/scripts/claude-memory`
- Requires Python 3.6+
- Session files must exist in `~/.claude/projects/`

### Version check warnings
- These are non-blocking and safe to ignore
- To suppress, set `GH_CHECK_UPDATES=false`
- To update, set `GH_SETUP_VERSION=AUTO` for automatic latest, or pin a version

---

*Last updated: 2026-02-19*
