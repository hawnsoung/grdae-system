import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("200x300")
window.title("학생 수강 정보 관리 시스템")

names = []     # 학생의 이름
numbers = ['1']  # 학생의 학번
phones = []    # 학생의 핸드폰 번호
course = ["프로그래밍 입문", "크리에이티브디자인", "ai응용수학", "실용영어"]  # 학생의 수강정보
passwords = ['1']
selected_course = []
students = {}
filename = r"C:\Users\Administrator\Desktop\박준현\student.txt"


def student_system():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button1_1.pack(side=tk.TOP)
    button1_2.pack(side=tk.TOP)
    button1_3.pack(side=tk.TOP)
    button1_4.pack(side=tk.TOP)
    button_return.pack_forget()
    student_listbox.pack_forget()
    delete_button.pack_forget()
    delete_entry()

    def course_system():
        delete_menu()
        button2_1.pack()
        button2_2.pack()
        button1_4.pack()
        button1_5.pack()

    def course_course():
        delete_menu()
        for i, course_name in enumerate(course):
            checkbox = tk.Checkbutton(text=course_name, command=lambda idx=i: select_course(idx))
            checkbox.pack()
        button_return2.pack(side=tk.BOTTOM)


def select_course(index):
    course_name = course[index]
    if course_name in selected_course:
        selected_course.remove(course_name)
        messagebox.showinfo("알림", f"{course_name}이(가) 선택 해제되었습니다.")
    else:
        selected_course.append(course_name)
        messagebox.showinfo("알림", f"{course_name}이(가) 선택되었습니다.")
