import re, sys
import time

def tags(t):
    if type(t) == str: return '<s n="' + t.strip() + '"/>'
    elif type(t) == list: return "".join([tags(x) for x in t])

def mono_lexc_entry_read(line):
    entry = re.compile(r'([\S(?:% )]*):([\S(?:% )]*?)\s*(\S*)\s*;(\s*!.*)?')
    return entry.match(line)

def bidix_entry_read(line):
    entry = re.compile(r'\s*<e\s*.*?\s*><p><l>(.*?)(?:<s n=".*?"/>)*</l><r>(.*?)<s')
    t  = re.compile(r'<s n="(.*?)"/>')
    try:
        l,r = line.split("<r>")
    except ValueError:
        return None
    ltags, rtags  = re.findall(t,l), re.findall(t,r)
    m = entry.match(line)
    if not m: return None
    lw, rw = m.groups()
    return lw, rw, ltags,rtags

def bidix_entry_build(lw,rw,ltags,rtags,dr=None):
    lw,rw = lw.strip().replace(" ","<b/>"), rw.strip().replace(" ","<b/>")
    out = "     <e"
    if dr:
        out += " r=" + dr
    out += "><p><l>" + lw + tags(ltags) + "</l><r>" + rw + tags(rtags) + "</r></p></e>"
    return out

if __name__ == "__main__":
    counter = 0
    s = set()
    t = time.clock()
    for line in sys.stdin.readlines():
        m = bidix_entry_read(line)
        if not m:
            continue
        if " " in m[1] or " " in m[3]:
            print(line)
    print(time.clock()-t)
    
