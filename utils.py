from student import students_list

def search_student(student_id):
    for s in students_list:
        if s['id'] == student_id:
            return s
    return None
