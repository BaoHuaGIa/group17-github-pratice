class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def __str__(self):
        return f"[{self.student_id}] {self.name} - Chuyên ngành: {self.major}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Thêm sinh viên mới vào danh sách"""
        self.students.append(student)