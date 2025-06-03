import korflab

file = "db_IME_Rose_WT_introns.fa.gz"

#print(type(korflab.readfasta(file)))

test = [(1,2),(4,5),(6,7),(8,9)]
print(test[3][1])

num = 1
if num in test:
	print("yes")
