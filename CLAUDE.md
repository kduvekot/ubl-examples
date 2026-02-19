# Claude Code Configuration for ubl-examples

This document describes the development environment setup, tools, and workflows for the `ubl-examples` project.

## Project Overview

`ubl-examples` is a repository for validated sample documents for UBL (Universal Business Language), an ISO/IEC 19845 standard that defines standardized electronic business documents for supply chain, procurement, and transportation.

---

## Development Tools

### GitHub CLI (gh)

GitHub CLI is automatically installed on session start. When using gh commands that support repositories, always include the `--repo` flag:

```bash
gh pr list --repo kduvekot/ubl-examples
gh issue create --repo kduvekot/ubl-examples --title "..." --body "..."
```

### Session Memory Tool

A session data extraction tool is available at `.claude/scripts/claude-memory`. Run with `--help` to see all commands and usage patterns:

```bash
.claude/scripts/claude-memory --help
```

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

The `ubl-examples` repository contains validated sample XML documents for various UBL document types.

### Validation Requirements

Sample documents must meet three validation criteria:

1. **XML Valid**: Proper XML structure and syntax
2. **XSD Valid**: Conformance to XML Schema Definition (UBL 2.3 spec)
3. **Semantically Correct**: Sample data and contents are realistic and meaningful

Note: Maintain backwards compatibility with UBL 2.3 samples as the standard evolves toward UBL 2.5.

### Reference Resources

- [OASIS UBL 2.3 Standard](https://docs.oasis-open.org/ubl/UBL-2.3.html)
- [Peppol UBL Invoice Documentation](https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/)

---

*Last updated: 2026-02-19*
