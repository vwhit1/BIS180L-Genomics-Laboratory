import argparse
import os

parser = argparse.ArgumentParser(description='run IMEter with specified split point and k size')
parser.add_argument('folder', help='folder to run in')
# Intron file arg is unnecessary. imeter.py is built to take Rose introns only
#parser.add_argument('intron_file', help='intron file to run IMEter on')
parser.add_argument('split_start', help='first split location (bp)', type=int)
parser.add_argument('split_end', help='last split location (bp)', type=int)
parser.add_argument('-s', '--splitby', help='interval between splits', default=100, type=int)
parser.add_argument('kmer_start', help='first kmer length', type=int)
parser.add_argument('kmer_end', help='last kmer length', type=int)
parser.add_argument('-k', '--kmerby', help='interval between kmers', default=1, type=int)
arg = parser.parse_args()

folder = arg.folder
#intron_file = arg.intron_file
splits = list(range(arg.split_start, arg.split_end + arg.splitby, arg.splitby))
ks = list(range(arg.kmer_start, arg.kmer_end + arg.kmerby, arg.kmerby))
#print(splits)
#print(ks)

for split in splits:
    for k in ks:
        proxfa = f'{folder}/prox-{split}.fa'
        distfa = f'{folder}/dist-{split}.fa'
        proxk = f'{folder}/prox-{split}-k{k}.tsv'
        distk = f'{folder}/dist-{split}-k{k}.tsv'
        ime = f'{folder}/imeter-{split}-k{k}.tsv'
        cmd1 = f'python3 isplitter.py introns.fa {split} > {proxfa}'
        cmd2 = f'python3 isplitter.py introns.fa {split} --high > {distfa}'
        cmd3 = f'python3 kmercount.py --prob {folder}/prox-{split}.fa {k} > {proxk}'
        cmd4 = f'python3 kmercount.py --prob {folder}/dist-{split}.fa {k} > {distk}'
        cmd5 = f'python3 imeter.py db_IME_Rose_WT_introns.fa.gz {proxk} {distk} {k} > {ime}'
        print(cmd1, cmd2, cmd3, cmd4, cmd5, sep='\n')
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
