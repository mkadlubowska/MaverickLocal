import math
from collections import Counter

in_file = '/home/mkk/Projects/MaverickQC/QC_251113/MX_251113_7444.perfect3primerBothOrientations.maxhits1.both_strands.mincols46.top_hits_only.id0.84.tsv'
lines = []
pages = []
with open(in_file, 'r') as f:
    ref_numbers = [int(l.strip().split('\t')[0].split('-')[1]) for l in f.readlines()]

for entry in ref_numbers:
    lines.append(math.floor(entry/512))
    pages.append(math.floor(entry/(512*256)))

print(Counter(lines).most_common(5))
print(Counter(pages).most_common(5))
print(f'Detected {len(set(lines))} lines.')
print(Counter(lines).most_common()[-5:])

################### FOR 20MERs ############################################
## For 7443 ID 0.84:
# [(140, 48952), (61, 11915), (469, 11731), (233, 11357), (0, 10886)]
# [(0, 1403697), (1, 828113), (2, 1)]

## For 7444 ID 0.84:
# [(140, 50489), (61, 16259), (233, 15771), (0, 12929), (32, 11056)]
# [(0, 1451010), (1, 849084), (2, 2)]

## For 7443 ID 0.87:
# [(140, 40015), (6, 10514), (233, 9863), (38, 6829), (259, 6036)]
# [(0, 677571), (1, 466655)]

## For 7444 ID 0.87:
# [(140, 39633), (6, 15519), (233, 14839), (34, 8460), (38, 7697)]
# [(0, 710753), (1, 478549), (2, 1)]

## For 7443 ID 0.9:
# [(6, 6593), (253, 3135), (259, 2817), (330, 2803), (409, 1947)]
# [(0, 121671), (1, 94556)]
# Detected 512 lines.

## For 7444 ID 0.9:
# [(6, 10635), (234, 4972), (257, 2930), (233, 2358), (330, 2342)]
# [(0, 126448), (1, 96595)]
# Detected 512 lines.

## The least common lines for id 0.9 still have >= 160 hits

################### FOR FULL LENGTH ID 0.84 ##################################
## For 7443 ID 0.84:
# [(12, 2094), (145, 843), (408, 247), (208, 136), (479, 110)]
# [(0, 6354), (1, 2549)]
# Detected 511 lines.
# [(396, 1), (503, 1), (374, 1), (277, 1), (481, 1)]

## For 7444 ID 0.84: