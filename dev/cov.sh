#!/bin/sh
# http://wiki.apertium.org/wiki/Asturian#Calculating_coverage


# Example use:
# zcat corpa/en.crp.txt.gz | sh corpus-stat.sh

TARGET=$1


#CMD="cat corpa/en.crp.txt"
CMD="cat"

CRP=$1
F0=/tmp/uig-tur.raw.txt
F1=/tmp/uig-tur.morph.txt
F2=/tmp/uig-tur.postchunk.txt
F3=/tmp/uig-tur.gen.txt

$CMD | grep -v '^ *$' > $F0

# Calculate the number of tokenised words in the corpus:
# for some reason putting the newline in directly doesn't work, so two seds
$CMD $F0 | apertium-destxt | lt-proc -w uig-tur.automorf.bin |apertium-retxt | sed 's/\$\W*\^/$\n^/g' | grep -v '^ *$' > $F1
$CMD $F0 | apertium -d . uig-tur-postchunk2 2>/dev/null | sed 's/\$\W*\^/$\n^/g' | grep -v '^ *$' | tee $F2 | lt-proc -d uig-tur.autogen.bin > $F3
NUMWORDS=`cat $F1 | wc -l`
echo "Number of tokenised words in the corpus: $NUMWORDS"

# Calculate the number of words that are not unknown

NUMKNOWNWORDS=`cat $F1 | grep -v '\*' | wc -l`
NUMTRIMMED=`cat $F3| grep -v '#' | grep -v '\*' | grep -v '@' | wc -l `
NUMTOTAL=`cat $F3| wc -l `
echo "Number of known words in the corpus: $NUMKNOWNWORDS"

TARGETFORMS=`calc "($NUMTOTAL/100)*$TARGET"`
REMAININGFORMS=`calc $TARGETFORMS-$NUMTRIMMED`

# Calculate the coverage

COVERAGE=`calc "round($NUMKNOWNWORDS/$NUMWORDS*1000)/10"`
TRIMCOV=`calc "round($NUMTRIMMED/$NUMTOTAL*1000)/10"`
echo "Coverage: $COVERAGE %"
echo "Trimmed coverage: $TRIMCOV %"
echo "Forms to $TARGET%: $REMAININGFORMS"

#If you don't have calc, change the above line to:
#COVERAGE=$(perl -e 'print int($ARGV[0]/$ARGV[1]*1000)/10;' $NUMKNOWNWORDS $NUMWORDS)

# Show the top-ten unknown words.

echo "Top unknown words in the corpus:"
cat $F1 | grep '\*' | sort -f | uniq -c | sort -gr > /tmp/uig-tur.hitparade.txt
paste $F2 $F3 | sort -f | uniq -c | sort -gr | grep '#' > /tmp/uig-tur.genparade.txt
cat /tmp/uig-tur.hitparade.txt | head -n 100


