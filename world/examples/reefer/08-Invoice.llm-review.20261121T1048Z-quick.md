# LLM review: 08-Invoice.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/08-Invoice.xml`, Git blob `c7d20b45ee6e5d88b12d8df022cbdd47656fbf73` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### reefer/08#F1 · Low · Delivery stated at the buyer's cold store, the CIP terms left out
- XPath: `/Invoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Hafefo Fresh Produce, cold store, Selanu`
- Why: the sale is CIP Port of Selanu (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIP`, place `XLSEL`, repeated in `02-OrderResponse.xml` and `07-BillOfLading.xml`): the seller's price covers carriage and insurance to the port, and the road leg from the port to the cold store is the buyer's own on-carriage by Nalevi Warehousing (`07-BillOfLading.xml`). The invoice names the cold store as the delivery location and carries no delivery terms, so it reads as if the seller delivered to the buyer's door, and nothing in it says that the 28,868.00 includes ocean freight and insurance — which `05-ExportCustomsDeclaration.xml` (export value deducted for freight) and `09-ImportCustomsDeclaration.xml` (landed value = invoice value) rely on.
- Condition: the invoice's delivery information agrees with the contract terms: the delivery location (if given) is the CIP place or is clearly the final destination, and the CIP terms with their place are stated.
- Options: (a) add `cac:DeliveryTerms` CIP Port of Selanu and give the port as the delivery location (preferred); (b) keep the cold store but mark it as the final destination in the note and add the delivery terms.
- Needs decision: no

## Checked and consistent
- 672 × 26 = 17,472.00; 280 × 24.5 = 6,860.00; 168 × 27 = 4,536.00; sum 28,868.00 = line extension = tax exclusive = tax inclusive = payable; category G, 0 %, exemption EXP, as in the order and response.
- Late payment: 1.5 % × 28,868.00 = 433.02 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `433.02` (a month's surcharge); penalty period starts the day after the due date.
- Due date: 30 days from Thursday 23 April is Saturday 23 May; the next working day is Monday 25 May, the due date given; `12-RemittanceAdvice.xml` pays on 25 May.
- Payee account: IBAN-like check digits pass; bank code `BLUM` and branch `387120` in the account agree with the branch and bank given; the same account is in `12-RemittanceAdvice.xml`. RF reference `RF88HRWINV260772` passes ISO 11649.
- References: order `26-0215` and despatch advice `HRW-DA-26-0764` resolve; despatch date 22 April agrees with `06-DespatchAdvice.xml`. The preferential origin statement (criterion P) agrees with `09-ImportCustomsDeclaration.xml`.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:Name` = `Marrowdale branch`: the cooperative is in Harrowmead — refuted: a business may bank at a branch in a nearby town, and the account, branch and bank agree with each other and with the remittance advice.
- `/Invoice/cac:OrderReference/cbc:ID` = `26-0215`: the invoice follows the response's quantities but cites the order — refuted: the order is the document the response answers, and the lines reference the order lines; the open question of the buyer's acceptance is reefer/02#F1.
