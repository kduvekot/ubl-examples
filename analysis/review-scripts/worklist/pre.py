T = 'title'
E = 'elements'
PRE = [
    ('CONTRACTTERMS', {T: r'transport plan|contradicts? the (payment term|contract)|as the contract says|instead of the contract|contract.s payment terms'}),
    ('DUEDATE', {T: r'due date|days net|\b(30|45) days'}),
    ('CONTRACTTERMS', {T: r'payment term.*(plan|contract)|(plan|contract).*payment term|settlement discount.*(net|contract)|agreed payment term'}),
    ('PENALTYMONTH', {T: r'one-month penalty|penalty period of one month|per month late'}),
    ('MAPSCALE', {T: r'kilomet|nautical|\bnm\b|\bkm\b|map|coordinates'}),
    ('ISSUETIME', {T: r'(issued|issue time).*(before|after|later|earlier)|before (it|the .*) (is|was) issued|after the .* (was|is) issued|minutes later|hours (before|later)|not yet (issued|exist)|could not yet exist|reports? .*after|"actual".*after|actual .* after|later document|issued later|after its own issue'}),
    ('TARIFF', {T: r'national tariff|Urvanian (national )?tariff|tariff code'}),
    ('ITEMCOPY', {T: r'product sheet|customs values on a certificate|customs values in a packing list'}),
    ('CUSTOMSGOODS', {T: r'customs value (is not|without a reference)|invoice the customs value rests on|shipment-level customs'}),
    ('CUSTOMSVALUE', {T: r'customs value|declared value|export value|statistical value'}),
    ('WEEKEND', {T: r'Saturday|Sunday|weekend'}),
    ('KNOCKDOWN', {T: r'assembled|knocked|do(es)? not fit (the )?(pallet|trailer|container|truck)|fit (on|in) (a|the|one) (pallet|trailer|container|truck)'}),
]
POST = [
    ('LOCNAME', {T: r'(location|place|origin|destination|from and to|issue location|status location|notification location|AtLocation).*(named after|names? the|is the|company|carrier|consignee|business address|office)'}),
    ('LOCNAME', {T: r'named after (the |a )?compan'}),
    ('COSTCENTRE', {T: r'cost cent|cost account|booked (as|to)|charged to the buyer|AccountingCost'}),
    ('COSTCENTRE', {E: r'^AccountingCost'}),
    ('ISIC', {T: r'industry classification|classified as wired|ISIC'}),
    ('DESPDATES', {T: r'despatch advice.*(neither|without|does not say|states neither|no despatch)|advice (says|states) neither|advice does not say when|despatch itself is not described'}),
    ('ORDERDATES', {T: r'(order|change).*(no requested|states no|without a collection|gives no requested)|no requested (pick-up|delivery)'}),
    ('INVLINK', {T: r'invoice (says nothing|is not linked)|(invoice|zero-rating).*(no delivery|without delivery)|delivery of the service has no date|not linked to the despatch'}),
    ('REMIT', {T: r'payment order|referenced twice on (the|the same) line|line repeats the header|line-level parties repeat'}),
    ('TEPTERMS', {T: r'(late-payment|late-delivery).*(penalty|surcharge|percentage)|surcharge element .*penalty|post-event|stationary|waiting-time|commission|(plan|request) does not say what|does not say in structured form what|not say what is (to be )?carried'}),
    ('CUSTOMSGOODS', {T: r'(packages|transport mode|mode or means).*(not declared|border)|goods item quantity is a weight|packages of the goods item|customs value (is not tied|is not linked|without a reference)|carries no packages'}),
    ('ITEMPROP', {T: r'validity (period )?on the property|Length repeated|commercial specification|full commercial specification'}),
    ('ITEMCOPY', {T: r'(customs classification|classification and origin) .*domestic'}),
    ('MASTERCOPY', {T: r'(permit|licence|bank account|account).*(in (a|an|the)|on (a|the))\b'}),
    ('ROLEDUP', {T: r'notifier is the importer|named as the party to be notified|CustomerParty is the same|repeat the contracting party|originator and beneficiary|repeated as notifier|own addressee'}),
    ('TEMPCODE', {T: r'temperature code'}),
    ('JOURNEY', {T: r'voyage number in the element|regular service schedule'}),
    ('GROSSWT', {T: r'GrossWeightMeasure. equals|gross weight is goods plus packaging'}),
]
PRE += [
    ('ISSUETIME', {T: r'revision (time|date).*(after|before) the issue|accepted before it was lodged|passed before the goods arrived|invoiced .* before the goods were received|before any receipt'}),
]
POST += [
    ('MASTERCOPY', {T: r'stock-exchange listing'}),
    ('REMIT', {T: r'(accounting|line-level) parties repeat|referred to twice in the same line|referenced twice'}),
    ('WAYBILLTYPE', {T: r'\bCMR\b|\bCIM\b|consignment note for (goods sent|a carriage)|"consignment note" in an air|on the consignment note. in an air|road consignment note'}),
    ('CUSTOMSISSUER', {T: r'customs (administration )?(as|named as) issuer|declared by the exporter itself|3PL declares'}),
    ('FORWARDER', {T: r'freight forwarder.*consolidat|as freight forwarder \(consolidator\)|forwarder role'}),
    ('TEPSERVICE', {T: r'(container-train|container train|full truck load|bulk).*(service|ore|cargo|plan)|service.*contradicts the plan|freight invoiced as bulk|bulk-wagon freight'}),
    ('TEPPERIOD', {T: r'(pickup|pre-arrival notification period|transport window).*(before|ends before)|lies before the (period|transport)'}),
    ('HANDLINGUNIT', {T: r'pallet (listed as|lists itself)|package quantity used|contained in itself|lists itself as the one package'}),
    ('LINEID', {T: r'line ID|reuses line|same line ID|line ID 1 used twice|carries the ID of the order|refers to the bench line'}),
]
PRE += [
    ('TAXO', {T: r'(category|tax) O (with|and) a (rate|percent) of 0|0 % on a category|rate 0 % on a category'}),
    ('FXRATE', {T: r'(pricing|alternative|payment alternative|requested invoice) currency|currency .*without (a reason|an amount)|payable alternative amount'}),
]
POST += [
    ('FARMADDR', {T: r'address lines repeat'}),
    ('FARMREG', {T: r'expiry date on|yearly expiring registration|commercial-register entry'}),
    ('BALE', {T: r'PackSizeNumeric. 227|PackSizeNumeric 227|nominal bale weight'}),
    ('CLASSING', {T: r'classing results'}),
    ('WAYBILLTYPE', {T: r'on the consignment note'}),
    ('EVENTS', {T: r'events? (without|with date and time but no|has no time)|without (a )?place|generic (event|events)|"additional" (free-text )?event|loading reported (in generic|only as)|acceptance reported as a generic|arrival is a generic|waypoints without'}),
    ('PLACES', {T: r'named (but|,)? ?not identified|named without the identifier|only (by|as) (name|description|text)|identified by description only|only described, not identified|named, not identified|without its UN/LOCODE|without the airport|description only'}),
    ('TRANSPORTCONTENT', {T: r'(request|instructions|booking|plan|waybill|bill|manifest|consignment note|report|itinerary).{0,40}(do(es)? not (say|describe|list)|without (goods|an arrival|places)|that does not (say|list))'}),
    ('TRANSPORTCONTENT', {T: r'does not say (what|between|how)|not say what is|does not describe the goods|does not list the cargo|without goods, container|not say what is carried'}),
    ('PREVDECL', {T: r'previous (customs )?declaration|previous version of this export|"No previous procedure"'}),
    ('CUSTOMSOFFICE', {T: r'(exit|entry|border) office|office of entry|customs office in|inland (border )?office|exit office'}),
    ('ADVALOREM', {T: r'AdValorem|ad valorem|declared (for )?carriage value|value declared for carriage'}),
    ('INCOPLACE', {T: r'(DAP|FOB|EXW|CPT|CIF|FCA|delivery|Incoterm).{0,30}(place|location).{0,40}(text|description|free text)|named place .*text|place (given )?only as text|delivery places only as text|delivery location described only'}),
    ('ITEMCOPY', {T: r'product sheet'}),
    ('ZEROTAX', {T: r'tax total of (zero|0)|zero tax without|zero total of allowances'}),
]
PRE += [
    ('TAXO', {T: r'(a )?0 % rate (on|with)|exemption reason given for a levy'}),
    ('SUPPLYTYPE', {T: r'supply of services|supply type|SupplyTypeCode'}),
    ('DEBITROLES', {T: r'(creditor and debtor|accounting supplier and customer) (are )?(reversed|the reverse)|supplier as creditor and the department as debtor|entered as a credit, while the debit|deducted as a credit, while the debit'}),
]
POST += [
    ('REMIT', {T: r'references the same invoice twice|payment purpose|purpose "supplier payment"|payment-order references'}),
    ('ROLEDUP', {T: r'repeats the (receiver|sender|contracting|party|line)|roles all filled with|repeats the contracted carrier|stated twice, identical to the seller|PerformingParty in the sub-lines repeats|addressee listed again|BeneficiaryParty repeats|source issuer repeats'}),
    ('FURNBRAND', {T: r"maker's brand|own-line item carries"}),
    ('MASTERCOPY', {T: r'tax scheme (of the contracting authority )?in a|contracting authority.s tax scheme'}),
    ('CONTESTAMT', {T: r'54,000 lume'}),
    ('PROCNOTICE', {T: r'NoticeTypeCode|requested legal form|DurationPeriod of the reference|CandidateReductionConstraintIndicator|PublishAwardIndicator|only state the default|declared as (a|an additional) language|NoticeLanguage|does not refer to the contract notice|refers to the prior information notice but not|links the prior information notice but not|points to "the contest notice"|not identify the contract notice'}),
    ('PROCQUAL', {T: r'fulfilment indicator|FulfilmentIndicator|exclusion grounds|self-declaration|does not refer to the request it answers|evidence (is )?not linked|same (text|sentence) (twice|as response)|group.s lead role|lists its other member|BusinessIdentityEvidenceID|scored reference criteria|reference criteria of the request are not answered|"Expected" amounts|indicator property|property groups typed|Properties typed as requirements|same limit stated twice'}),
    ('UTILSTMT', {T: r'AverageAmount|average amount|SupplierConsumption|SubscriberID|Subscriber type|SubscriberType|descriptions without information|filler descriptions|delivery location that only points back|district-heating|ConsumptionEnergyQuantity|energy consumer level|meter constant|maximum flow'}),
]
F = 'flow'
PRE += [
    ('KNOCKDOWN', {T: r'pallet said to hold 24 benches'}),
    ('TENDERDATES', {F: ['tender'], T: r'(period|periods|availability).*(before|after) the (notice|procedure|call|award)|before the (notice|procedure)|inside the appeal period|last day (of|on which) (the )?appeal|appeal period is the award|after the period for requests|came after the period'}),
]
POST += [
    ('TENDERCOLOUR', {F: ['tender'], T: r'moss green|grey variant|standard grey|special-colour|new colour'}),
    ('TENDERINSTALL', {F: ['tender'], T: r'installers'}),
    ('TENDERTERMS', {F: ['tender'], T: r'security clearance|guarantee of 2400|guarantee.s amount|turnover (criterion|threshold)|subcontract|variants?|VariantConstraint|paper copies|paper-copy|reimbursement fee|request lines?|minimum and maximum amount|unit prices as minimum|penalty clause|framework (values|agreement)|electronic auction|OriginalContractingSystemID|money terms|As for the procedure|quality criterion|technical committee|consortium lead|tender preparation|design-contest|design contest|invitations and requests|invitation and participation|advertisement amount|strategic-procurement|repeats the instructions|performance guarantee|tender-phase terms'}),
    ('TENDERPROJECT', {F: ['tender'], T: r'Lot 2|lot 2|installation lot|additional classification|quality control|budget account|estimates? (equal|made)|equals the buyer.s estimate|project (is named|has another name)|programme (has another|code)|named "… for'}),
    ('TENDERCOLOUR', {F: ['tender'], T: r'moss green|grey variant|standard grey|special-colour|colour charge|new colour'}),
    ('TENDERINSTALL', {F: ['tender'], T: r'installation|installers'}),
    ('TENDERTAX', {F: ['tender'], T: r'tax representative|withholding'}),
    ('REFID', {T: r'referenced under an ID|under (an ID|identifiers) (no|that)|ID no document|identifiers no document|under an ID that is not|"replaced notice"|replaced notice is named|does not exist|exists nowhere|resolves nowhere|that no example contains|cannot be linked|lead nowhere|not in the flow|appears nowhere else'}),
]
def nn(a, b):
    return [f'{i:02d}' for i in range(a, b + 1)]
