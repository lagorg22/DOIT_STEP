import csv

with open('../titanic.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    with open('survivors.csv', 'a+') as res_f:
        writer = csv.writer(res_f, delimiter=',')
        writer.writerow(headers)
        for row in reader:
            if row[1] == '1':
                writer.writerow(row)
