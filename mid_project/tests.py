from menu import Menu
from faker import Faker
import random

m = Menu()
f = Faker()
grades = ['A', 'B', 'C', 'D', 'E', 'F']

print('<========================Testing addition================================>')
for i in range(800):
    name = f.name() + ' ' + f.last_name()
    roll_number = i
    grade = random.choice(grades)
    m.add_student(name, roll_number, grade)

print('<========================Testing grade change================================>')
for _ in range(400):
    roll_number = random.randint(0, 400)
    grade = random.choice(grades)
    m.change_grade(roll_number, grade)

print('<========================Testing student removal================================>')
for _ in range(100):
    roll_number = random.randint(0, 400)
    m.remove_student(roll_number)



