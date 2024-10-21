import csv

with open('../organizations-100.csv', 'r') as f:
    data = csv.DictReader(f)
    headers = list(data.fieldnames)
    not_wanted_fields = ['Index', 'Country', 'Description', 'Founded']
    headers = [val for val in headers if val not in not_wanted_fields]
    with open('ssl_companies.csv', 'w') as res_f:
        dict_writer = csv.DictWriter(res_f, fieldnames=headers)
        dict_writer.writeheader()
        for row in data:
           if row['Website'][4] == 's':
               trimmed_row = {key: val for key, val in row.items() if key not in not_wanted_fields}
               dict_writer.writerow(trimmed_row)