PRE += [
    ('REGDATE', {T: r'years in (operation|business).*registered|years in business against a registration'}),
    ('DUTIES', {T: r'duties (said to be )?paid|"Duties paid"|duty or tax|import consumption tax|duties and (import )?tax|duties claimed'}),
    ('NUMBERING', {T: r'document numbers? (do not follow|ahead of)|numbers out of order|numbered (after|before)'}),
]
POST += [
    ('ITEMCOPY', {T: r'catalogue record'}),
    ('REFTYPE', {T: r'with only an ID|do not say what they refer to|says nothing about what it is|reference does not say what it is|does not say what it is'}),
    ('CATALOGUE', {T: r'"Active"|Active" as the status|status "Active"|CatalogueIndicator'}),
    ('CATTERRITORY', {T: r'sales territory'}),
    ('ORDERREFS', {T: r'SalesOrderID|sales order number in the buyer|release (number|identifier).*(ReleaseID|delivery-access|no other example)|CustomerReference'}),
    ('PROCNOTICE', {T: r'declared as (an )?additional language'}),
    ('PROCQUAL', {F: ['tender'], 'docs': nn(6, 7)}),
    ('TENDERQUALIF', {F: ['tender'], 'docs': ['04', '05', '08', '09', '10', '11', '12', '13']}),
    ('TENDERGUAR', {F: ['tender'], T: r'guarantee|immobili|ontology URI'}),
    ('TENDERBIDS', {F: ['tender'], 'docs': nn(15, 19)}),
    ('TENDERAWARD', {F: ['tender'], 'docs': nn(20, 23)}),
    ('TENDERCALLOFF', {F: ['tender'], 'docs': nn(24, 36)}),
]
PRE += [
    ('CONTRACTTERMS', {T: r'payment terms contradict the freight invoice'}),
    ('TAXABLEALLOW', {T: r'taxable amount (ignores|leaves out)|outside the taxable amount|anticipated total and the tax base'}),
    ('MELT', {T: r'manufacture date|manufactured a day later|registration ID for castings|RegistrationID on castings|melt'}),
    ('STOCKCHAIN', {T: r"distributor's stock|from stock. to a farm|from stock\b"}),
]
POST += [
    ('INVLINK', {T: r'export exemption without|exemption without the evidence'}),
    ('MASTERCOPY', {T: r'customs numbers'}),
    ('PRIVACY', {T: r'confidential|confidentiality and security|PrivacyCode|security classification'}),
    # --- flow stories ---
    ('ENERGYPIPE', {F: ['energy'], T: r'shipment|2400 MWh|consigned|export declaration of the same gas|for which period the gas|imported by nobody'}),
    ('AIRSTORY', {F: ['air'], T: r'flight|CPT|CIF|delivery slot|cancel|replacement|acceptance|validity period on an unconditional|order reference contradicts|road feeder'}),
    ('AIRPACK', {F: ['air'], T: r'box|weight|volume|consolidat|substitute carrier|consignor-assigned|requested. events|special security|waybill numbers|anticipated total'}),
    ('ORESTORY', {F: ['ore']}),
    ('PLASTICSCERT', {F: ['plastics'], T: r'recycled-content certificate'}),
    ('WOODUNIT', {F: ['wood'], T: r'OrderableUnitFactorRate|per thousand slats'}),
]
POST += [
    ('REFKIND', {T: r'(given|cited|referenced|referred to) as (a|an|the) (delivery note|despatch advice|receipt advice|billing document|contract)|as the order.s contract|cited as the contract|quotation.s document number used as a contract|as a contract identifier'}),
    ('MASTDG', {F: ['mast'], T: r'placard|fissile|activity of one|hazardous|battery|PI 965|orange plates|danger level|cargo-aircraft|CAO|dangerous|mode-specific|emergency|transport data'}),
    ('MASTAIR', {F: ['mast']}),
    ('CARNET', {F: ['carnet']}),
    ('WASTESTORY', {F: ['waste']}),
    ('CONTESTSTORY', {F: ['contest']}),
    ('COTTONCLASS', {F: ['cotton'], T: r'classing|phytosanitary|sampled|previous version|certificate'}),
    ('COTTONSELFBILL', {F: ['cotton'], 'docs': ['01', '02', '03', '04', '05', '06', '07']}),
    ('COTTONSEA', {F: ['cotton'], 'docs': ['08', '09', '11', '12', '13', '14', '15', '16', '17', '18']}),
    ('FURNSCM', {F: ['furniture'], 'docs': ['03', '04', '05', '06', '07']}),
    ('FURNPUBLIC', {F: ['furniture'], 'docs': ['15', '16', '17']}),
    ('FURNORDER', {F: ['furniture']}),
    ('ENERGYISOL', {F: ['energy']}),
    ('PLASTICSISOL', {F: ['plastics']}),
    ('WOODISOL', {F: ['wood']}),
    ('PACKAGINGISOL', {F: ['packaging']}),
    ('AIRPACK', {F: ['air']}),
]
PRE += [
    ('TAXO', {T: r'tax rate of 0 % on a levy'}),
]
POST[0:0] = [
    ('ROLEDUP', {T: r'header contract parties repeated'}),
    ('ROADSUBST', {F: ['road'], T: r'substitut|2026 casting|old casting|extra side frame'}),
    ('ROADCOO', {F: ['road'], T: r'certificate reference resolves'}),
    ('UTILEXCISE', {F: ['utilities'], T: r'excise|energy tax'}),
    ('UTILESTIMATE', {F: ['utilities'], T: r'estimate correction|correction unit'}),
]
POST += [
]
POST[0:0] = [
    ('PAYNOTE', {T: r'payment note calls|called "Invoice" in the payment note|calls the sales order an invoice'}),
    ('CATALOGUE', {T: r'full.container. discount|percentage of the bench|dependent price'}),
    ('SEAVOYAGE', {F: ['sea'], T: r'still an estimate|reporting positions|requested arrival differs'}),
    ('SEACIF', {F: ['sea'], T: r'CIF|freight|insur|deductible|pre-carriage|final delivery haulage|confirmed payable amount|policy'}),
]
POST += [
    ('ROADCOO', {F: ['road'], 'docs': ['06', '07'], T: r'.'}),
    ('RETAILCAT', {F: ['retail'], 'docs': ['01', '02', '03', '04', '20']}),
    ('RETAILPROMO', {F: ['retail'], 'docs': ['05', '06', '07', '21']}),
    ('RETAILTRANSPORT', {F: ['retail'], 'docs': ['11', '12', '13', '14', '15', '16', '17']}),
    ('UTILTELECOM', {F: ['utilities'], 'docs': ['12', '13', '14']}),
    ('SEAAGREE', {F: ['sea'], 'docs': ['01', '03', '04']}),
    ('SEASHIP', {F: ['sea'], 'docs': ['13', '14', '15', '16', '17']}),
    ('SEAFINANCE', {F: ['sea'], 'docs': ['22', '23', '24', '25', '26', '27', '28']}),
    ('UTILWATER', {F: ['utilities'], 'docs': ['05', '08', '09', '10', '11'], T: r'levy|on account|mandate|PayerParty|bank account|payment reference|fee|credit'}),
]
POST += [('ROADISOL', {F: ['road']}), ('RETAILISOL', {F: ['retail']}), ('UTILISOL', {F: ['utilities']}), ('RAILISOL', {F: ['rail']}), ('SEAISOL', {F: ['sea']})]
