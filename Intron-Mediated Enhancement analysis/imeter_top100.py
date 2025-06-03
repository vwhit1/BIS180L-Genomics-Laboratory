import argparse
import sys
import korflab
import math

def read_kmer_table(filename):
	kmer_table = {}
	with open(filename, "r") as file:
		for line in file:
			line = line.strip()
			line = line.split()
			kmer_table[line[0]] = float(line[1])
	return kmer_table
        

parser = argparse.ArgumentParser(description='the IMEter')
parser.add_argument('fasta', help='input fasta file')
parser.add_argument('prox', help='proximal kmer file')
parser.add_argument('dist', help='distal kmer file')
parser.add_argument('k', type=int, help='kmer size')
parser.add_argument('n', type=int, help='top n sequences')
arg = parser.parse_args()

prox = read_kmer_table(arg.prox)
dist = read_kmer_table(arg.dist)

if arg.k > 10: sys.exit(f'{sys.argv[0]} not designed for large values of k')
#kdict = korflab.kmers(arg.k)
#print(kdict)

all_seqs = []

#outfile = open("imeter_out.tsv", "w")

for name, seq in korflab.readfasta(arg.fasta):
	score = 0
	kdict = korflab.kmers(arg.k, init=0)
	
	# Create kmer prob table for the input fasta
	for i in range(len(seq) - arg.k + 1):
		kmer = seq[i:i+arg.k]
		if kmer in kdict: kdict[kmer] += 1
	
	# Score each kmer and sum it for overall score
	for k in kdict.keys():
		score += kdict[k] * math.log2(prox[k]/dist[k])
		# Multiply how frequently each kmer occurs here
		# by how likely the kmer is to be prox vs dist
		# (negative multiplier for more dist than prox,
		# positive multiplier for more likely prox)
	
	all_seqs.append((name, seq, score))
	#print(score)
	#outfile.write(f"{score}\t{expression}\n")
	
top_seqs = sorted(all_seqs, key=lambda x: x[2])[:arg.n]
for seq in top_seqs:
	print(">",seq[0],"\n",seq[1],"\n", sep='', end='')
	

	

#outfile.close()
