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
2. **XSD Valid**: Conformance to XML Schema Definition (UBL 2.5 spec)
3. **Semantically Correct**: Sample data and contents are realistic and meaningful

### Example Party Data (identifiers, addresses, contacts)

Identifiers and contact data in sample documents must never belong to a real
organisation or person. Take them from the **Global Test Data** set:

- Site: https://sipico.github.io/global-test-data/
- Machine-readable: https://sipico.github.io/global-test-data/data/all.json
- Source and rules: https://github.com/sipico/global-test-data

Rules:

1. **Use a Global Test Data value whenever one is usable** for the element:
   status `reserved`, `published-example` (and it passes the checks the document
   needs) or `derived`. Never use a value with status `avoid`.
2. **If no usable value fits**, a different value may be used, but record **why**
   (which element, what was missing or unsuitable, and how the replacement was
   chosen and checked) in the document's notes or in `analysis/`. Where the
   replacement is generally useful, propose it to Global Test Data with its source.
3. Keep the `ubl:` hints in the data (element and `schemeID`) consistent with how
   the value is used in the document.

### Reference Resources

- [OASIS UBL 2.5 CSD02](https://docs.oasis-open.org/ubl/csd02-UBL-2.5/)
- [Peppol UBL Invoice Documentation](https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/)
- [Global Test Data](https://sipico.github.io/global-test-data/): safe example identifiers per country

---

*Last updated: 2026-11-05*
