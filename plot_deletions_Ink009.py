import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def ref_to_location():
    # ref num to (row, line) # line is the 2nd col in JM's file
    with open('/home/mkk/Projects/MaverickQC/Ink005-262144-randomTags-probe-location.txt') as f:
        lines = sorted([l.split('\t')[:3] for l in f], key=lambda x: int(x[1]))
    ref_to_location_dict = dict()
    for line in lines:
        ref_to_location_dict[line[2]] = (int(line[1]), int(line[0]))
    return ref_to_location_dict


def ref_to_deletion_count_dict_vsearch():
    """
    This uses 50-Mcount as deletions.
    """
    del_count_dict = {f'{i}': 50 for i in range(1, 512*512+1)}
    with open('/home/mkk/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.maxhits1.both_strands.mincols50.top_hits_only.id0.9.tsv') as f:
        lines = [[l.split('\t')[0], l.split('\t')[10].count('M')] for l in f]
    refs_to_aln_lengths = dict()
    for line in lines:
        ref = line[0]
        matches = line[1]
        if ref in refs_to_aln_lengths.keys():
            refs_to_aln_lengths[ref].append(matches)
        else:
            refs_to_aln_lengths[ref] = [matches]
    for ref in refs_to_aln_lengths.keys():
        avg_aln_len = sum(refs_to_aln_lengths[ref]) / len(refs_to_aln_lengths[ref])
        del_count_dict[ref] = 50 - avg_aln_len
    return del_count_dict

location_di
del_count_dict = ref_to_deletion_count_dict_vsearch()
data = np.zeros((512, 512))
#
for ref in del_count_dict.keys():
#     # if del_count_dict[ref] == 0:
#     #     del_count_dict[ref] = 0.0000000001
#     old_value = del_count_dict[ref]
#     line = int(ref) -1
#     new_value = 86 * (1 - 1/(old_value + 1))
#     data[line, :] = old_value

# Plot the heatmap

masked_data = np.ma.masked_where(data == 50, data)

# Get the 'hot' colormap and set the masked color
cmap = cm.hot_r
cmap.set_bad(color='grey')
plt.imshow(masked_data, cmap=cmap, interpolation='nearest')  # 'hot' colormap, 'nearest' interpolation

# Add a colorbar
plt.colorbar(label='DELs')

# Add title and labels
plt.xlabel('Ink009, MX_260102, ID 90%')
# plt.xlabel('Columns')

plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
# plt.ylabel('Rows')
# Display the plot
plt.show()

# plt.hist([round(d) for d in del_count_dict.values()], bins=62)
# plt.title('Vsearch 95% - deletion counts per ref')
# plt.show()