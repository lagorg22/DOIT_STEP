import csv

with open('../organizations-100.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)



sorted_data = sorted(data, key=lambda row: row[-1])
sorted_data.pop()

with open('sorted_file.csv', 'w') as res_f:
    writer = csv.writer(res_f, delimiter=',')
    writer.writerow(header)
    writer.writerows(sorted_data)