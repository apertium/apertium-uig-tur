import sys, os

def monofy(line,left=True):
    dic = { '<s n="adj"/>':'A1',
'<s n="adv"/>':"ADV",'<s n="n"/>':"N1",
            '<s n="np"/><s n="top"/>':"NP-TOP",
'<s n="post"/>':"POST",
            '<s n="np"/><s n="cog"/><s n="mf"/>':"NP-COG",
            '<s n="np"/><s n="org"/>':"NP-ORG",
            '<s n="prn"/><s n="itg"/>':"PRON-ITG",
            '<s n="det"/><s n="itg"/>':"DET-ITG",
            '<s n="adv"/><s n="itg"/>':"ADV-ITG",
            '<s n="v"/><s n="iv"/>':"V-IV",
            '<s n="cnjcoo"/>':"CC",
            '<s n="ij"/>':"INTERJ",
            '<s n="cnjsub"/>':"CS",
            '<s n="np"/><s n="ant"/><s n="m"/>':'NP-ANT-M',
            '<s n="np"/><s n="ant"/><s n="f"/>':'NP-ANT-F',
            '<s n="cnjadv"/>':"CA",
            '<s n="v"/><s n="tv"/>':"V-TV",
	    '<s n="det"/><s n="qnt"/>':"DET-QNT"
}

    if left:
        word = line.partition("<l>")[2].partition("<s")[0]
        tags= "".join(line.partition("<s")[1:]).partition("</l>")[0]
    else:
        word = line.partition("<r>")[2].partition("<s")[0]
        tags= "".join(line.partition("<r>")[2].partition("<s")[1:]).partition("</r>")[0]
    word = word.replace("<b/>","% ")
    entry = word + ":" + word + " " + dic[tags] + " ; !"
    return entry


if __name__=="__main__":
    d = os.path.dirname(__file__)
    filename = os.path.join(d, '../../apertium-uig/apertium-uig.uig.lexc')
    text = open(filename).read()
    left = True
    if "-tur" in sys.argv: left=False
    for line in sys.stdin.readlines():
        if "<e><p><l>" in line:
            try:
                m = monofy(line,left)
                if m not in text:
                    sys.stdout.write(m + "\n")
            except KeyError:
                print("Unknown tags:",line)
                continue
