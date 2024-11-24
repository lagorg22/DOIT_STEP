
class Student:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name: str = name
        self.roll_number: int = roll_number
        self.__grade: str = grade

    @property
    def grade(self):
       return self.__grade

    @grade.setter
    def grade(self, new_grade: str):
        self.__grade = new_grade

    def __str__(self):
        return f'Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}'

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'grade': self.grade
        }


