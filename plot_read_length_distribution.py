import matplotlib.pyplot as plt
with open('MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.fasta') as f:
    lens = [len(l.strip()) for l in f if l[0]!='>']

plt.hist(lens, bins=80)
plt.title('MX_260102 seq lengths.')
plt.show()