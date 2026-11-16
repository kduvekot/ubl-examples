T = 'title'
E = 'elements'
V = 'values'

from pre import PRE, POST

RULES = PRE + [
    # --- party master data / encoding -------------------------------------------------------------
    ('LOCALE', {E: r'\bLocaleCode\b'}),
    ('LOCALE', {T: r'LocaleCode|locale'}),
    ('REGION', {E: r'^Region$|\bRegion\b', T: r'province|Region'}),
    ('REGION', {T: r'province.*Region|Region.*province'}),
    ('GATE', {T: r'\bgate\b', E: r'AdditionalStreetName'}),
    ('GATE', {T: r'gate.*(street|address)|AdditionalStreetName'}),
    ('REGDATE', {T: r'1996|registration date|registered on 1 January|founding'}),
    ('REGDATE', {E: r'RegistrationDate', T: r'default|same date|shared'}),
    ('REGDATE', {T: r'\b(SMALL|LARGE|MEDIUM|MICRO)\b|size class|small enterprise|large enterprise|EntitySizeCode|employees'}),
    ('PUBBODY', {T: r'(public bod|customs|authority|chamber|department|council|board|administration|service|register).*(compan|commercial register|liquidation)'}),
    ('PUBBODY', {E: r'CompanyLiquidationStatusCode|CorporateRegistrationTypeCode'}),
    ('EXEMPTWORD', {T: r'exemption reason.*(sale|transaction|worded)|worded as a (sale|transaction)'}),
    ('LANGTAG', {T: r'tagged|en-X[BUL]|Italian|untagged|language tag|legal form.*(rendering|English|without)|rendering'}),
    ('WEEKEND', {T: r'Saturday|Sunday|weekend|weekday|office hours|contact hours|hours its contact'}),
    ('CONTACT', {E: r'JobTitle|Department', T: r'contact|desk|officer|job|department|sales|buying|purchasing'}),
    ('CONTACT', {T: r'contacts?\b', 'not_title': r'emergency|signatory|means of contact|SignatoryContact|notifier'}),
    ('STOCK', {E: r'CorporateStockAmount', T: r'share capital|CorporateStockAmount|number of shares'}),
    ('FXRATE', {T: r'exchange rate'}),
    ('REFTYPE', {T: r'referenced by ID only|with (an |only an )?ID only|ID only'}),
    ('ITEMCOPY', {T: r'(catalogue|product.passport|item).{0,25}(data|description)'}),
    ('MASTERCOPY', {T: r'master data|does nothing with|copied into|does not use|nothing to do with|logo|web ?site|social media|stock listing|share capital|tax registration|customs[- ]trader'}),
    # --- item data -------------------------------------------------------------------------------
    ('EMISSION', {E: r'ValueFactorNumeric|ValueBaseMeasure'}),
    ('EMISSION', {T: r'emission (factor|value).*(base|factor)|factor.*base'}),
    ('FULLNESS', {E: r'FullnessIndicationCode|LifecycleStage'}),
    ('FULLNESS', {T: r'FullnessIndication|system boundary|cradle|lifecycle stage|life-cycle stage'}),
    ('GTIN', {T: r'GTIN|GS1 (company )?prefix|item number.*(real|valid)'}),
    ('HSFRAME', {T: r'general cast article|side frame classified'}),
    ('HSFRAME', {T: r'732599|side frame.*(HS|classif|heading)|9401'}),
    ('ITEMCOPY', {T: r'(item|product|catalogue|passport).*(data|master).*(copied|does nothing|not use)|item master data|product data|catalogue data'}),
    # --- signatures, statuses, references --------------------------------------------------------
    ('DERIVEDID', {T: r'(signature|identifier|ID).*(flow|example number|file number|aggregate name|repeats the carrier prefix|unrelated to the document|derived)'}),
    ('PREFIX2', {T: r'prefix that is not|prefix.*not the'}),
    ('SIGNATURE', {T: r'signature', 'not_title': r'before the agreement|BF'}),
    ('NOSTATUS', {T: r'NoStatus|"No status"'}),
    ('REFTYPE', {T: r'(reference|referenced).*(only an ID|ID only|without (a )?(document )?type|no document type|type code)'}),
    ('FXRATE', {T: r'exchange rate|ExchangeRate'}),
    ('SHIPORDER', {E: r'ShippingOrderID'}),
    ('SHIPORDER', {T: r'ShippingOrderID'}),
    ('GROSSWT', {T: r'gross weight.*(container|equipment|tare|without)|(container|equipment|tare).*gross weight'}),
    ('ORIGINALS', {T: r'three originals|originals'}),
    ('TAXO', {T: r'(category|tax) .?O\b.*goods|outside (the )?scope.*goods|Services outside scope'}),
    ('TAXO', {T: r'0 % rate on tax category O|tax scheme without an identifier|tax that does not exist|No general sales tax'}),
]
RULES += POST

