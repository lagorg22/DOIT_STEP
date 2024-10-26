# დავალება 2.
# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და courses(კურსების სია, რომელშიც
# სტუდენტი არის ჩარიცხული). აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები. შექმენით რამდენიმე ობიექტი
# და დაარეგისტრირეთ სხვადასხვა კურსებზე.

class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.courses: list[str]= []

    def enroll(self, course: str) -> bool:
        if course in self.courses:
            print(f'Student {self.name} is already enrolled on course: {course}\n')
            return False
        else:
            self.courses.append(course)
            print(f'Congrats {self.name}, the course {course} is added successfully\n')
            return True

    def drop_course(self, course: str) -> bool:
        if course in self.courses:
            self.courses.remove(course)
            print(f'Not so congrats {self.name}, course {course} has been removed successfully\n')
            return True
        else:
            print(f'Student {self.name} is not enrolled on course {course}\n')
            return False

    def drop_out(self):
        self.courses.clear()
        print(f'Goodbye {self.name}, you have dropped all courses.\n')

    def show_courses(self):
        if not self.courses:
            print(f'Student {self.name} is not enrolled on any course.\n')
        else:
            print(f'Courses of Student {self.name}: {', '.join(self.courses)}\n')

lasha = Student('Lasha', '123')
lasha.enroll('Django')
lasha.enroll('Math')
lasha.enroll('Pandas')
lasha.enroll('Django')
lasha.enroll('NumPy')
lasha.enroll('English')
lasha.drop_course('English')
lasha.drop_course('jgsdkjgs')
lasha.show_courses()

alika = Student('Alika', '777')
alika.enroll('Georgian')
alika.enroll('Physics')
alika.enroll('Django')
alika.enroll('Dancing')
alika.show_courses()
alika.drop_out()
alika.show_courses()