from json import JSONDecodeError
from student import Student
import json

class Menu:
    def __init__(self):
        self.__students: dict[str, Student]= {}
        self.__read_db()

    def is_student_present(self, roll_number: str) -> bool:
        return roll_number in self.__students.keys()

    def change_grade(self, roll_number: int, grade: str):
        roll_number = str(roll_number)
        if self.is_student_present(roll_number):
            stud = self.__students[roll_number]
            stud.grade = grade
            self.__refresh_db()
        else:
            print(f'There is no student with roll number {roll_number}')

    def get_student_info(self, roll_number: int):
        roll_number = str(roll_number)
        if self.is_student_present(roll_number):
            print(self.__students[roll_number])
        else:
            print(f'There is no student with roll number {roll_number}')

    def display_all(self):
        for stud in self.__students.values():
            print(stud)

    def add_student(self, name: str, roll_number: int, grade: str):
        roll_number = str(roll_number)
        if self.is_student_present(roll_number):
            print(f'Student with roll number {roll_number} is already present.')
        else:
            stud = Student(name, int(roll_number), grade)
            self.__students[roll_number] = stud
            self.__store_in_db(stud)

    def __read_db(self):
        try:
            with open('db.json', "r") as file:
                data: dict[str, dict] = json.load(file)
                for roll_num, s in data.items():
                    self.__students[roll_num] = Student(s['name'], s['roll_number'], s['grade'])
        except (FileNotFoundError, JSONDecodeError):
            self.__students = {}

    def __store_in_db(self, stud: Student):
        new_data = {stud.roll_number: stud.to_dict()}
        try:
            with open('db.json', "r") as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            data = {}
        data.update(new_data)

        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)

    def __refresh_db(self):
        data = {roll_num: stud.to_dict() for roll_num, stud in self.__students.items()}
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)


