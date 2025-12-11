line_numbers = list(range(1,512*512+1,512)) # each line is represented by the first oligo in it
line_number_dict = {l: 0 for l in line_numbers}
with open('QC_251121/vsearch_trimmed_mincols86_id0.9_ref_with_cov_min_x1') as f:
    present_refs = [l.strip().split() for l in f.readlines()]

for r in present_refs:
    count = int(r[0])
    ref = int(r[1])
    for line in sorted(line_numbers, reverse=True):
        if line > ref:
            continue
        else:
            line_number_dict[line] += count
            break

missing_lines = []
for line in line_number_dict.keys():
    if line_number_dict[line] <128:
        missing_lines.append(line)

print(f'There are {len(missing_lines)} missing lines.')
print([int((i-1)/512) for i in missing_lines])
