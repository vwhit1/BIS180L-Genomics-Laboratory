import os

#folder = "build"
folder = "compare_split_k"
splits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

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
        #if folder == "build":
        cmd5 = f'python3 imeter.py db_IME_Rose_WT_introns.fa.gz {proxk} {distk} {k} > {ime}'
        #else:
        #    cmd5 = f'python3 imeter.py introns.fa {proxk} {distk} {k} > {ime}'
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
