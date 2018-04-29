cat apertium-uig-tur.uig-tur.dix | grep "<e>" | sed "s/<r>.*//" > /tmp/first.txt
cat /tmp/first.txt  | cut -f4 -d ">" | cut -f1 -d "<" | apertium -d ../apertium-uig uig-morph > /tmp/second.txt
paste /tmp/first.txt /tmp/second.txt > /tmp/third.txt
python3 dev/ayikla.py

