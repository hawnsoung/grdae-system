import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("200x300")
window.title("학생 수강 정보 관리 시스템")

names = []  # 학생의 이름
numbers = []  # 학생의 학번
phones = []  # 학생의 핸드폰 번호
course = ["프로그래밍 입문", "크리에이티브디자인", "ai응용수학", "실용영어"]  # 학생의 수강정보
passwords = []
selected_courses = []
students = {}
filename = r"C:\Users\OWNER\Documents\GitHub\grdae-system\student.txt"


def student_system():
    main_menu_frame.pack_forget()
    grade_system_frame.pack_forget()
    course_system_frame.pack_forget()
    student_system_frame.pack()
    button_return.pack_forget()
    delete_menu()
    student_listbox.pack()
    delete_button.pack()
    button_return.pack()
    button_return.configure(command=lambda: return_to_main_menu())
    button1_4.pack(side=tk.BOTTOM)


def course_system():
    main_menu_frame.pack_forget()
    grade_system_frame.pack_forget()
    student_system_frame.pack_forget()
    course_system_frame.pack()
    button_return.pack()
    button_return.configure(command=lambda: return_to_main_menu())
    delete_menu()
    course_listbox.pack()
    select_button = tk.Button(text="수강 과목 선택", command=slected_courses)
    select_button.pack()


def grade_system():
    main_menu_frame.pack_forget()
    course_system_frame.pack_forget()
    student_system_frame.pack_forget()
    grade_system_frame.pack()
    button_return.pack()
    button_return.configure(command=lambda: return_to_main_menu())
    delete_menu()
    grade_listbox.pack()


def return_to_main_menu():
    student_system_frame.pack_forget()
    grade_system_frame.pack_forget()
    course_system_frame.pack_forget()
    main_menu_frame.pack()


def slected_courses():
    selected_indices = course_listbox.curselection()
    if selected_indices:
        selected_courses.clear()
        for index in selected_indices:
            selected_courses.append(course[index])
        messagebox.showinfo("선택한 과목", ", ".join(selected_courses))


def delete_student():
    selected_indices = student_listbox.curselection()
    if selected_indices:
        for index in selected_indices:
            del names[index]
            del numbers[index]
            del phones[index]
        update_student_listbox()


def delete_menu():
    delete_button.pack_forget()
    delete_entry()
    student_listbox.pack_forget()
    grade_listbox.pack_forget()
    course_listbox.pack_forget()


def delete_entry():
    label_name.pack_forget()
    entry_name.pack_forget()
    student_number.pack_forget()
    entry_number.pack_forget()
    phone_number.pack_forget()
    entry_phone.pack_forget()
    password.pack_forget()
    entry_password.pack_forget()
    entry_name.delete(0, tk.END)
    entry_number.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_password.delete(0, tk.END)


def update_student_listbox():
    student_listbox.delete(0, tk.END)
    for name, number, phone in zip(names, numbers, phones):
        info = f"이름: {name}, 학번: {number}, 전화번호: {phone}"
        student_listbox.insert(tk.END, info)


def save(name, number, phone, password):
    names.append(name)
    numbers.append(number)
    phones.append(phone)
    passwords.append(password)
    update_student_listbox()


def login():
    number = entry_number1.get()
    password = entry_password1.get()
    if number in numbers:
        index = numbers.index(number)
        if passwords[index] == password:
            messagebox.showinfo("로그인", "로그인 성공!")
            entry_number1.delete(0, tk.END)
            entry_password1.delete(0, tk.END)
            delete_menu()
            course_system()
        else:
            messagebox.showerror("로그인 오류", "잘못된 비밀번호입니다.")
    else:
        messagebox.showerror("로그인 오류", "학번을 찾을 수 없습니다.")
def add_student():
    button1.pack_forget()
    button2.pack_forget()
    delete_menu()
    global entry_name, entry_number, entry_phone,label_name,student_number,phone_number,entry_password,password
    label_name = tk.Label(text="이름:")
    label_name.pack()
    entry_name= tk.Entry()
    entry_name.pack()
    student_number = tk.Label(text="학번:")
    student_number.pack()
    entry_number = tk.Entry()
    entry_number.pack()
    phone_number = tk.Label(text="전화번호:")
    phone_number.pack()
    entry_phone = tk.Entry()
    entry_phone.pack()
    password = tk.Label(text="비밀번호")
    password.pack()
    entry_password=tk.Entry()
    entry_password.pack()
    answer_button.configure(command=lambda: save(entry_name.get(),entry_number.get(),entry_phone.get(),entry_password.get()))
    answer_button.pack()
    button_return.pack()
    button1_4.pack()


# Main Menu
main_menu_frame = tk.Frame(window)
main_menu_frame.pack()

button1 = tk.Button(main_menu_frame, text="학생 관리", command=student_system)
button1.pack()

button2 = tk.Button(main_menu_frame, text="성적 확인", command=grade_system)
button2.pack()

button3 = tk.Button(main_menu_frame, text="수강 과목 관리", command=course_system)
button3.pack()

# Student System Frame
student_system_frame = tk.Frame(window)

button1_1 = tk.Button(student_system_frame, text="학생 추가", command=add_student)
button1_1.pack(side=tk.TOP)

button1_2 = tk.Button(student_system_frame, text="학생 삭제", command=delete_student)
button1_2.pack(side=tk.TOP)




student_listbox = tk.Listbox(student_system_frame)
delete_button = tk.Button(student_system_frame, text="삭제", command=delete_student)
button_return = tk.Button(student_system_frame, text="돌아가기", command=return_to_main_menu)

# Course System Frame
course_system_frame = tk.Frame(window)
course_listbox = tk.Listbox(course_system_frame)

# Grade System Frame
grade_system_frame = tk.Frame(window)
grade_listbox = tk.Listbox(grade_system_frame)

# Login Frame
login_frame = tk.Frame(window)

student_number1 = tk.Label(login_frame, text="학번:")
student_number1.pack()
entry_number1 = tk.Entry(login_frame)
entry_number1.pack()

password1 = tk.Label(login_frame, text="비밀번호:")
password1.pack()
entry_password1 = tk.Entry(login_frame, show="*")
entry_password1.pack()

answer_button = tk.Button(login_frame, text="로그인", command=login)

main_menu_frame.pack()

window.mainloop()
