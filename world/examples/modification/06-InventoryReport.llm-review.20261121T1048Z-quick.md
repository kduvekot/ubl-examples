# LLM review: 06-InventoryReport.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/06-InventoryReport.xml`, Git blob `dc929df8dbd1039f02fceeaaaed95c2d652a6b3c` (committed)
- Last commit changing the example: fd97400c 2026-11-20 O255: wood and modification, story and XML brought into line
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

### modification/06#F1 · Medium · Tostara reports as "retailer" customer and the sawmill as seller, the reverse of the order
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Tostara Wood Modification`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- Why: An InventoryReport is "sent by a Buyer (for example a retailer) to a Seller (for example a producer)"; RetailerCustomerParty is "The retailer, who sends this message". Tostara is not a retailer and does not buy the slats: in the order it is the seller of the processing service (`01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Tostara Wood Modification`) and here it reports stock it holds for the owner. The sawmill sells nothing to Tostara. The roles carry a meaning other than their definitions, and they contradict the roles of the same two parties in 01, 07 and 08. InventoryReportingParty (Tostara) describes the reporter correctly.
- Condition: every party role in the report means what UBL defines it as, and agrees with the roles of the same parties elsewhere in the flow, or the story states why a custodian uses the retailer role.
- Options: (a) keep the InventoryReport (the only UBL document for a stock report) and record the role use as a semantic difference (the custodian takes the mandatory retailer role); (b) a different document for the stock held for the owner (for example a Receipt or a status document), if one fits better. Preferred: (a) with the difference recorded, since UBL offers no custodian role.
- Needs decision: yes

### modification/06#F2 · Low · The lot in the note of line 1 reads as the blanks' lot, which 03 numbers differently
- XPath: `/InventoryReport/cac:InventoryReportLine[1]/cbc:Note` = `Kiln charge 1, from the first load of blanks, lot MDS-L26-0119: modified, planed, sealed and bundled.`
- XPath: `03-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `MDS-BL26-0109`
- Why: The first load of blanks is lot `MDS-BL26-0109` in 03. `MDS-L26-0119` is the lot of the finished slats (the shipping marks of `wood/06-DespatchAdvice.xml` carry it, and 0119 matches the end of kiln charge 1 on 19 January in 02). The note's wording ("from the first load of blanks, lot …") attaches the lot to the blanks. The same holds for line 2 and `MDS-L26-0126`.
- Condition: each lot number in the report is clearly the lot of the item it is given for (output lot of the slats), and the blank lot, if mentioned, is the one in 03.
- Options: (a) preferred: word the notes as "output lot MDS-L26-0119, from the first load of blanks (lot MDS-BL26-0109)"; (b) carry the output lot in the Item's ItemInstance/LotIdentification and keep the note short.
- Needs decision: no

### modification/06#F3 · Low · Line 2 reports 48 bundles in stock that are not yet bundled
- XPath: `/InventoryReport/cac:InventoryReportLine[2]/cbc:Quantity` = `48`
- XPath: `/InventoryReport/cac:InventoryReportLine[2]/cbc:Note` = `Kiln charge 2, from the second load of blanks, lot MDS-L26-0126: modified; still being planed and sealed.`
- Why: InventoryReportLine/Quantity is "The quantity of the item reported that is currently in stock"; the item is a strapped bundle of 50 planed slats, which line 2's goods are not yet (still being planed and sealed, available 2026-02-04). The quantity is what the bundles will be, not what is in stock.
- Condition: line 2 states what is currently held (modified slats in process) or makes clear that the 48 bundles are expected stock.
- Options: (a) preferred: keep the line with its AvailabilityDate and state in the line that the quantity is expected output (the document allows stock that "will be" in stock); (b) report line 2 as 2,400 modified slats in process, a different item.
- Needs decision: no

## Checked and consistent
- 48 + 48 bundles = 96 bundles of 01; 96 × 50 = 4,800 = the two loads of 2,400 blanks; "no blank is left over" agrees.
- `/InventoryReport/cac:InventoryReportLine[2]/cbc:AvailabilityDate` = `2026-02-04` agrees with 02's "ready in store on 4 February".
- `/InventoryReport/cac:DocumentReference/cbc:ID` = `MDS-PO-26-0047` resolves to 01; "Job TWM-J-2526-014" is 01's SalesOrderID.
- SellersItemIdentification `MDS-SL-1800-50` is the sawmill's code, and the sawmill is the seller of this report.

## Outside this review
- The output lots `MDS-L26-0119` and `MDS-L26-0126` also appear in wood/06-DespatchAdvice.xml; whether the dates fit is a cross-flow timeline question.
