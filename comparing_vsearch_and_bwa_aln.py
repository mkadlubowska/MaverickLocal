import statistics

vsearch_file = '/home/mkk/Projects/MaverickQC/vsearch6/JetSmth_252708_1_R1.vsearch.iddef2.id0.7.mincols6.tsv'
aln_file = '/home/mkk/Projects/MaverickQC/bwa_aln_primary_mapped/JetSmth_252708_1_R1.primary.mapped.sam'

vsearch_reads = set()
aln_reads = set()
vsearch_refs = set()
aln_refs = set()
vsearch_dict = dict()
aln_dict = dict()

with open(vsearch_file, 'r') as f:
    vsearch_lines = [l.strip().split('\t') for l in f]

with open(aln_file, 'r') as f:
    aln_lines = [l.strip().split('\t') for l in f]

with open('/home/mkk/Projects/MaverickQC/reads_fasta/JetSmth_252708_1_R1.reads') as f:
    lines = [l.strip('\n>').split('\t') for l in f]
    reads_dict = {l[0]: l[1] for l in lines}

for line in vsearch_lines:
    vsearch_refs.add(line[0])
    vsearch_reads.add(line[1])
    vsearch_dict[line[1]] = line[0]

for line in aln_lines:
    aln_reads.add(line[0])
    aln_refs.add(line[2])
    aln_dict[line[0]] = line[2]


print(f'Number of vsearch reads: {len(vsearch_reads):,}')
print(f'Number of aln reads: {len(aln_reads):,}')
print(f'Number of overlapping reads: {len(vsearch_reads.intersection(aln_reads)):,}')
print(f'Number of reads only in vsearch: {len(vsearch_reads - aln_reads):,}')
print(f'Number of reads only in aln: {len(aln_reads - vsearch_reads):,}')

matching_alignments = 0
unmatching_alignments = 0

for read, ref in aln_dict.items():
    if read in vsearch_dict.keys():
        if vsearch_dict[read] == aln_dict[read]:
            matching_alignments += 1
        else:
            unmatching_alignments += 1

print(f'Matching alignments: {matching_alignments:,} ({round( 100*matching_alignments/len(vsearch_reads.intersection(aln_reads)),2)}%)')
print(f'Non-matching alignments: {unmatching_alignments:,} ({round( 100*unmatching_alignments/len(vsearch_reads.intersection(aln_reads)),2)}%)')

overlapping_lengths = []
non_overlapping_lengths = []
for read in reads_dict.keys():
    if read in vsearch_reads.intersection(aln_reads):
        overlapping_lengths.append(len(reads_dict[read]))
    else:
        non_overlapping_lengths.append(len(reads_dict[read]))
print(f'Median len of reads aligned by both vsearch and bwa: {statistics.median(overlapping_lengths)}')
print(f'Median len of reads aligned by only one aligner: {statistics.median(non_overlapping_lengths)} ')