import pickle
import statistics

with open('/home/mkk/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers') as f:
	lines = [l.strip() for l in f]

end_divider = '\x1b[00m'
start_divider = '\x1b[01;31m'
end_divider_length = len('\x1b[00m')
start_divider_length = len('\x1b[01;31m')
read_lengths = []
i = 0
umi_dict = dict()

with open('/home/mkk/Projects/MaverickQC/MX_260102/seqs_with_2_near_perfect_fwd_primers.extracted.fasta', 'w') as f:
	for line in lines:
		if line.index('\x1b[01;31m') == 8:  # exclude too short and too long first umis
			first_umi = line[:8]
			end_of_3prime_primer = line.rfind('\x1b[00m')
			if len(line[end_of_3prime_primer:]) >= 8: # check if 2nd umi is not truncated
				second_umi = line[end_of_3prime_primer+end_divider_length : end_of_3prime_primer+end_divider_length+8]
				read = ''.join(''.join(line.split(start_divider)[1:]).split(end_divider)[:-1])
				read_lengths.append(len(read))
				f.write(f'>Read{i} {first_umi}-{second_umi}\n')
				f.write(read+'\n')
				i += 1
				if f'{first_umi}-{second_umi}' in umi_dict.keys():
					umi_dict[f'{first_umi}-{second_umi}'].append(read)
				else:
					umi_dict[f'{first_umi}-{second_umi}'] = [read]
			else:
				continue

with  open('/home/mkk/Projects/MaverickQC/MX_260102/umi_dict.pkl', 'wb') as f:
	pickle.dump(umi_dict, f)

umi_read_numbers = [len(umi_dict[k]) for k in umi_dict.keys()]
print(f'Avg read length: {sum(read_lengths)/len(read_lengths)}')
print(f'Median read length: {statistics.median(read_lengths)}')
print(f'Min read length: {min(read_lengths)}')
print(f'Max read length: {max(read_lengths)}')
print(f'Found {len(umi_dict.keys())} unique UMI combinations.')
print(f'Min number of reads per UMI combination: {min(umi_read_numbers)}')
print(f'Max number of reads per UMI combination: {max(umi_read_numbers)}')
print(f'Average number of reads per UMI combination: {statistics.mean(umi_read_numbers)}')