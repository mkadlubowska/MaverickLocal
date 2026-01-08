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
with open('/home/mkk/Projects/MaverickQC/MX_260102/perfect_refs_id0.95_uniq') as f:
    perfect_refs = [int(l.strip()) for l in f.readlines()]

location_dict = ref_to_location()

for r in perfect_refs:
    ref = int(r)
    r, c = location_dict[ref]
    data[r,c] =1

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
#plt.colorbar(label='Log(Cov)')

# Add title and labels
plt.xlabel('MX_260102, 95%; Perfect oligos (white = perfect)')
# plt.xlabel('Rows')
# plt.ylabel('Columns')
# Display the plot
plt.show()