import sys, os, re

def monofy(line,left=True):
    dic = { '<s n="adj"/>':'A1',
            '<s n="adv"/>':"ADV1",
            '<s n="n"/>':"N1",
            '<s n="np"/><s n="top"/>':"NP-TOP",
	    '<s n="post"/>':"POST",
            '<s n="np"/><s n="cog"/><s n="mf"/>':"NP-COG-MF",
            '<s n="np"/><s n="org"/>':"NP-ORG",
            '<s n="np"/><s n="al"/>':"NP-AL",
            '<s n="prn"/><s n="itg"/>':"PRON-ITG",
            '<s n="prn"/><s n="pers"/>':"PRON-PERS",
            '<s n="det"/><s n="itg"/>':"DET-ITG",
            '<s n="adv"/><s n="itg"/>':"ADV-ITG",
            '<s n="v"/><s n="iv"/>':"V-IR-IV",
            '<s n="cnjcoo"/>':"CC",
            '<s n="ij"/>':"INTERJ",
            '<s n="cnjsub"/>':"CS",
            '<s n="np"/><s n="ant"/><s n="m"/>':'NP-ANT-M',
            '<s n="np"/><s n="ant"/><s n="f"/>':'NP-ANT-F',
            '<s n="cnjadv"/>':"CA",
            '<s n="abbr"/>':"ABBR",
            '<s n="v"/><s n="tv"/>':"V-IR-TV",
	    '<s n="det"/><s n="qnt"/>':"DET-QNT",
	    '<s n="det"/><s n="dem"/>':"DET-DEM",
	    '<s n="cog"/><s n="mf"/>':"NP-COG-MF",
            '<s n="prn"/><s n="qnt"/>':"PRON-QNT",
            '<s n="prn"/><s n="dem"/>':"PRON-DEM",
            '<s n="num"/><s n="num"/>':"NUM"
}

    if left:
        word = line.partition("<s")[0]
        #word = line.partition("<l>")[2].partition("<s")[0]
        tags= "".join(line.partition("<s")[1:]).partition("</r>")[0]
    else:
        word = line.partition("<s")[0]
        tags= "".join(line.partition("<s")[1:]).partition("</r>")[0]
    word = re.sub("<b */>", "% ", word)
    entry = word + ":" + word + " " + dic[tags] + " ; !"
    return entry


if __name__=="__main__":
    left = True
    if "-tur" in sys.argv: left=False
    d = os.path.dirname(__file__)
    if left:
        filename = os.path.join(d, '../../apertium-uig/apertium-uig.uig.lexc')
    else:
        filename = os.path.join(d, '../../apertium-tur/apertium-tur.tur.lexc')
    #text = "".join([x for x in open(filename).readlines() if "V-TD" not in x])
    present_entries = set()
    entry_re = re.compile("([-\w]*):([-\w]*) *([\w-]*) ;")
    with open(filename) as infile:
        for line in infile.readlines():
            present_entry = re.match(entry_re, line)
            if present_entry is not None:
                present_entries.add(present_entry.groups())
    for line in sys.stdin.readlines():
        if "<" in line:
            try:
                m = monofy(line,left)
                new_entry = re.match(entry_re, m)
                if not new_entry:
                    continue
                if new_entry.groups() not in present_entries:
                    sys.stdout.write(m + "\n")
            except KeyError:
                continue

