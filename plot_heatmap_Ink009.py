import math
import statistics

import matplotlib.pyplot as plt
import numpy as np


def ref_to_location():
    # ref num to (row, line) # line is the 2nd col in JM's file
    with open('/home/mkk/Projects/MaverickQC/Ink005-262144-randomTags-probe-location.txt') as f:
        lines = sorted([l.split('\t')[:3] for l in f], key=lambda x: int(x[1]))
    for line in lines:
        line[2] = line[2].split('-')[1]
    line_dict = dict()
    for line in lines:
        line_dict[int(line[2])] = (int(line[1]), int(line[0]))
    return line_dict


data = np.zeros((512, 512))
with open('/home/mkk/Projects/MaverickQC/MX_260102/MX_260102_seqs_with_2_near_perfect_fwd_primers.extracted.maxhits1.both_strands.mincols50.top_hits_only.id0.9.min.refs_with_cov_min_x1') as f:
    present_refs = [l.strip().split() for l in f.readlines()]

location_dict = ref_to_location()
print(f'Last ref covered: ', max([int(l[1]) for l in present_refs]))
print(f'Num refs not covered: ', 512*512-len(present_refs))
coverages = [int(l[0]) for l in present_refs] + [0]*(262144-len(present_refs))
print(f'Avg coverage: ', statistics.mean(coverages))
print('Median cov: ', statistics.median(coverages))
print(f'Max coverage: ', max(coverages))
for r in present_refs:
    count = int(r[0])
    ref = int(r[1])
    r, c = location_dict[ref]
    data[r,c] = math.log(count) #+= math.log(count)

#data = data[::-1]
# Create the heatmap
# Plot the heatmap
plt.imshow(data, cmap='hot', interpolation='nearest') # 'hot' colormap, 'nearest' interpolation
# plt.tick_params(
#     axis='both',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False,
#     labelleft=False) # labels along the bottom edge are off
plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
# Add a colorbar
plt.colorbar(label='Log(Cov)')

# Add title and labels
plt.xlabel('Ink009-262144-random-20mer-short-primers, MX_260102, 90%')
# plt.xlabel('Rows')
# plt.ylabel('Columns')
# Display the plot
# plt.show()