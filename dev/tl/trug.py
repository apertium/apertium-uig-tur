import sys,os
from collections import OrderedDict

def readfile(tu=True):
    lets = OrderedDict()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    t_path = os.path.join(dir_path,"t.csv")
    with open(t_path) as infile:
        for line in infile:
            a,b = line.split(";")
            if tu:
                lets[b.strip()] = a.strip()
            else:
                lets[a.strip()] = b.strip()
    return lets


if __name__=="__main__":
    if "--ut" in sys.argv:
        lets = readfile(False)
    else:
        lets = readfile(True)
    for line in sys.stdin.readlines():
        out = line
        for key in lets:
            try:
                out = out.replace(key,lets[key])
            except KeyError:
                continue
        sys.stdout.write(out + "\n")
