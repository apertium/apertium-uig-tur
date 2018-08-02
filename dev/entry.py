import sys,os


def entrify(line):
    line = line.strip("\n")
    pos_tags = {
"Adj":'<s n="adj"/>',
"Adv":'<s n="adv"/>',
"C":'<s n="cnjcoo"/>',
"iv":'<s n="v"/><s n="iv"/>',
"N":'<s n="n"/>',
"post":'<s n="post"/>',
"Pronoun":'<s n="prn"/><s n="pers"/>',
"top":'<s n="np"/><s n="top"/>',
"tv":'<s n="v"/><s n="tv"/>',
"ant":'<s n="np"/><s n="ant"/><s n="m"/>',
"antf":'<s n="np"/><s n="ant"/><s n="f"/>',
"cog":'<s n="np"/><s n="cog"/><s n="mf"/>',
"interj":'<s n="ij"/>',
"org":'<s n="np"/><s n="org"/>',
"al":'<s n="np"/><s n="al"/>',
"num":'<s n="num"/>',
"det":'<s n="det"/><s n="dem"/>'
}
    epl, rpe, lr = "       <e><p><l>", "</r></p></e>", "</l><r>"
    out = ""
    a = [x.strip() for x in line.split("\t")]
    if len(a)<3 or a[0] not in pos_tags:
        return out
    out = epl + a[2].replace(" ","<b/>")+pos_tags[a[0]] + lr 
    out += a[1].replace(" ","<b/>")+pos_tags[a[0]] + rpe
    return out

if __name__ == "__main__":
    d = os.path.dirname(__file__)
    bidix = os.path.join(d, "../apertium-uig-tur.uig-tur.dix")
    items = set([x.strip("\n").strip() for x in open(bidix).readlines()])
    lines = sys.stdin.readlines()
    rev  = sorted([x[::-1] for x in map(entrify,lines) if len(x)>2])
    entries = [x[::-1] for x in rev]
    for e in entries:
        if e.strip() not in items:
            print(e)
