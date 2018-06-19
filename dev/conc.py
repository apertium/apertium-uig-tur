import sys
import re

def concordance(filename,keyword,n=30,rtl=True):
    RED,END,BOLD = '\033[91m','\033[0m','\033[1m'
    dots = "("+ "." * n + ")"
    keyword = "(" + keyword.strip() + "\w*" +  ")"
    exp = re.compile(dots + keyword + dots)
    with open(filename) as infile:
        for line in infile:
            e = exp.search(line)
            if not e:
                continue
            fspace = "".join([" " for i in range(0,8-(len(e.group(2))-len(keyword)))] )
            nspace = "        "
            if rtl:
                out = e.group(3) + fspace +RED + BOLD +  e.group(2) + END+ nspace + e.group(1)
            else:
                out = e.group(1) + fspace +RED + BOLD +  e.group(2) + END+ nspace + e.group(3)
            out = "..." + out + "..."
            print(out)

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 conc.py WORD file.txt")
        quit(0)
    w = sys.argv[1]
    f = sys.argv[2]
    concordance(f,w)
