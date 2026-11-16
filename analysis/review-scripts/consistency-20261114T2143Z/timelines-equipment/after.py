import csv,re
T='/home/user/ubl-examples/.review/tables/'
docs={(d['flow'],d['file']):d for d in csv.DictReader(open(T+'documents.csv'))}
past=re.compile(r'^(Actual|Acceptance|Loading|Discharge|Takeover|Pickup|Delivery|Handling|Positioning|Examination|Exportation|Quarantine|Detention|Receipt|Storage|Warehousing|Dropoff|Availability|TransportEvent|OptionalTakeover)')
fut=re.compile(r'^(Estimated|Planned|Requested|Updated)')
for r in csv.DictReader(open(T+'dates.csv')):
    if not r['element'].endswith('Date'): continue
    d=docs[(r['flow'],r['file'])]; it=d['issue_timestamp'] or d['issue_date']
    if not it: continue
    v=r['timestamp'] or r['value']
    p=r['parent']; e=r['element']
    kind=None
    if e=='OccurrenceDate':
        if past.match(p): kind='PAST'
        elif fut.match(p): kind='FUT'
    elif e in ('ActualDeliveryDate','ActualDespatchDate','ActualPickupDate','ManufactureDate','ReceivedDate','PaidDate','WeighingDate','LatestMeterReadingDate','ValidationDate','AwardDate','ResolutionDate','RegisteredDate','TransactionDate','PurchaseDate','ResponseDate','OnsetDate','JoinedShipDate','VisitDate','ApplicationDate','LastDrinkingWaterAnalysisDate','CallDate') or (e=='IssueDate' and p.endswith('Reference')):
        kind='PAST'
    elif e.startswith('Estimated') or p.startswith('Estimated'):
        kind='FUT'
    if kind=='PAST' and (v>it if len(v)>10 and len(it)>10 else v[:10]>it[:10]):
        print('PAST>ISSUE',r['flow'],r['file'],it,v,r['xpath'])
    if kind=='FUT' and (v<it if len(v)>10 and len(it)>10 else v[:10]<it[:10]):
        print('FUT<ISSUE',r['flow'],r['file'],it,v,r['xpath'])
