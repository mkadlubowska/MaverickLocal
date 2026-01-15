from matplotlib import pyplot as plt
from collections import Counter
three_prime_bases = []

alignment_dict = {}  # ref seq is the key,


with open('/home/magda/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.primer_corrected.maxhits1.both_strands.mincols50.top_hits_only.id0.85.tsv') as f:
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
    last_deleted_position = 0
    for i in range(50):
        bases = [s[i] for s in alignments]
        dels = bases.count('-')
        if dels > .5*len(bases):
            last_deleted_position = i
        else:
            if last_deleted_position > 0:
                three_prime_bases.append(ref_seq[i])
            last_deleted_position = 0

plt.hist(three_prime_bases, bins=4)
plt.title('MX_260102 primer-corrected ID 85%; bases on 3\' of deletion (consensus-based)')
plt.show(dpi=200)
plt.savefig('MX_260102_0.85_primer_corrected-bases_on_3prime-of-deletion.png', dpi=200)
plt.close()
c = Counter(three_prime_bases)
print(c.most_common(4))
