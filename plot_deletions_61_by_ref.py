import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def ref_to_deletion_count_dict_vsearch():
    """
    This uses 61-Mcount as deletions.
    """
    del_count_dict = {f'{i}': 61 for i in range(1, 256+1)}
    with open('/home/magda/Projects/MaverickQC/QC_251208/MX_251208_7387.trimmed.mincols61.id0.95.top_hits_only.tsv') as f:
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
        del_count_dict[ref] = 61 - avg_aln_len
    return del_count_dict

def get_deletion_dict(alignment_file):
    deletion_dict = dict()
    for i in range(1,257):
        deletion_dict[i] = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'cov': 0}
    with open(alignment_file) as f:
        lines = [l.strip().split('\t') for l in f.readlines()]
    for line in lines:
        ref = int(line[0])
        target_seq = line[-1]
        read_seq = line[-2]
        missing_a = target_seq.count('A') - read_seq.count('A')
        if missing_a < 0:
            missing_a = 0
        missing_c = target_seq.count('C') - read_seq.count('C')
        if missing_c < 0:
            missing_c = 0
        missing_g = target_seq.count('G') - read_seq.count('G')
        if missing_g < 0:
            missing_g = 0
        missing_t = target_seq.count('T') - read_seq.count('T')
        if missing_t < 0:
            missing_t = 0
        deletion_dict[ref]['cov'] += 1
        deletion_dict[ref]['A'] += missing_a
        deletion_dict[ref]['C'] += missing_c
        deletion_dict[ref]['G'] += missing_g
        deletion_dict[ref]['T'] += missing_t
    for ref in deletion_dict.keys():
        if deletion_dict[ref]['cov'] > 0:
            deletion_dict[ref]['A'] /= deletion_dict[ref]['cov']
            deletion_dict[ref]['C'] /= deletion_dict[ref]['cov']
            deletion_dict[ref]['G'] /= deletion_dict[ref]['cov']
            deletion_dict[ref]['T'] /= deletion_dict[ref]['cov']
    return deletion_dict

id = 0.9
deletion_dict = get_deletion_dict(f'/home/mkk/Projects/MaverickQC/QC_251208/MX_251208_7387-primer_trimmed_reads-id{id}-alignment_userfields')
data_a = np.zeros((256, 512))
data_c = np.zeros((256, 512))
data_g = np.zeros((256, 512))
data_t = np.zeros((256, 512))

with open(f'QC_251208/MX_251208_7387-primer_trimmed_reads-id{id}_deletions_per_ref.tsv', 'w') as f:
    f.write(f'#REF\tA deletions/cov\tC deletions/cov\tG deletions/cov\tT deletions/cov\n')
    for ref in sorted(deletion_dict.keys()):
        if deletion_dict[ref]['cov'] >= 0:
            data_a[ref-1, :] = deletion_dict[ref]['A']
            data_c[ref-1, :] = deletion_dict[ref]['C']
            data_g[ref-1, :] = deletion_dict[ref]['G']
            data_t[ref-1, :] = deletion_dict[ref]['T']
            f.write(f'seq{ref}\t{deletion_dict[ref]["A"]}\t{deletion_dict[ref]["C"]}\t{deletion_dict[ref]["G"]}\t{deletion_dict[ref]["T"]}\n')
        else:
            data_a[ref-1, :] = -1
            data_c[ref-1, :] = -1
            data_g[ref-1, :] = -1
            data_t[ref-1, :] = -1
            f.write(f'seq{ref}\t-\t-\t-\t-\n')




# Plot the heatmap

masked_a_data = np.ma.masked_where(data_a == -1, data_a)
masked_c_data = np.ma.masked_where(data_c == -1, data_c)
masked_g_data = np.ma.masked_where(data_g == -1, data_g)
masked_t_data = np.ma.masked_where(data_t == -1, data_t)

# Get the 'hot' colormap and set the masked color
cmap = cm.hot_r
cmap.set_bad(color='green')

#A deletions
plt.imshow(masked_a_data, cmap=cmap, interpolation='nearest')  # 'hot' colormap, 'nearest' interpolation
plt.colorbar(label='DELs/cov') # Add a colorbar
plt.xlabel(f'Ink006, MX_251208, ID {id*100}%, A deletions') # Add title and labels
plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
plt.show()

#C deletions
plt.imshow(masked_c_data, cmap=cmap, interpolation='nearest')  # 'hot' colormap, 'nearest' interpolation
plt.colorbar(label='DELs/cov') # Add a colorbar
plt.xlabel(f'Ink006, MX_251208, ID {id*100}%, C deletions') # Add title and labels
plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
plt.show()

#G deletions
plt.imshow(masked_g_data, cmap=cmap, interpolation='nearest')  # 'hot' colormap, 'nearest' interpolation
plt.colorbar(label='DELs/cov') # Add a colorbar
plt.xlabel(f'Ink006, MX_251208, ID {id*100}%, G deletions') # Add title and labels
plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
plt.show()

#T deletions
plt.imshow(masked_t_data, cmap=cmap, interpolation='nearest')  # 'hot' colormap, 'nearest' interpolation
plt.colorbar(label='DELs/cov') # Add a colorbar
plt.xlabel(f'Ink006, MX_251208, ID {id*100}%, T deletions') # Add title and labels
plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)
plt.show()

all = np.array([masked_a_data[:,0], masked_c_data[:,0], masked_g_data[:,0], masked_t_data[:,0]])
print(all)


