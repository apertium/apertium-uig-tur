from dixflow import *

bidpath = "../apertium-uig-tur.uig-tur.dix"
turpath = "../../apertium-tur/apertium-tur.tur.lexc"

bid_mon = {
'adj':["A1","A2","A3","A4"],
'adv':["ADV1","ADV2","ADV3","ADV4"],
('adv', 'itg'):"ADV-ITG",
('adv', 'qnt'):"ADV-QNT",
'cnjadv':"CA",
'cnjcoo':"CC",
'cnjsub':"CS",
('det', 'dem'):"DET-DEM",
('det', 'itg'):"DET-ITG",
('det', 'neg'):"DET-NEG",
('det', 'qnt'):"DET-QNT",
('det', 'ref'):"DET-REF",
'n':["N1","N2","N3","N4","N5"],
('np', 'al'):"NP-AL",
('np', 'al','pl'):"NP-AL-PL",
('np', 'ant', 'f'):"NP-ANT-F",
('np', 'ant', 'm'):"NP-ANT-M",
('np', 'cog', 'mf'):"NP-COG-MF",
('np', 'org'):"NP-ORG",
('np', 'top'):"NP-TOP",
'post':"POST",
'postadv':"POSTADV",
('prn', 'adv'):"PRON-ADV",
('prn', 'dem'):"PRON-DEM",
('prn', 'ind'):"PRON-IND",
('prn', 'itg'):"PRON-ITG",
('prn', 'pers'):"PRON-PERS",
('prn', 'qnt'):"PRON-QNT",
('v', 'iv'):["V-AR-IV","V-IR-IV"],
('v', 'tv'):["V-AR-TV","V-IR-TV"]}

bd, mn = {},{}
for line in open(bidpath):
    b = bidix_entry_read(line)
    if b:
        try:
            if b[3] not in bd[b[1]]:
                bd[b[1]].append(b[3])
        except KeyError:
            bd[b[1]] = [b[3]]

for line in open(turpath):
    m = mono_lexc_entry_read(line)
    if m:
        g = m.groups()
        try:
            if g[2] not in mn[g[0]]:
                mn[g[0]].append(g[2])
        except KeyError:
            mn[g[0]] = [g[2]]

missing = []
verbose = False
for bi_lemma in bd:
    if verbose: print("")
    if verbose: print("Analyzing",bi_lemma)
    mono_lemma = bi_lemma.replace("<b/>","% ")
    try:
       mono_analyses = mn[mono_lemma]
    except KeyError:
        unk_analyses = bd[bi_lemma]
        for item in unk_analyses: 
            try:
                if len(item ) == 1: a = bid_mon[item[0]]
                else: a = bid_mon[tuple(item)]
                missing.append((mono_lemma,a))
            except KeyError: continue
        continue
    bi_analyses = bd[bi_lemma]
    check = []
    for analysis in bi_analyses:
        try:
            if len(analysis) == 1: bm = bid_mon[analysis[0]]
            else:
                bm = bid_mon[tuple(analysis)]
            if bm not in check:
                check.append(bm)
        except KeyError: continue
    try:
        if type(check[0]) == str: check = [check]
    except IndexError: continue
    for item in check:
        if verbose: print("Checking:",item)
        present = False
        for cand in item:
            if verbose: print(cand, mono_analyses)
            if cand in mono_analyses:
                present=True
                if verbose: print("FOUND")
                break
        if verbose: print("Mono analyses:", mono_analyses)
        if verbose: print("Bidix analyses:", check)
        if not present:
            if verbose: print("ADDED",mono_lemma)
            missing.append((mono_lemma,item))

      
entries = []
for x in missing:
    if type(x[1]) == str: tag = x[1]
    else: tag = x[1][0]
    entries.append(x[0] + ":" + x[0] + " " + tag + " ;")

entries = sorted([x[::-1] for x in entries])
entries = [x[::-1] for x in entries]
for item in entries: print(item)

