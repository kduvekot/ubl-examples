#!/usr/bin/env python3
"""Which kinds of organisation does the UBL example world need?

Every party element in every UBL document type (each ASBIE whose content is
cac:Party or a wrapper such as CustomerParty or SupplierParty) is assigned
an organisation type, based on the UBL definition of the element in its
context. The report then shows:

  * the full cover: all organisation types that the 101 document types need;
  * per document type, how many different organisations it needs at least,
    when no organisation appears twice in one document;
  * which types could be merged, because no document needs both.

Some roles do not need an organisation of their own: they only point to a
party that is already present (the sender or receiver of a document, a
signatory, the issuer of a referenced document, a party to notify). They
are marked "relational".

Usage
  python3 tools/party_cover.py --model UBL-Entities-2.5.gc > analysis/party-cover.md
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import coverage  # noqa: E402  (model loading)

# ---------------------------------------------------------------------------
# Organisation types. "26+C" names the matching party of the agreed set
# (analysis/session-decisions.md on branch sample-research, section 5.3), or "-" if none.
TYPES = {
    "BUYER":      ("Buyer (customer organisation)", "1, 26"),
    "SELLER":     ("Seller (supplier organisation)", "5, 6"),
    "MANUFACTURER": ("Manufacturer", "5"),
    "AUTHORITY":  ("Contracting authority", "2"),
    "OPERATOR":   ("Economic operator (tenderer)", "5"),
    "OPERATOR2":  ("Second economic operator (consortium partner, subcontractor)", "-"),
    "REVIEW":     ("Review body (procurement appeals and mediation)", "-"),
    "PUBLIC":     ("Public information service (publication office, business registry)", "21"),
    "GOVERNMENT": ("Other government authority (flag state, certifying ministry)", "-"),
    "FORWARDER":  ("Freight forwarder / logistics operator", "10"),
    "CARRIER":    ("Carrier (transport service provider)", "11-15"),
    "CARRIER2":   ("Second carrier (substitute carrier)", "11-15"),
    "WAREHOUSE":  ("Warehouse / goods processing", "8, 9"),
    "PORT":       ("Port, terminal or weighing operator", "16-18"),
    "CUSTOMS":    ("Customs authority", "19"),
    "CUSTOMS2":   ("Second customs authority (other country)", "19"),
    "CUSTOMSAGENT": ("Customs agent / declarant", "3"),
    "CERTIFIER":  ("Certifying body (chamber of commerce, guaranteeing association)", "20"),
    "CERTIFIER2": ("Second certifying body (other country)", "20"),
    "INSURER":    ("Insurer", "-"),
    "INSBROKER":  ("Insurance broker", "-"),
    "BANK":       ("Bank / financial institution (also factor, guarantor)", "22-25"),
    "TAXREP":     ("Tax representative", "-"),
    "UTILITY":    ("Utility supplier", "5"),
    "WASTE":      ("Waste processor (recovery or disposal facility)", "7"),
    "GOVERNOR":   ("Governance body of a digital agreement", "-"),
    "IDAGENCY":   ("Identifier issuing agency (item or property identifiers)", "-"),
    "REL":        ("relational: a party already present", ""),
}

# Merges that make sense in the real world: (type, merged into, why).
# The script checks that no document needs both types.
MERGES = [
    ("MANUFACTURER", "SELLER", "The seller makes what it sells."),
    ("UTILITY", "SELLER", "A utility is a seller of energy, water or telecom services."),
    ("WAREHOUSE", "FORWARDER", "A logistics operator also runs warehouses."),
    ("CUSTOMSAGENT", "FORWARDER", "Forwarders commonly act as customs agent."),
    ("INSBROKER", "FORWARDER", "Forwarders commonly arrange cargo insurance."),
    ("TAXREP", "FORWARDER", "Forwarders and customs agents commonly act as fiscal representative."),
    ("PORT", "CARRIER", "A carrier can operate its own terminal."),
    ("INSURER", "BANK", "One financial group can provide both finance and insurance."),
    ("IDAGENCY", "CERTIFIER", "A chamber of commerce or trade association can issue identifiers."),
    ("GOVERNOR", "PUBLIC", "A public service can govern a digital agreement framework."),
    ("REVIEW", "PUBLIC", "A public body can handle procurement appeals."),
    ("GOVERNMENT", "CUSTOMS", "One government administration for customs and certification."),
    ("OPERATOR", "SELLER", "In procurement, the tenderer is the seller."),
    ("WASTE", "SELLER", "A waste processor sells its processing service."),
]

# Role name -> type, used unless a context or document rule below applies.
ROLE = {
    # commercial parties
    "AccountingCustomerParty": "BUYER", "BuyerCustomerParty": "BUYER", "CustomerParty": "BUYER",
    "DeliveryCustomerParty": "BUYER", "ContractorCustomerParty": "BUYER", "OriginatorCustomerParty": "BUYER",
    "OriginatorParty": "BUYER", "RetailerCustomerParty": "BUYER", "BillToParty": "BUYER",
    "ConsigneeParty": "BUYER", "ImporterParty": "BUYER", "DeliveryParty": "BUYER", "FinalDeliveryParty": "BUYER",
    "PayerParty": "BUYER", "TransportUserParty": "BUYER", "SubscriberParty": "BUYER",
    "UtilityCustomerParty": "BUYER", "ApproverParty": "BUYER", "BusinessParty": "SELLER",
    "AccountingSupplierParty": "SELLER", "SellerSupplierParty": "SELLER", "DespatchSupplierParty": "SELLER",
    "ProviderParty": "SELLER", "ConsignorParty": "SELLER", "ExporterParty": "SELLER", "DespatchParty": "SELLER",
    "OriginalDespatchParty": "SELLER", "InformationContentProviderParty": "SELLER", "WarrantyParty": "SELLER",
    "ShipperParty": "SELLER", "TransitExporterParty": "SELLER", "HolderParty": "SELLER",
    "ApplicantParty": "SELLER", "PreparationParty": "SELLER", "RepresentativeParty": "SELLER",
    "InventoryReportingParty": "SELLER", "PolicyHolderParty": "SELLER", "InsuranceParty": "SELLER",
    "PerformingParty": "SELLER", "PayeeParty": "BANK", "ManufacturerParty": "MANUFACTURER",
    "BillOfLadingHolderParty": "BANK", "MortgageHolderParty": "BANK", "FinancingParty": "BANK",
    "GuarantorParty": "BANK", "TaxRepresentativeParty": "TAXREP", "UtilitySupplierParty": "UTILITY",
    # public procurement
    "ContractingParty": "AUTHORITY", "TenderRecipientParty": "AUTHORITY", "TenderEvaluationParty": "AUTHORITY",
    "QualificationRequestRecipientParty": "AUTHORITY", "DocumentProviderParty": "AUTHORITY",
    "AdditionalInformationParty": "AUTHORITY", "ContractResponsibleParty": "AUTHORITY",
    "AppealInformationParty": "AUTHORITY",
    "EconomicOperatorParty": "OPERATOR", "TendererParty": "OPERATOR", "WinningParty": "OPERATOR",
    "PreSelectedParty": "OPERATOR", "MainQualifyingParty": "OPERATOR", "InterestedParty": "OPERATOR",
    "AdditionalQualifyingParty": "OPERATOR2", "SubcontractorParty": "OPERATOR2",
    "AppealReceiverParty": "REVIEW", "MediationParty": "REVIEW",
    "EvidenceIssuingParty": "PUBLIC",
    # logistics
    "FreightForwarderParty": "FORWARDER", "LogisticsOperatorParty": "FORWARDER",
    "SendingLogisticsOperatorParty": "FORWARDER", "TransportAdvisorParty": "FORWARDER",
    "HazardousItemNotificationParty": "FORWARDER",
    "CarrierParty": "CARRIER", "PerformingCarrierParty": "CARRIER", "TransportServiceProviderParty": "CARRIER",
    "ResponsibleTransportServiceProviderParty": "CARRIER", "PickupParty": "CARRIER",
    "OperatingParty": "CARRIER", "OwnerParty": "CARRIER", "SupplierParty": "CARRIER",
    "SourceIssuerParty": "CARRIER", "ReporterParty": "CARRIER", "FuelProviderParty": "CARRIER",
    "SubstituteCarrierParty": "CARRIER2",
    "WarehouseParty": "WAREHOUSE", "ProcessingParty": "WAREHOUSE",
    "TerminalOperatorParty": "PORT", "WeighingParty": "PORT", "AuthorityParty": "PORT",
    "LoadingProofParty": "CUSTOMS", "CustomsParty": "CUSTOMS", "ExportingCustomsParty": "CUSTOMS",
    "ImportingCustomsParty": "CUSTOMS2", "CustomsAgentParty": "CUSTOMSAGENT",
    "ISSCIssuerParty": "GOVERNMENT", "LegalAuthorityParty": "GOVERNMENT",
    "InsurerParty": "INSURER", "BrokerParty": "INSBROKER",
    # certificates
    "EndorserParty": "CERTIFIER", "ExportingGuarantorParty": "CERTIFIER", "ImportingGuarantorParty": "CERTIFIER2",
    # waste
    "WasteProducerParty": "MANUFACTURER", "NotifierParty": "SELLER",
    "RecoveryFacilityParty": "WASTE", "DisposalFacilityParty": "WASTE",
    # agreements
    "GovernorParty": "GOVERNOR", "ParticipantParty": "REL",
    # relational: point to a party that is already present
    "SenderParty": "REL", "ReceiverParty": "REL", "SignatoryParty": "REL", "RecipientParty": "REL",
    "NotifyParty": "REL", "ContactParty": "REL", "BeneficiaryParty": "REL", "CollectedForParty": "REL",
    "RequestorParty": "REL", "ResponderParty": "REL", "ResponsibleParty": "REL", "Party": "REL",
}

# (parent aggregate, role) -> type, where the context changes the meaning
CONTEXT = {
    ("DocumentReference", "IssuerParty"): "REL",      # issuer of a document referred to
    ("DocumentResponse", "IssuerParty"): "REL",
    ("CustomsDeclaration", "IssuerParty"): "REL",     # the declarant, a party already present
    ("Certificate", "IssuerParty"): "CERTIFIER",
    ("Attestation", "IssuerParty"): "CERTIFIER",
    ("CertificateOfOriginApplication", "IssuerParty"): "CERTIFIER",
    ("ImmobilizedSecurity", "IssuerParty"): "BANK",
    ("ItemIdentification", "IssuerParty"): "IDAGENCY",
    ("PropertyIdentification", "IssuerParty"): "IDAGENCY",
    ("TransportEquipment", "ProviderParty"): "CARRIER",
    ("Despatch", "ResponsibleParty"): "CARRIER",       # picks up the goods
    ("TransportSegment", "TransportServiceProviderParty"): "CARRIER",
}

# (document type, role) -> type, for document-level roles whose meaning
# depends on the document
DOCUMENT = {
    ("PriorInformationNotice", "ReceiverParty"): "PUBLIC",   # notices go to the publication office
    ("ContractNotice", "ReceiverParty"): "PUBLIC",
    ("ContractAwardNotice", "ReceiverParty"): "PUBLIC",
    ("BusinessInformation", "SenderParty"): "PUBLIC",        # sent by the business registry
    ("GoodsItemPassport", "IssuerParty"): "CERTIFIER",       # the issuing chamber
    ("GoodsCertificate", "IssuerParty"): "CERTIFIER",
    ("CertificateOfOrigin", "IssuerParty"): "CERTIFIER",
    ("GuaranteeCertificate", "InterestedParty"): "OPERATOR",
}


def classify(doc, parent, role):
    if parent == "<doc>" and (doc, role) in DOCUMENT:
        return DOCUMENT[(doc, role)]
    if (parent, role) in CONTEXT:
        return CONTEXT[(parent, role)]
    return ROLE[role]


def party_roles(abies, docs, partylike, doc, max_depth=99):
    """(parent, role, depth, path) for every party role reachable in a document."""
    out, seen, todo = {}, {doc}, collections.deque([(doc, 0, doc)])
    while todo:
        a, depth, path = todo.popleft()
        for p in abies[a]["props"]:
            t = p.get("target")
            if not t:
                continue
            parent = "<doc>" if a == doc else a
            if t in partylike:
                out.setdefault((parent, p["ComponentName"]), (depth + 1, f"{path}/{p['ComponentName']}"))
                continue
            if t not in seen and depth + 1 < max_depth:
                seen.add(t)
                todo.append((t, depth + 1, f"{path}/{p['ComponentName']}"))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    args = ap.parse_args()
    abies, docs = coverage.load_model(args.model)
    partylike = {"Party"} | {a for a, x in abies.items() if a not in docs and a.endswith("Party")
                             and any(p.get("target") == "Party" for p in x["props"])}

    unmapped = set()
    per_doc = {}      # doc -> {"top": types at document level, "near": types up to depth 2, "all": all}
    users = collections.defaultdict(set)   # type -> documents (document level)
    roles_of = collections.defaultdict(set)
    for d in docs:
        res, minimum = {}, {}
        for label, depth in (("top", 1), ("near", 2), ("all", 99)):
            types = set()
            found = party_roles(abies, docs, partylike, d, depth)
            # a sender and a receiver are always two different parties
            minimum[label] = 2 if {("<doc>", "SenderParty"), ("<doc>", "ReceiverParty")} <= set(found) else 1
            for (parent, role), (dep, path) in found.items():
                if role not in ROLE and (parent, role) not in CONTEXT and (d, role) not in DOCUMENT:
                    unmapped.add((parent, role))
                    continue
                t = classify(d, parent, role)
                roles_of[t].add(f"{role}" + ("" if parent == "<doc>" else f" ({parent})"))
                if t != "REL":
                    types.add(t)
                    if label == "top":
                        users[t].add(d)
            res[label] = types
        res["min"] = minimum
        per_doc[d] = res
    if unmapped:
        sys.exit(f"unmapped roles: {sorted(unmapped)}")

    used = {t for t in TYPES if t != "REL" and any(t in r["all"] for r in per_doc.values())}
    w = print
    w("# Party cover: the organisations the UBL example world needs\n")
    w("Every party element in every UBL 2.5 document type is assigned an organisation")
    w("type, based on its UBL definition in its context. Generated by")
    w("`tools/party_cover.py` from `UBL-Entities-2.5.gc`; the mapping table is in the script.\n")
    w("## Summary\n")
    count = lambda r, k: max(len(r[k]), r["min"][k])
    tops = {d: count(r, "top") for d, r in per_doc.items()}
    nears = {d: count(r, "near") for d, r in per_doc.items()}
    alls = {d: count(r, "all") for d, r in per_doc.items()}
    mx = lambda m: (max(m.values()), sorted(d for d in m if m[d] == max(m.values())))
    w(f"- **Organisation types needed (full cover):** {len(used)}, listed below.")
    w(f"- **Most organisations one document needs, document level:** {mx(tops)[0]} ({', '.join(mx(tops)[1])}).")
    w(f"- **… including one structure level deeper** (delivery, shipment, tendering terms): "
      f"{mx(nears)[0]} ({', '.join(mx(nears)[1])}).")
    w(f"- **… including every party element a document can contain:** {mx(alls)[0]} "
      f"({', '.join(mx(alls)[1])}).\n")

    w("## Organisation types\n")
    w("| Type | 26+C | Document types (document level) | Roles |\n|---|---|---:|---|")
    for t, (name, ref) in TYPES.items():
        if t == "REL" or t not in used:
            continue
        roles = sorted(roles_of[t])
        shown = ", ".join(f"`{r}`" for r in roles[:8]) + (f" and {len(roles) - 8} more" if len(roles) > 8 else "")
        w(f"| {name} | {ref} | {len(users[t])} | {shown} |")
    rel = sorted(roles_of["REL"])
    w(f"\n**Relational roles** (filled by a party already present, no organisation of their own): "
      + ", ".join(f"`{r}`" for r in rel) + ".\n")

    w("## Merging types: the smallest world\n")
    w("Some types can be one organisation in practice. A merge is only possible if")
    w("no document needs both types (checked at document level and one structure")
    w("level deeper); otherwise one organisation would appear twice in that document.\n")
    cooc = collections.defaultdict(set)
    for d, r in per_doc.items():
        for a in r["near"]:
            for b in r["near"]:
                cooc[(a, b)].add(d)
    w("| Merge | Why it can be one organisation | Conflict |\n|---|---|---|")
    merged = {}
    for a, b, why in MERGES:
        if a not in used or b not in used:
            continue
        clash = sorted(cooc[(a, b)])
        ok = not clash
        if ok:
            merged[a] = b
        w(f"| {TYPES[a][0].split(' (')[0]} → {TYPES[b][0].split(' (')[0]} | {why} | "
          + ("none: merge possible" if ok else "not possible, both needed in " + ", ".join(clash)) + " |")
    def root(t):
        while t in merged:
            t = merged[t]
        return t
    smallest = {root(t) for t in used}
    w(f"\n**Smallest world:** {len(smallest)} organisations, after the possible merges above:")
    w(", ".join(TYPES[t][0].split(" (")[0] for t in sorted(smallest, key=lambda t: list(TYPES).index(t))) + ".\n")

    w("## Compared with the 26+C party set\n")
    missing = [t for t in sorted(used, key=lambda t: list(TYPES).index(t)) if TYPES[t][1] == "-"]
    w("Types that the documents need but that have no counterpart in the 26+C set")
    w("(`analysis/session-decisions.md` on branch `sample-research`, section 5.3):\n")
    for t in missing:
        into = f" (can merge into {TYPES[root(t)][0].split(' (')[0]})" if root(t) != t else ""
        w(f"- {TYPES[t][0]}{into}")
    w("")

    w("## Organisations per document type\n")
    w("Different organisations a document needs when none appears twice:")
    w("document level / including one level deeper / including every party element.")
    w("A document with a sender and a receiver always needs at least two.\n")
    w("| Document type | Document level | One level deeper | Everything |\n|---|---:|---:|---:|")
    for d in sorted(docs, key=lambda d: (-tops[d], -nears[d], d)):
        w(f"| {d} | {tops[d]} | {nears[d]} | {alls[d]} |")


if __name__ == "__main__":
    main()
