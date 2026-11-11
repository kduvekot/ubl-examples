# Sources of the world's code lists

Machine-readable copies of the authoritative lists the world's code lists are built from. Each was fetched on 2026-11-11. The citations of other sources (standards texts, PDFs and web pages that are not copied here) are in `analysis/source-verification.md`. unece.org blocks automated access (also from GitHub runners), so the UN/EDIFACT lists come from UN/CEFACT's own GitHub repository and from OpenPeppol's code list files.

| Directory | Source | Version |
|---|---|---|
| uncefact/ | https://github.com/uncefact/vocabulary-outputs (`_data/*codelist.json`) | commit 51768f9c41be13673bc6d555c8c21c79d9e481a0 (2024-07-29), data set D22A. UN/CEFACT names lists by concept: `documentcodelist` = UNCL 1001, `allowancechargeidcodelist` = UNCL 5189, `allowancechargereasoncodelist` = UNCL 4465, `paymentmeanscodelist` = UNCL 4461, `measuredattributecodelist` = UNCL 6313 … |
| peppol/ | https://github.com/OpenPEPPOL/poacc-upgrade-3 (`structure/codelist/`): UNCL 7161, 1001, 5387, UN/ECE Rec 21; https://github.com/OpenPEPPOL/peppol-bis-invoice-3: ISO 6523 ICD list | poacc-upgrade-3 commit c3bd29f5afe321c1769d67c89756296e35ef327e; peppol-bis-invoice-3 commit 38d693d71d28d813781323a6ca97324edcc4d239 |
| iso10383/ | https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv | as published 2026-11-11 |
| iso4217/ | https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml | as published 2026-11-11 |
| iso639-2/ | https://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt (ISO 639-2 Registration Authority) | as published 2026-11-11 |
| cpc/ | https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/CPC_Ver_2_1_english_structure.txt | CPC Ver.2.1 (Ver.3.0 was published in June 2025) |
| iana/ | https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry (BCP 47) | as published 2026-11-11 |
| epsg/ | https://apps.epsg.org/api/v1/CoordRefSystem/4326/ | as published 2026-11-11 |
| bic/ | https://www.bic-code.org/bic-codes/&lt;code&gt;/ (the BIC register of ISO 6346 owner codes): the result of looking up the world's container owner codes, not a copy of the register | 2026-11-11 |
| pronom/ | https://www.nationalarchives.gov.uk/PRONOM/fmt/479.xml, fmt/480.xml, fmt/481.xml (PDF/A-3a, -3b, -3u) | as published 2026-11-11 |
| rec28/ | https://unece.org/trade/uncefact/cl-recommendations (Rec 28): `Rec28_Rev4.2e_2018.xls`, the code list "Revision 4.2" (2018, the current code list; sheet header "CODES FOR TYPES OF MEANS OF TRANSPORT Revision 4.2"), and `Rec28_Rev3e_2010.pdf`, the Recommendation text, Revision 3 (CEFACT/ICG/2010/IC011, approved 12 July 2010). Downloaded by the project owner from a normal browser on 2026-11-11, because unece.org blocks automated access. | Revision 4.2 (code list), Revision 3 (text) |
| optd/ | https://raw.githubusercontent.com/opentraveldata/opentraveldata/master/opentraveldata/optd_aircraft.csv (OpenTravelData, CC BY 4.0): IATA aircraft type codes with ICAO codes. A secondary source: the official list, IATA SSIM Appendix A, is not public. ATF = ATR 72 Freighter (ICAO AT72) is confirmed by Airport Coordination Netherlands, "Noise values for slot allocation" S25 (note 22.913.02, 30 August 2024), and by avcodes.co.uk and SeatLink, all read 2026-11-11. | commit cfc7b82f6c96cdf7cd12c7be000bc2e0f82dbdaf |
| cpc/CPC21-HS2017.csv | https://unstats.un.org/unsd/classifications/Econ/tables/CPC/CPCv21_HS2017/CPC21-HS2017.csv (UN Statistics Division, official correspondence HS 2017 ↔ CPC Ver.2.1; columns HS 2017, HS partial, CPC Ver. 2.1, CPC partial) | as published 2026-11-11 |

## SHA-256

