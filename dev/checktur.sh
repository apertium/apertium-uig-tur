cat apertium-uig-tur.uig-tur.dix | grep "<e>" | sed "s/.*<r>//" > /tmp/first.txt
cat /tmp/first.txt  |  cut -f1 -d "<" | apertium -d ../apertium-tur tur-morph > /tmp/second.txt
paste /tmp/first.txt /tmp/second.txt | sed "s/\(.*\)\t\(.*\)/\2\t\1/"  | rev |sort -u |rev | sed "s/\(.*\)\t\(.*\)/\2\t\1/" > /tmp/third.txt
python3 dev/ayikla.py 

