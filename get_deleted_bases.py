from matplotlib import pyplot as plt
from collections import Counter
deleted_bases = []

alignment_dict = {}  # ref seq is the key,


with open('vsearch_to_full/seqs_with_2_near_perfect_fwd_primers.extracted.maxhits1.both_strands.mincols50.top_hits_only.id0.8.tsv') as f:
    lines = [l.split('\t') for l in f]

for line in lines:
    ref_seq = line[-1].replace('-', '')
    if 'I' in ref_seq or 'D' in ref_seq:
        exit(ref_seq) # definitely should not happen
    if ref_seq in alignment_dict:
        alignment_dict[ref_seq].append(line[-2])
    else:
        alignment_dict[ref_seq] = [line[-2]]

for ref_seq, alignments in alignment_dict.items():
    for i in range(50):
        bases = [s[i] for s in alignments]
        dels = bases.count('-')
        if dels > .5*len(bases):
            deleted_bases.append(ref_seq[i])

plt.hist(deleted_bases, bins=4)
plt.title('MX_260102 deleted bases (consensus-based); ID 80%')
plt.savefig('MX_260102_deleted_bases_cons_id0.8.png')
plt.close()
c = Counter(deleted_bases)
print(c.most_common(4))
