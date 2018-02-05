import os
import csv

resource_files = os.listdir('Resources')

for f in resource_files:
    voter_ID = list()
    county=list()
    candidate=list()
    unique_candidates=list()
    unique_candidates_count=list()
    unique_candidates_perc=list()
    with open(os.path.join('Resources',f),'r') as data:
        csvdata = csv.reader(data)
        next(csvdata)
        for line in csvdata:
            voter_ID.append(line[0])
            county.append(line[1])
            candidate.append(line[2])
            if line[2] not in unique_candidates:
                unique_candidates.append(line[2])
    total_votes = len(voter_ID)
    for cands in unique_candidates:
        unique_candidates_count.append(candidate.count(cands))
        unique_candidates_perc.append(round(candidate.count(cands)/total_votes*100,2))
    winner = unique_candidates[unique_candidates_count.index(max(unique_candidates_count))]
    output_lines = list()
    output_lines.append('Poll Results for Election file: '+f+'\n')
    output_lines.append('---------------------------------------\n')
    output_lines.append('Total Votes Cast: '+str(total_votes)+'\n')
    output_lines.append('---------------------------------------\n')
    for x in range(len(unique_candidates)):
        output_lines.append(str(unique_candidates[x])+':  '+str(unique_candidates_perc[x])+'  ('+str(unique_candidates_count[x])+')\n')
    output_lines.append('---------------------------------------\n')
    output_lines.append('Winner:   '+str(winner)+'\n\n')
    for line in output_lines:
        print(line,end='')
    with open('output_'+f.split('.')[0]+'.txt','w') as output:
        output.writelines(output_lines)