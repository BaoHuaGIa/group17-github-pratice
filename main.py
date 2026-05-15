from student import Student, StudentManager
from utils import search_student


def show_menu():
    print("\n===== HE THONG QUAN LY SINH VIEN =====")
    print("1. Them sinh vien")
    print("2. Hien thi danh sach sinh vien")
    print("3. Tim kiem sinh vien theo ma so")
    print("0. Thoat")


def input_student():
    print("\n--- Them sinh vien moi ---")
    student_id = input("Nhap ma sinh vien: ").strip()
    name = input("Nhap ho ten sinh vien: ").strip()
    major = input("Nhap chuyen nganh: ").strip()

    return Student(student_id, name, major)


def handle_add_student(manager):
    student = input_student()
    manager.add_student(student)
    print("=> Them sinh vien thanh cong.")


def handle_display_students(manager):
    print("\n--- Danh sach sinh vien ---")
    manager.display_students()


def handle_search_student(manager):
    print("\n--- Tim kiem sinh vien ---")
    student_id = input("Nhap ma sinh vien can tim: ").strip()

    student = search_student(manager, student_id)

    if student is None:
        print("=> Khong tim thay sinh vien.")
    else:
        print("=> Tim thay sinh vien:")
        print(student)


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Nhap lua chon cua ban: ")

        if choice == "1":
            handle_add_student(manager)
        elif choice == "2":
            handle_display_students(manager)
        elif choice == "3":
            handle_search_student(manager)
        elif choice == "0":
            print("Thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le. Vui long nhap lai.")


if __name__ == "__main__":
    main()