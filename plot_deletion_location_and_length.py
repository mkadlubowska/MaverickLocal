from matplotlib import pyplot as plt

del_locations = []
del_lengths = []

with open('/home/mkk/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.maxhits1.both_strands.mincols50.top_hits_only.id0.85.tsv') as f:
    strings = [l.split('\t')[-2] for l in f]

for s in strings[:3]:
    i = 0
    length = 0
    while i < len(s):
        if s[i] == '-':
            del_locations.append(i)
            length += 1
        else:
            if length > 0:
                del_lengths.append(length)
            length = 0
        i += 1

plt.hist(del_locations, bins=50)
plt.title('MX_260102 deletion locations; ID 85%')
plt.savefig('MX_260102_deletion_locations_id0.85.png')
plt.close()

plt.hist(del_lengths, bins=8)
plt.title('MX_260102 deletion lengths; ID 85%')
plt.savefig('MX_260102_deletion_lengths_id0.85.png')
plt.close()