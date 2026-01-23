import math
import statistics
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import numpy as np


def ref_to_location():
    # ref num to (row, line) # line is the 2nd col in JM's file
    with open('/home/magda/Projects/MaverickQC/Ink005-262144-randomTags-probe-location.txt') as f:
        lines = sorted([l.split('\t')[:3] for l in f], key=lambda x: int(x[1]))
    for line in lines:
        line[2] = line[2].split('-')[1]
    line_dict = dict()
    for line in lines:
        line_dict[int(line[2])] = (int(line[1]), int(line[0]))
    return line_dict


data = np.zeros((512, 512))
with open('/home/magda/Projects/MaverickQC/MX_260121/MX_260121.extracted.corrected.id0.95.refs_with_cov_min_x1') as f:
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

fig, ax = plt.subplots(figsize=(7, 5.12), dpi=1000)
im = ax.imshow(data, cmap='hot', interpolation='nearest') # 'hot' colormap, 'nearest' interpolation
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.tick_params(axis='y', which='minor', length=4, width=1)
ax.tick_params(axis='y', which='major', length=8, width=1, labelsize=8)
ax.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
fig.colorbar(im, label='Log(Cov)')

# Add title and labels
ax.set_xlabel('MX_260121, 95%')
fig.show()