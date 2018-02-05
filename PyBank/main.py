import os
import csv

resource_files = os.listdir('Resources')

for f in resource_files:
    date = list()
    revenue = list()
    with open(os.path.join('Resources',f),'r') as data:
        csvdata = csv.reader(data)
        next(csvdata)
        for line in data:
            sp_line = str.split(line,',')
            date.append(sp_line[0])
            revenue.append(int(sp_line[1]))
    num_months = len(revenue)
    total_revenue = sum(revenue)
    revenue_intervals = list()
    for i in range(len(revenue)-1):
        revenue_intervals.append(revenue[i+1]-revenue[i])
    average_revenue_change = sum(revenue_intervals)/len(revenue_intervals)
    max_revenue_change = max(revenue_intervals)
    min_revenue_change = min(revenue_intervals)
    output_lines = list()
    output_lines.append('Financial Analysis for file: '+f+'\n')
    output_lines.append('--------------------------------------------------'+'\n')
    output_lines.append('Total Months: '+str(num_months)+'\n')
    output_lines.append('Total Revenue: '+str(total_revenue)+'\n')
    output_lines.append('Average Revenue Change: '+str(average_revenue_change)+'\n')
    output_lines.append('Greatest Increase in Revenue: '+str(date[revenue_intervals.index(max_revenue_change)+1])+' ('+str(max_revenue_change)+')'+'\n')
    output_lines.append('Greatest Decrease in Revenue: '+str(date[revenue_intervals.index(min_revenue_change)+1])+' ('+str(min_revenue_change)+')\n\n')
    for line in output_lines:
        print(line,end='')
    with open('output_'+f.split('.')[0]+'.txt','w') as output:
        output.writelines(output_lines)


