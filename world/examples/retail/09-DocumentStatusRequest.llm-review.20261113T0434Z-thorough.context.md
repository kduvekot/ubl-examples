# LLM review: 09-DocumentStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/09-DocumentStatusRequest.xml`, Git blob `68cae595b7754cc365ebfdb3b09245cd84b8e2fc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/09#F1 · High · The status request is sent after the status it asks for
- XPath: `/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `/DocumentStatusRequest/cbc:IssueDate` = `2026-04-26`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `/DocumentStatusRequest/cbc:Note` = `Has the order been accepted?`
- Why: a DocumentStatusRequest is "A document used to request the status of a collaboration/process
  associated with a document"; 10-DocumentStatus.xml is the answer (same order, same day, "Accepted
  and booked."). The answer was issued at 11:14, the question at 11:52. Either the buyer asks about
  a status it has already received, or the answer predates the question.
- Condition: the request is issued before the status that answers it.
- Options: a request time before 11:14 (or a status time after 11:52) (preferred); the times are
  this flow's only link between the two documents.
- Needs decision: no

### retail/09#F2 · Medium · A language code in LocaleCode
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/09#F3 · Low · Signature and master data a status request does nothing with
- XPath: `/DocumentStatusRequest/cac:Signature/cbc:ID` = `BM-SIG-26-DSR`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: a one-line question about an order's status needs neither a signature (here only an ID and a
  signatory, no method or attachment) nor share capital, tax schemes, a customs trader number or a
  social-media profile of the parties (IND5/IND6).
- Condition: everything present has a use in the request.
- Options: drop them; keep identification, name and electronic address.
- Needs decision: no

## Checked and consistent
- RequestedDocumentReference `BS-PO-26-0224` resolves to 08-Order.xml (issued 2026-04-24); sender
  Brightmarket and receiver Lumeway are the order's buyer and seller.
- TrackingID `BS-PO-26-0224` identifies the process by the order number, which is a legitimate
  tracking identifier for an ordering process.
