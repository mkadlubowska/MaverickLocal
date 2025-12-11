import os
import statistics
from collections import Counter
from matplotlib import pyplot as plt

files = os.listdir('/home/mkk/Projects/MaverickQC/vsearch6')


common_alignments = dict()
for file in files:
    sample = file.split('.')[0]
    with open(os.path.join('vsearch6', file), 'r') as f:
        lines = [l.strip().split('\t') for l in f.readlines()]
    starts = []
    lengths = []
    cigars = []
    alignments = []
    refs = set()
    for line in lines:
        refs.add(line[0])
        starts.append(int(line[2]))
        lengths.append(int(line[3])-int(line[2])+ 1)
        cigars.append(line[-1])
        alignments.append(f'{line[2]}-{line[3]}')
    print(f'\n\n***** {sample} *****')
    print(f'Total alignments: {len(lines):,}')
    print(f'Median alignment length: {statistics.median(lengths)}')
    print(f'Min alignment length: {min(lengths)}; Max alignment length: {max(lengths)}')
    print(f'Median start position: {statistics.median(starts)}')
    print(f'Max start position: {max(starts)}')
    print(f'Number of ref seqs with >=x1 cov: {len(refs)} ({round(100*len(refs)/147456,2)}%)')
    common_alignments[sample] = Counter(alignments).most_common()
    plot = plt.hist(lengths, bins=len(set(lengths)), color='green')
    plt.title(f'{sample} - Alignment lengths (vsearch)')
    plt.xlabel('Alignment length')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'plots_vsearch6/{sample}-alignment_lengths-aln.png')
    plt.close()
    plot = plt.hist(starts, bins=len(set(starts)))
    plt.title(f'{sample} - Alignment start positions (vsearch)')
    plt.xlabel('Alignment start position')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'plots_vsearch6/{sample}-alignment_start_positions-aln.png')
    plt.close()

