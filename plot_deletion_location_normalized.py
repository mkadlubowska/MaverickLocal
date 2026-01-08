from matplotlib import pyplot as plt

del_locations_reads = []
del_locations_consensus = []

alignment_dict = {}



with open('/home/mkk/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.maxhits1.both_strands.mincols50.top_hits_only.id0.85.tsv') as f:
    lines = [l.split('\t') for l in f]

for line in lines[:10]:
    if line[0] in alignment_dict:
        alignment_dict[line[0]].append(line[-2])
    else:
        alignment_dict[line[0]] = [line[-2]]

for ref, alignments in alignment_dict.items():
    for i in range(50):
        bases = [s[i] for s in alignments]
        dels = bases.count('-')
        if dels > .5*len(bases):
            del_locations_consensus.append(i)

plt.hist(del_locations_consensus, bins=50)
plt.title('MX_260102 deletion locations (consensus based); ID 85%')
plt.savefig('MX_260102_deletion_locations_cons_id0.85.png')
plt.close()

