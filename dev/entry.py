import sys


def entrify(line):
    line = line.strip("\n")
    pos_tags = {"Adj":'<s n="adj"/>',"Adv":'<s n="adv"/>',
    "C":'<s n="cnjcoo"/>',"iv":'<s n="v"/><s n="iv"/>',"N":'<s n="n"/>',"post":'<s n="post"/>',
    "Pronoun":'<s n="prn"/><s n="pers"/>',"top":'<s n="np"/><s n="top"/>',
    "tv":'<s n="v"/><s n="tv"/>'}
    epl, rpe, lr = "       <e><p><l>", "</r></p></e>", "</l><r>"
    out = ""
    a = [x.strip() for x in line.split("\t")]
    if len(a)<3 or a[0] not in pos_tags:
        return out
    out = epl + a[2].replace(" ","<b/>")+pos_tags[a[0]] + lr 
    out += a[1].replace(" ","<b/>")+pos_tags[a[0]] + rpe
    return out

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    rev  = sorted([x[::-1] for x in map(entrify,lines) if len(x)>2])
    entries = [x[::-1] for x in rev]
    for e in entries:
        print(e)