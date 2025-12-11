import os
import statistics
from collections import Counter
from matplotlib import pyplot as plt

files = os.listdir('beds')


common_alignments = dict()
for file in files:
    sample = file.split('.')[0]
    with open(os.path.join('beds', file), 'r') as f:
        lines = [l.strip().split('\t') for l in f.readlines()]
    starts = []
    stops = []
    lengths = []
    alignments =  []
    refs = set()
    for line in lines:
        starts.append(int(line[1]))
        stops.append(int(line[2]))
        lengths.append(int(line[2]) - int(line[1]))
        alignments.append(f'{line[1]}-{line[2]}')
        refs.add(line[0])
    print(f'\n\n***** {sample} *****')
    print(f'Num refs with cov: {len(refs):,} ({round(len(refs)*100/147456, 2)}%)')
    # print(f'Total alignments: {len(lines):,}')
    # print(f'Median alignment length: {statistics.median(lengths)}')
    # print(f'Min alignment length: {min(lengths)}; Max alignment length: {max(lengths)}')
    # print(f'Median start position: {statistics.median(starts)}')
    # print(f'Max start position: {max(starts)}')
    # common_alignments[sample] = Counter(alignments).most_common()
    # plot = plt.hist(lengths, bins=len(set(lengths)), color='green')
    # plt.title(f'{sample} - Alignment lengths')
    # plt.xlabel('Alignment length')
    # plt.ylabel('Count')
    # plt.show()
    # plt.savefig(f'plots_aln/{sample}-alignment_lengths.png')
    # plt.close()
    # plot = plt.hist(starts, bins=len(set(starts)))
    # plt.title(f'{sample} - Alignment start positions')
    # plt.xlabel('Alignment start position')
    # plt.ylabel('Count')
    # plt.show()
    # plt.savefig(f'plots/{sample}-alignment_start_positions.png')
    # plt.close()

