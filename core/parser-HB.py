import filepaths as FILES
import csv
from collections import OrderedDict
files = ["xaa","xab","xac","xad","xae","xaf","xag","xah","xai","xaj"]

total_count = {}
for f in files:
    with open(FILES.get_filepath("hashtags\\" + f + "-occurrences"), 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] in total_count:
                total_count[line[0]] += int(line[1])
            else:
                total_count[line[0]] = int(line[1])

ordered_counts = OrderedDict(sorted(total_count.items(), key=lambda t: -t[1]))
with open(FILES.get_filepath("hashtags\\nov-all-occurrences"), 'w') as csvfile:
    for o_c in ordered_counts.keys():
        if ordered_counts[o_c] > 100:
            print(o_c, str(ordered_counts[o_c]) + '\n')
        csvfile.write(o_c + ',' + str(ordered_counts[o_c]) + '\n')