#!/bin/bash

for seqlen in {25..400..25}; do
	echo Working on size $seqlen
	makeprotseq\
		-pepstatsfile E.coli.aggregated.pepstats\
		-amount 10000\
		-length $seqlen\
		-outseq sequences_data/$seqlen.fa
	water\
		-asequence sequences_data/$seqlen.fa\
		-bsequence sequences_data/$seqlen.fa\
		-gapopen 10\
		-gapextend 1\
		-outfile results/$seqlen.align
	grep Score results/$seqlen.align | cut -f3 -d " " | tail -9999 \
		> results/$seqlen.txt
done
