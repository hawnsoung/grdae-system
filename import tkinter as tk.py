import tkinter as tk

window = tk.Tk()
window.title("Student Management System")

names = []
numbers = []
phones = []
passwords = []
course = ["프로그래밍 입문", "크리에이티브디자인", "ai응용수학", "실용영어"]
selected_course = []
grades = {}

def add_student():
    name = name_entry.get()
    number = number_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()

    names.append(name)
    numbers.append(number)
    phones.append(phone)
    passwords.append(password)

    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def delete_student():
    selected_index = student_listbox.curselection()[0]
    del names[selected_index]
    del numbers[selected_index]
    del phones[selected_index]
    del passwords[selected_index]
    student_listbox.delete(selected_index)

def search_student():
    search_number = search_entry.get()
    password = password_entry.get()

    if search_number in numbers and passwords[numbers.index(search_number)] == password:
        index = numbers.index(search_number)
        result_label["text"] = f"이름: {names[index]}, 학번: {numbers[index]}, 전화번호: {phones[index]}, 수강정보: {course[index]}"
    else:
        result_label["text"] = "검색 결과가 없거나 비밀번호가 일치하지 않습니다."

def add_course():
    selected_index = course_listbox.curselection()[0]
    selected_course.append(course[selected_index])
    course_listbox.selection_clear(0, tk.END)

def delete_course():
    selected_index = selected_course_listbox.curselection()[0]
    selected_course.pop(selected_index)
    selected_course_listbox.delete(selected_index)

def enter_grades():
    student_number = grades_entry.get()
    selected_subject = selected_subject_var.get()
    grade = grade_entry.get()

    if student_number in grades:
        grades[student_number][selected_subject] = grade
    else:
        grades[student_number] = {selected_subject: grade}

    grades_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def modify_grades():
    student_number = grades_entry.get()
    selected_subject = selected_subject_var.get()
    new_grade = grade_entry.get()

    if student_number in grades and selected_subject in grades[student_number]:
        grades[student_number][selected_subject] = new_grade

    grades_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def view_grades():
    student_number = grades_entry.get()

    if student_number in grades:
        grade_text = ""
        for subject, grade in grades[student_number].items():
            grade_text += f"과목: {subject}, 성적: {grade}\n"
        result_label["text"] = grade_text
    else:
        result_label["text"] = "입력한 학번의 학생의 성적 정보가 존재하지 않습니다."

def calculate_statistics():
    selected_subject = selected_subject_var.get()

