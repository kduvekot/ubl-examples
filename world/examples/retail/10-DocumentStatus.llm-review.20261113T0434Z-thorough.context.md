# LLM review: 10-DocumentStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/10-DocumentStatus.xml`, Git blob `862ae5d80ac13b0164755f867566718b3cc3bf6b` (committed)
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

### retail/10#F1 · High · The status is issued before it was requested
- XPath: `/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `/DocumentStatus/cbc:Note` = `Accepted and booked.`
- Why: a DocumentStatus is "A document used to provide information about the status of a
  collaboration/process associated with a document"; in this flow it answers the request
  09-DocumentStatusRequest.xml ("Has the order been accepted?") about the same order on the same day.
  The answer is timed 11:14, 38 minutes before the question (11:52).
- Condition: the status is issued after the request it answers.
- Options: a status time after 11:52 (preferred), or an earlier request.
- Needs decision: no

### retail/10#F2 · Medium · A language code in LocaleCode
- XPath: `/DocumentStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/10#F3 · Low · Status "accepted" for the supplier's own transport request, without the carrier's answer
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:DocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:Response/cbc:ResponseCode` = `AP`
- Why: AdditionalDocumentResponse is "A document linked or related to the document for which the
  status was requested". `LD-TR-26-0227` is Lumeway's own transport execution plan request to Bayforth
  (11-TransportExecutionPlanRequest.xml); "Accepted" is not Lumeway's response to it but Bayforth's.
  Bayforth's answer, the plan `BF-TEP-26-0227` that 14-TransportationStatusRequest.xml refers to, is
  the document that shows the booking. The buyer is told of an internal request rather than of the
  booking the note mentions ("booked").
- Condition: the related document response is about a document whose status the sender can state,
  e.g. the carrier's plan that confirms the booking.
- Options: (a) refer to `BF-TEP-26-0227` (the accepted plan) instead of the request; (b) drop the
  additional response and keep "booked" in the note (preferred, the buyer needs no transport
  documents of its supplier).
- Needs decision: no

### retail/10#F4 · Low · Signature and master data a status message does nothing with
- XPath: `/DocumentStatus/cac:Signature/cbc:ID` = `LD-SIG-26-DS`
- XPath: `/DocumentStatus/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/DocumentStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the signature has only an ID and a signatory; the status message uses none of the share
  capital, tax schemes, customs trader number or social-media profile (IND5/IND6).
- Condition: everything present has a use here.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- DocumentResponse refers to the order `BS-PO-26-0224` (08-Order.xml) with response code `AP`
  (Accepted), matching the note; sender and receiver are the seller and the buyer.
- The status (2026-04-26) is issued the day after the transport request it mentions (2026-04-25).
