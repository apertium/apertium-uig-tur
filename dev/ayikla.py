third = "/tmp/third.txt"

with open(third) as infile:
    lines = [x.strip("\n").strip().split("^") for x in infile.readlines()]

unk, probs = [],[]

for item in lines:
    if len(item)<2:
        continue
    if "<s n" not in item[0]:
        continue
    if "*" in item[1]:
        unk.append(item)
        continue
    left,right = item[0], item[1]
    left_tag = left.partition('s n="')[2].partition('"')[0] 
    rt = []
    right_tags = item[1].split("/")
    for r in right_tags:
        if "<" not in r:
            continue
        tag = r.partition("<")[2].partition(">")[0]
        rt.append(tag)
    if left_tag not in rt:
        probs.append(item)
    

print("Completely Unknown:",len(unk))
for item in unk:
    print("^".join(item))
print("Tag mismatch:", len(probs))
for item in probs:
    print("^".join(item))

