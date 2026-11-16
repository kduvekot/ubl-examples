import csv,collections,re,datetime
T='/home/user/ubl-examples/.review/tables/'
docs=list(csv.DictReader(open(T+'documents.csv')))
dates=collections.defaultdict(list)
for r in csv.DictReader(open(T+'dates.csv')): dates[(r['flow'],r['file'])].append(r)
per=collections.defaultdict(list)
for r in csv.DictReader(open(T+'periods.csv')): per[(r['flow'],r['file'])].append(r)
refs=collections.defaultdict(set)
for r in csv.DictReader(open(T+'references.csv')):
    for m in filter(None,[x.strip() for x in r['example_matches'].split('|')]):
        refs[(r['flow'],r['file'])].add(m.split('/')[-1][:2] if m.startswith(r['flow']+'/') else m.split('-')[0])
keep=re.compile(r'(TransportEvent|RequestedArrivalEvent)$|^(Despatch|Delivery|Pickup|ReceiptLine|ItemInstance|Payment|PrepaidPayment|CollectedPayment|TenderResult|TenderReceipt|QualificationResolution|VerifiedGrossMass|MeterReading|PurchaseReceipt|MainCarriageShipmentStage)$')
pk=re.compile(r'^(InvoicePeriod|DeliveryPeriod|RequestedDeliveryPeriod|PromisedDeliveryPeriod|TenderSubmissionDeadlinePeriod|ParticipationRequestReceptionPeriod|InvitationSubmissionPeriod|DocumentAvailabilityPeriod|PresentationPeriod|ContractFormalizationPeriod|ServiceStartTimePeriod|ServiceEndTimePeriod|ReportedPeriod|StatementPeriod|ForecastPeriod|EstimatedDespatchPeriod|EstimatedDeliveryPeriod|TransitPeriod|ApplicablePeriod|NotificationPeriod|RequestedStatusPeriod|ReminderPeriod|ExceptionObservationPeriod|InventoryPeriod|AdoptionPeriod|NominationPeriod|ActivityPeriod)$')
def short(p):
    q=p.replace('TransportEvent','').replace('Transport','')
    return q or 'Event'
for fl in sorted(set(d['flow'] for d in docs)):
    print(f'\n#### {fl}\n\n| Issued | Document | Dated events and periods it carries | Refers to |\n|---|---|---|---|')
    ds=sorted([d for d in docs if d['flow']==fl],key=lambda d:d['issue_timestamp'] or d['issue_date'] or 'Z')
    for d in ds:
        k=(fl,d['file']); ev=[]; seen=set()
        for r in dates[k]:
            if r['element'].endswith('Time') and r['timestamp']: continue
            if keep.search(r['parent']) and r['element'] not in ('RegistrationDate',):
                v=(r['timestamp'] or r['value']).replace('T',' ')[:16]
                lab=f"{short(r['parent'])}.{r['element'].replace('Date','').replace('Occurrence','')}".rstrip('.')
                lab=lab.replace('.','',1) if lab.endswith('.') else lab
                key=(lab,v)
                if key in seen: continue
                seen.add(key); ev.append(f'{lab} {v}')
        for r in per[k]:
            if pk.match(r['element']) and (r['start'] or r['end']):
                key=(r['element'],r['start'],r['end'])
                if key in seen: continue
                seen.add(key); ev.append(f"{r['element']} {r['start'].replace('T',' ')[:16]}–{r['end'].replace('T',' ')[:16]}")
        t=(d['issue_timestamp'] or d['issue_date'] or '(none)').replace('T',' ')[:16]
        wd=datetime.date.fromisoformat(t[:10]).strftime('%a') if t[0]=='2' else ''
        print(f"| {t} {wd} | {d['file'].replace('.xml','')} `{d['id']}` | {'; '.join(ev)[:700]} | {', '.join(sorted(refs[k]))} |")
