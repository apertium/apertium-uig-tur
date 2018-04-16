import sys

def monofy(line):
    dic = { '<s n="adj"/>':'A1','<s n="adv"/>':"ADV",'<s n="n"/>':"N1",
            '<s n="np"/><s n="top"/>':"NP-TOP",'<s n="post"/>':"POST",
            '<s n="prn"/><s n="itg"/>':"PRON-ITG",
            '<s n="det"/><s n="itg"/>':"DET-ITG",
            '<s n="adv"/><s n="itg"/>':"ADV-ITG",
            '<s n="v"/><s n="iv"/>':"V-IV",
            '<s n="v"/><s n="tv"/>':"V-TV"}


    word = line.partition("<l>")[2].partition("<s")[0]
    tags= "".join(line.partition("<s")[1:]).partition("</l>")[0]
    word = word.replace("<b/>","% ")
    entry = word + ":" + word + " " + dic[tags] + " ; !"
    return entry


if __name__=="__main__":
    for line in sys.stdin.readlines():
        if "<e><p><l>" in line:
            try:
                sys.stdout.write(monofy(line) + "\n")
            except KeyError:
                print("Unknown tags!")
                continue
