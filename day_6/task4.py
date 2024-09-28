departments = {
    "HR": [
        {
             "first_name": "John",
             "last_name": "Doe",
             "age": 30,
             "salary": 50000
        },
        {
             "first_name": "Jane",
             "last_name": "Smith",
             "age": 25,
             "salary": 48000
        }
    ],
    "Engineering": [
        {
             "first_name": "Alice",
             "last_name": "Johnson",
             "age": 28,
             "salary": 75000
        },
        {
             "first_name": "Bob",
             "last_name": "Brown",
             "age": 35,
             "salary": 80000
         }
    ],
    "Marketing": [
        {
            "first_name": "Eve",
            "last_name": "White",
            "age": 32,
            "salary": 60000
         },
        {
            "first_name": "Tom",
             "last_name": "Green",
             "age": 29,
             "salary": 62000
        }
    ]
}
result = dict()
for department, employees in departments.items():
    curr_dep_avg = sum(employee['salary'] for employee in employees) / len(employees)
    result[department] = curr_dep_avg

print(result)
