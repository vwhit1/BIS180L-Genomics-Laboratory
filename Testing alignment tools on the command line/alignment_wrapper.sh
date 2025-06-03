for seqlen in 25 50 75 100 125 150 175 200 225; do
	makeprotseq \
		-pepstatsfile E.coli.pepstats \
		-amount 1000 \
		-length $seqlen \
		-outseq sequences_data/$seqlen.fa
	water \
		-asequence sequences_data/$seqlen.fa \
		-bsequence sequences_data/$seqlen.fa \
		-gapopen 10 \
		-gapextend 1 \
		-outfile results/$seqlen.align
	grep Score results/$seqlen.align | cut -f3 -d " " | tail -999 | \
		python3 stats.py > results/$seqlen.stats
done
