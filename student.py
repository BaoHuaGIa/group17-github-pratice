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

    def display_students(self):
        """Hiển thị tất cả sinh viên"""
        if not self.students:
            print("-> Danh sách đang trống.")
            return
        
        for index, student in enumerate(self.students, 1):
            print(f"{index}. {student}")
    def add_student(self, student):
        """Thêm sinh viên mới vào danh sách"""
        self.students.append(student)
