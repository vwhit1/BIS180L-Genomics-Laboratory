# Count how many sequences are in the file
# and also count the total number of amino acids.

echo 'Count the number of sequences are in E.coli.fa'
grep -c ">" E.coli.fa

echo 'Count the total number of amino acids in E.coli.fa'
chars=$(grep -v ">" E.coli.fa | wc -c)
newlines=$(grep -v ">" E.coli.fa | wc -l)
expr $chars - $newlines
# The way this works is:
# Remove all lines with > in them (the ID lines)
# All characters remaining are amino acids, except the newlines.
# Use the subtraction expression to subtract the number of newlines
# (which is the same as the number of lines, wc -l)
# from the number of characters, wc -c