MANUAL = {}
MANUAL.update({
    'cotton/10#F17': 'COTTONCLASS',
    'conditions#F1': 'CATTERRITORY', 'conditions#F2': 'DUEDATE', 'conditions#F3': 'CONTRACTTERMS',
    'conditions#F4': 'TENDERTAX', 'conditions#F5': 'CUSTOMSVALUE', 'conditions#F6': 'DUTIES',
    'conditions#F7': 'WEEKEND', 'conditions#F8': 'TENDERTAX', 'conditions#F9': 'PENALTYMONTH',
    'conditions#F10': 'TARIFF', 'conditions#F11': 'PRICECHAIN', 'conditions#F12': 'REGDATE',
    'timelines#F1': 'MAPSCALE', 'timelines#F2': 'MELT', 'timelines#F3': 'ISSUETIME', 'timelines#F4': 'STOCKCHAIN',
    'timelines#F5': 'SEAVOYAGE', 'timelines#F6': 'ISSUETIME', 'timelines#F7': 'SEAISOL', 'timelines#F8': 'ISSUETIME',
    'equipment#F1': 'KNOCKDOWN', 'parties#F1': 'SELANUNAME', 'parties#F2': 'REGDATE',
    'items#F1': 'STOCKCHAIN', 'items#F2': 'GTIN', 'items#F3': 'BENCHWEIGHT', 'items#F4': 'REPLACEITEM',
    'identifiers#F1': 'PREFIX', 'identifiers#F2': 'NUMBERING', 'identifiers#F3': 'PROFILEEXEC',
    'identifiers#F4': 'DERIVEDID', 'identifiers#F5': 'PREFIX2',
})
MANUAL.update({
    # corrections after reading the rule results
    'ore/05#F10': 'REFTYPE', 'rail/06#F16': 'REFTYPE', 'plastics/04#F12': 'MASTERCOPY', 'plastics/04#F20': 'MASTERCOPY',
    'air/03#F10': 'SHIPORDER', 'energy/04#F12': 'JOURNEY', 'sea/08#F2': 'SEAISOL',
    'utilities/07#F1': 'NUMBERING', 'utilities/14#F1': 'NUMBERING',
    'road/10#F12': 'CUSTOMSGOODS', 'sea/19#F11': 'CUSTOMSGOODS', 'plastics/08#F6': 'PLASTICSISOL', 'waste/03#F1': 'WASTESTORY',
    'tender/13#F1': 'TENDERQUALIF', 'tender/01#F2': 'TENDERDATES', 'tender/03#F1': 'TENDERDATES', 'tender/21#F12': 'TENDERDATES',
    'packaging/08#F4': 'PACKAGINGISOL', 'retail/17#F12': 'RETAILTRANSPORT', 'furniture/11#F4': 'FURNORDER',
    'retail/18#F2': 'RETAILISOL', 'rail/02#F3': 'RAILISOL', 'rail/03#F3': 'RAILISOL',
    'mast/02#F14': 'LANGTAG', 'mast/03#F14': 'LANGTAG', 'mast/04#F11': 'LANGTAG', 'mast/05#F7': 'LANGTAG', 'sea/05#F8': 'LANGTAG',
    'plastics/01#F7': 'LANGTAG', 'mast/04#F6': 'WAYBILLTYPE', 'retail/13#F7': 'WAYBILLTYPE', 'air/03#F5': 'WAYBILLTYPE',
    'tender/04#F5': 'TENDERTERMS', 'tender/06#F4': 'PROCQUAL', 'tender/06#F5': 'PROCQUAL', 'tender/07#F6': 'PROCQUAL',
    'tender/21#F14': 'TENDERPROJECT', 'tender/26#F13': 'FXRATE', 'tender/32#F14': 'FXRATE', 'tender/33#F14': 'FXRATE',
    'air/08#F8': 'AIRSTORY', 'air/10#F6': 'AIRPACK', 'contest/02#F3': 'CONTESTSTORY', 'contest/09#F8': 'CONTESTSTORY',
    'contest/16#F11': 'CONTESTSTORY', 'retail/18#F12': 'REFID', 'waste/01#F15': 'REFTYPE', 'waste/02#F9': 'REFTYPE',
    'air/04#F5': 'TRANSPORTCONTENT', 'ore/02#F2': 'TRANSPORTCONTENT', 'ore/03#F6': 'TRANSPORTCONTENT',
    'plastics/04#F6': 'TRANSPORTCONTENT', 'wood/04#F4': 'TRANSPORTCONTENT', 'rail/10#F3': 'CONTRACTTERMS',
    'rail/04#F3': 'RAILISOL', 'energy/04#F4': 'ENERGYPIPE', 'energy/05#F5': 'ENERGYPIPE',
    'utilities/12#F5': 'ROLEDUP', 'utilities/12#F10': 'COSTCENTRE', 'utilities/13#F8': 'TAXO',
    'utilities/08#F11': 'MASTERCOPY', 'utilities/10#F6': 'MASTERCOPY', 'utilities/09#F10': 'ROLEDUP',
    'sea/25#F7': 'ZEROTAX', 'sea/25#F8': 'ROLEDUP', 'sea/27#F6': 'ROLEDUP', 'sea/26#F5': 'REFKIND', 'sea/28#F7': 'REFKIND',
    'sea/25#F12': 'REFTYPE', 'sea/13#F3': 'REFID', 'sea/13#F5': 'EVENTS', 'sea/13#F9': 'PLACES', 'sea/13#F10': 'MASTERCOPY',
    'sea/14#F18': 'EVENTS', 'sea/14#F19': 'PLACES', 'sea/16#F22': 'PLACES', 'sea/17#F4': 'EVENTS', 'sea/17#F5': 'EVENTS',
    'sea/16#F19': 'EVENTS', 'sea/15#F3': 'TRANSPORTCONTENT', 'sea/18#F4': 'COSTCENTRE', 'sea/03#F1': 'ISSUETIME',
    'sea/04#F8': 'MASTERCOPY', 'road/06#F12': 'MASTERCOPY', 'ore/03#F11': 'TEPTERMS',
    'retail/21#F10': 'MASTERCOPY', 'retail/21#F11': 'LOCNAME', 'retail/06#F12': 'LOCNAME', 'sea/29#F8': 'LOCNAME',
    'sea/06#F2': 'GROSSWT',
})
MANUAL.update({
    'tender/18#F2': 'REFID', 'utilities/13#F2': 'UTILTELECOM', 'cotton/04#F20': 'COTTONSELFBILL',
    'air/07#F14': 'ROLEDUP', 'carnet/01#F19': 'ITEMCOPY', 'utilities/08#F13': 'UTILISOL',
})
