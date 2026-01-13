import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit('Usage: /tools/bin/.venv/bin/python plot_wafer_heatmap.py <input_file> <output_file>\n'
             'input_file is a tab separated file where the first 2 columns are the coordinates and the third is the integer representing intensity.')
    data = np.zeros((512, 512))
    with open(sys.argv[1]) as f:
        vals = [l.strip().split('\t') for l in f.readlines()]

    for line in vals:
        assert len(line) == 3
        r, c, val = line
        data[int(r)-1,int(c)-1] = float(val)


    plt.imshow(data, cmap='hot', interpolation='nearest') # 'hot' colormap, 'nearest' interpolation
    plt.colorbar()
    plt.tick_params(labeltop=True, labelbottom=False, bottom=False, top=True)

    #plt.xlabel('TITLE')

    plt.savefig(sys.argv[2])