# LLM review: 13-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/13-ReceiptAdvice.xml`, Git blob `604fd2f166bf65e6e949e78ef14e8423b7c4b8ad` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/13#F1 · Low · The accepted extra side frame is never billed, returned or declared
- XPath: `/ReceiptAdvice/cbc:DeliveryAcceptanceCode` = `ACCEPTED`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `13`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:OversupplyQuantity` = `1`
- XPath: `15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `12`
- XPath: `17-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:Quantity` = `12`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `717.60`
- Why: Receipt Line. Oversupply Quantity is "The quantity over-supplied, i.e., the quantity over and above the quantity ordered." The corrected receipt accepts the whole delivery, including one side frame (worth 5 980 XUF at the order price) that was picked twice at the 3PL (`/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box more than despatched: picked twice at the 3PL.`). No document of the flow settles it: the invoice bills 12, the remittance pays the invoice in full and nothing more, no return, debit note or invoice correction follows, and the import declaration values 12 units, so one unit crossed into Bayvarra without customs value. The documents do not contradict each other on their own terms, but the money side of the flow leaves the accepted extra unit unaccounted for.
- Condition: The flow says what happens to the over-supplied side frame in money terms: it is billed (and declared at import), or returned to the seller, or the acceptance excludes it, and the receipt advice, invoice and import declaration agree with that.
- Options: (a) the receipt does not accept the extra unit and says it is held for return to the 3PL (preferred: it fits "picked twice", needs no further document, and leaves the invoice, the payment and the import value right); (b) Valdara bills the 13th unit with a further invoice or debit note and the import declaration is corrected to 13; (c) the receipt records the unit as kept free of charge, with a note.
- Needs decision: yes

## Checked and consistent
- The invoice bills what was ordered and despatched (12 = `04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cbc:DeliveredQuantity` = `12`), and all 96 benches received here are billed (`15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `96`), so the full payment of 4 862 160 XUF is right for the ordered goods.
