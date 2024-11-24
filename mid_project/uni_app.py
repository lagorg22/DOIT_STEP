from menu import Menu

class App:
    def __init__(self):
        self.menu = Menu()
        self.commands: dict = {
            'c': self.change_grade,
            'd': self.display_students,
            's': self.display_student,
            'a': self.add_student
        }

    def run(self):
        print('======================SchoolApp is running========================\n')
        print('Here are the commands for this application: \n'
              'close: "x"\n'
              'display students: "d"\n'
              'display student: "s" \n'
              'change grade: "c"\n'
              'add student: "a" \n')
        while True:
            command = input('Enter command: \n')
            if command == 'x':
                print('Process Ended.')
                break

            if command not in self.commands.keys():
                continue
            self.commands[command]()

    def __get_roll_num(self)->int:
        while True:
            try:
                roll_number = int(input('Enter the roll number: \n'))
                break
            except ValueError:
                print("Enter a valid integer.\n")
        return roll_number

    def __get_grade(self) -> str:
        while True:
            grade = input('Enter the new Grade: \n')
            if grade.upper() not in ['A', 'B', 'C', 'D', 'E', 'F']:
                print('Enter a valid grade.')
            else:
                break
        return grade.upper()

    def display_student(self):
        print('--------------------Displaying student--------------------\n')
        roll_number = self.__get_roll_num()
        self.menu.get_student_info(roll_number)

    def display_students(self):
        print('--------------------Displaying all students--------------------\n')
        self.menu.display_all()

    def change_grade(self):
        print('--------------------Changing grade of a student--------------------\n')
        roll_number =  self.__get_roll_num()
        grade = self.__get_grade()
        self.menu.change_grade(roll_number, grade)

    def add_student(self):
        print('--------------------Adding new student--------------------------\n')
        roll_number = self.__get_roll_num()
        grade = self.__get_grade()
        name = input('Enter student name: \n').title()
        self.menu.add_student(name, roll_number, grade)


