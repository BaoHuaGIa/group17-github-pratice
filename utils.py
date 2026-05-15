def search_student(manager, student_id):
    """Tìm kiếm sinh viên bằng ID trong StudentManager"""
    for student in manager.students:
        if student.student_id == student_id:
            return student
    return None
