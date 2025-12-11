INFILE = '/home/mkk/Projects/MaverickQC/Ink005-262144-randomTags.txt'

outfile = INFILE.replace('.txt', '20MER.fasta')

with open(INFILE) as f:
    lines = [l.strip().split('\t') for l in f.readlines()]

print(f'Len of the 3prime index is {len('TCTCCCTATAGTGAGTCGTATTACAA')}')

with open(outfile, 'w') as f:
    for line in lines:
        f.write('>' + line[0] + '\n')
        f.write(line[1][-46:].upper() + '\n')