```
a8a4e088e637fd253f6c329f98c7a2f288a23ac2fee79d6529f238c0569f3c5c  ./cpc/CPC21-HS2017.csv
06c22576347c5b44cb83e1113a0bd2702418cd2fa61838dc1ace37b57a7b2693  ./optd/optd_aircraft.csv
cb572a961ad83e131e0fb71b38c591d591c9187e32e2733d48e50ca43596d2a7  ./rec28/Rec28_Rev3e_2010.pdf
69d9c888a31609943c568b48a8f4bb202f54f6cd1e402ee9616062cccab7c96b  ./rec28/Rec28_Rev4.2e_2018.xls
1c3e88e5fa67b9ba0d27594cb3363f717321f58fe0308be60b326ebf927c1b92  ./cpc/CPC_Ver_2_1_english_structure.txt
eab591fb6bae660e1e45c63a9fd84ad3d2b865728c1c37869bc7cc9527487bd7  ./epsg/crs-4326.json
755fad43283be7b41ebe3c89ad054b6eaf928f404f9c0edb74799e0eab74beb1  ./iana/language-subtag-registry.txt
1d7f8aadd0ff8ca6ee94cbe67f1165845c67124731edddcc26b129f1da45eb0a  ./iso10383/ISO10383_MIC.csv
33139b438657d1cee116ba737807ea71d19d6de4b90f799a09c56f0cc6a1b0ff  ./iso4217/list-one.xml
42b71885e4dc885559fda5ad059fd81838cf4782cedb5fd08cc3431f7d067371  ./iso639-2/ISO-639-2_utf-8.txt
5c4346f81e24f44f2444baa823f865e921c6b28d6dd6c06ab285b3cd5ab04717  ./peppol/ICD.xml
8ae48183e46c5c9f92613e6e92269de1efcd13422cdc6278c493a3ec61e9f182  ./peppol/UNCL1001.xml
2852002a7503586c6f7e11814fc916c170947041bb9e1709d6e822597a022eab  ./peppol/UNCL5387.xml
e325d85ba63a7c5405fe27037bc7551568bbd7508147d2a3952a6cded3ae1921  ./peppol/UNCL7161.xml
ddf79c5eb3e76054f8db3b13edb51a5ff4b01d03005fa27df23f212907855d0e  ./peppol/UNECERec21-9e.xml
eb56a731294d8b6f816e829d28391f191c00ebbbc3a562a1e8208777e592b495  ./pronom/fmt-479.xml
9c99c340d597793064c54b8944ad7626d3e34b50e71e82d37279e8f7d43654bb  ./pronom/fmt-480.xml
46a53c29812a821a1f5ffd89632db0821163e0cbe71081d80e29fdbadf98a2f9  ./pronom/fmt-481.xml
63b3fc56d73c8c4a7d8c6488aba0d76bf21218da8eef7fd2702af6c7acaf6b95  ./uncefact/PROVENANCE.txt
928503255be4e2c53abc18d2e7b6e750e701b2f881a42b6c54a399d36d0860b6  ./bic/owner-codes.txt
e84677fbd02f65cc8c123412d15e5ce566d89a873f4e8cd845eb454b713aa518  ./uncefact/allowancechargeidcodelist.json
2fb6e178cffea3181849e6c220e33619f0ca3a27aedab2501f661f8d60b4339c  ./uncefact/allowancechargereasoncodelist.json
d33c42ffa70af3c095630f9484ff9bbafc655d08303fb4216fc78aa863edf62d  ./uncefact/cargocategorycodelist.json
1789f618329b5903ff836cc4236debb7e0ebcb6c21bf5415c04c82d9e4d3595e  ./uncefact/cargotypeclassificationcodelist.json
eb6d9d00cc6d13d74fb4fac8c05f54e8affb1e85f3623a4be800f6fcaab5b5be  ./uncefact/dangerousgoodspackaginglevelcodelist.json
94d47ba3d927c45acb6d83a62d3bd8dca28e7915519b91716aa1b3cdf9220ac7  ./uncefact/dangerousgoodsregulationcodelist.json
43aeda189577f6d03d4c3c44c64959c8ef568a607ec5f456c5903d5c255794bf  ./uncefact/dimensiontypecodelist.json
2b7ff59177100601aeb5e3a5265e1c97582fe181376c63b6db787a14b75444bc  ./uncefact/documentcodelist.json
35578a94111490309837f41909abd248238e5111d0532b61f3836360931e3e4e  ./uncefact/measuredattributecodelist.json
a3c3a0a5dfa683c5567808fc09f99b0dcea87d367cf6296d900c0a30fd08cdc4  ./uncefact/paymentmeanschannelcodelist.json
89f8d6324b77fd2174c51fa75eb55b528d9c2566e74f1a1566ed8499d124334c  ./uncefact/paymentmeanscodelist.json
e4d13c4d011652e596c1caac8e5d1983dea0fd96ab88988f8710d8a27433b04f  ./uncefact/responsetypecodelist.json
f5d9559efbb060765cfa46d701a8a907fac9fb51aa4592d0e2d512f3aa10fa0b  ./uncefact/sealconditioncodelist.json
0858697a205504a439271c894ce02813107ea31b9b8ea09310a748cfb14d1448  ./uncefact/sealingpartyrolecodelist.json
a29d6129ecc33a1760f86e549b6ef4b58d006eb6fce9e930dc0ccc9a836786c0  ./uncefact/taxcategorycodelist.json
7d4e5ad249dbeb76be2ba67a202ed24c6ef6828b7e4305ba1d31393ef2b90b38  ./uncefact/taxtypecodelist.json
a0cde3b5c97493cad4e2fb16091b144fb96144ffcb3c5eb15acc8322256149fb  ./uncefact/timereferencecodelist.json
504a7c59bc53197a85c79acb041fdf2688f582783f3997c5669a917eab06e970  ./uncefact/transportmeanstypecodelist.json
65f51d385f9ea71c5e1c7324b764a8268dc1c33d3893f476c747ff3ffddafb96  ./uncefact/undgidentificationcode.json
```
