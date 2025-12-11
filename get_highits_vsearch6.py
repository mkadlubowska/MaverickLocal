import os

files = os.listdir('/home/mkk/Projects/MaverickQC/vsearch6')

NUM_REFS = 147456

for file in files:
    sample = file.split('.')[0]
    highit_refs = set()
    with open(os.path.join('vsearch6', file), 'r') as f:
        lines = [l.strip().split('\t') for l in f.readlines()]
    for line in lines:
        start = int(line[2])
        end = int(line[3])
        ref = line[0].replace('-REV', '')
        if start <= 8 and end >=72:
            highit_refs.add(ref)
    highits = len(highit_refs)
    print(f'\n{sample} vsearch6: {highits} ({round(100*highits/NUM_REFS , 2)}%)')

# files = os.listdir('/home/mkk/Projects/MaverickQC/bwa_aln_primary_mapped')
#
# for file in files:
#     sample = file.split('.')[0]
#     with open(os.path.join('bwa_aln_primary_mapped', file), 'r') as f:
#         lines = [l.strip().split('\t') for l in f.readlines()]