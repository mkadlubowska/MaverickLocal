import os

files = os.listdir('/home/mkk/Projects/MaverickQC/vsearch6')

NUM_REFS = 147456

for file in files:
    sample = file.split('.')[0]
    medhit_refs = set()
    with open(os.path.join('vsearch6', file), 'r') as f:
        lines = [l.strip().split('\t') for l in f.readlines()]
    for line in lines:
        start = int(line[2])
        end = int(line[3])
        ref = line[0].replace('-REV', '')
        if start <= 20 and end >=60:
            medhit_refs.add(ref)
    medhits = len(medhit_refs)
    print(f'\n{sample} vsearch6: {medhits} ({round(100*medhits/NUM_REFS , 2)}%)')

# files = os.listdir('/home/mkk/Projects/MaverickQC/bwa_aln_primary_mapped')
#
# for file in files:
#     sample = file.split('.')[0]
#     with open(os.path.join('bwa_aln_primary_mapped', file), 'r') as f:
#         lines = [l.strip().split('\t') for l in f.readlines()]