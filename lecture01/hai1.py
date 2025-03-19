class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"ID: {self.student_id}번 / 이름: {self.name} / 나이: {self.age}살")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        new_student = Student(*student)
        self.students.append(new_student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

tester = StudentManager()
tester.add_student([1, "김철수", 20])
tester.add_student([2, "이영희", 21])
tester.add_student([3, "박지민", 19])

print("현재 등록된 학생 목록:")
tester.display_all_students()
print()

tester.add_student([4, "한지수", 22])
print("학번 4번 학생 추가 후:")
tester.display_all_students()
