import tkinter as tk
from tkinter import messagebox
import pickle


window = tk.Tk()
window.geometry("800x1200")
window.title("학생 수강 정보 관리 시스템")

names = []  # 학생의 이름
numbers = ['1']  # 학생의 학번
phones = []  # 학생의 핸드폰 번호
course=["프로그래밍 입문","크리에이티브디자인","AI응용수학","DU실용영어","AI융합비전설계","나의대학생활과진로","컴퓨팅사과와코딩","DU사랑빛자유프로젝트"]  # 학생의 수강정보
passwords = ['1']
selected_course = []
students = {}
filename = r"C:\Users\hawns\OneDrive\문서\GitHub\grdae-system\student.txt"
course_timetable = {
  '프로그래밍 입문': ['월요일10:00', '수요일 10:00'],
  '사랑빛자유프로젝트': ['화요일 10:00'],
  'ai응용수학': ['월요일 13:30','수요일 3:00'],
  '크리에이티브디자인':['화요일 13:30','목요일 15:00' ],
  'Du실용영어':['화요일 16:00','목요일 12:00'],
  'Ai융합비전설계':['목요일 11:00'],
  '나의대학생활과진로':['목요일 10:00'],
}


entry_name = None  # entry_name 변수 초기화
entry_number = None  # entry_number 변수 초기화
entry_phone = None  # entry_phone 변수 초기화
entry_password = None  # entry_password 변수 초기화
entry_number1 = None

def update_timetable():#학생시간표
    global timetable_labels

    for i, course_name in enumerate(course_timetable):
        matched_timeslots = course_timetable.get(course_name, [])
        for time_slot in matched_timeslots:
            day_str, time_str = time_slot.split('요일')
            day = ['월', '화', '수', '목', '금', '토', '일'].index(day_str)
            hour = int(time_str[:2])
            row = hour -9
            cell_label = timetable_labels[row][day]
            if course_name in selected_course:
                cell_label.config(text=course_name, bg="lightblue")
            else:
                cell_label.config(text="", bg="white")


    update_timetable()

def student_system():#학생관리시스템
    if button1 is not None:
        button1.pack_forget()
    if button2 is not None:
        button2.pack_forget()
    if button3 is not None:
        button3.pack_forget()
    button1_1.pack(side=tk.TOP)
    button1_2.pack(side=tk.TOP)
    button1_3.pack(side=tk.TOP)
    button_return.pack_forget()
    student_listbox.pack_forget()
    delete_button.pack_forget()

def add_student():#학생추가
    if button1 is not None:
        button1.pack_forget()
    if button2 is not None:
        button2.pack_forget()
    delete_menu()
    global entry_name, entry_number, entry_phone, label_name, student_number, phone_number, entry_password, password
    label_name = tk.Label(text="이름:")
    label_name.pack()
    entry_name = tk.Entry()
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
    entry_password = tk.Entry()
    entry_password.pack()
    answer_button.configure(command=lambda: save(entry_name.get(), entry_number.get(), entry_phone.get(),entry_password.get()))
    answer_button.pack()
    button_return.pack()
    if button1_4 is not None:
        button1_4.pack()

def save(name,number,phone,password):#학생추가에서 확인버튼이 눌렸을경우
        name = entry_name.get()
        number = entry_number.get()
        phone = entry_phone.get()
        password = entry_password.get()

        if not (name and number and phone and password):
            # Display a warning message if any information is missing
            messagebox.showwarning("필수 입력", "모든 정보를 입력하세요.")
            return

        if number in students:
            # Display a warning message if the student number is already in the dictionary
            messagebox.showwarning("학번 중복", "이미 등록된 학번입니다.")
            return

        students[number] = {
            '이름': name,
            '비밀번호': password,
            '전화번호': phone,
            '학번': number
        }

        with open('student.txt', 'w') as file:
            for student_number, student_data in students.items():
                name = student_data['이름']
                student_number = student_data['학번']
                phone_number = student_data['전화번호']
                password = student_data['비밀번호']

                line = f"{name},{student_number},{phone_number},{password}\n"
                file.write(line)

        entry_name.delete(0, 'end')
        entry_number.delete(0, 'end')
        entry_phone.delete(0, 'end')
        entry_password.delete(0, 'end')

        messagebox.showinfo("학생 정보 저장 성공", "학생 정보를 성공적으로 저장하였습니다.")

        answer_button.config(command=save)
       

def course_system():#수강관리시스템
    delete_menu()
    button2_1.pack()
    button2_2.pack()
    button1_4.pack()
    button1_5.pack()
    delete_labels.pack()
    

def delete_labels():#학생삭제
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.pack_forget()
            button_return.pack_forget()
            
def show_course_info():#수강관리시스템에서 수강과목확인
    delete_menu()
    label = tk.Label(text="수강 정보")
    label.pack()
    global selected_course
    selected_course = load_courses()

    for course_name in selected_course:
        course_label = tk.Label(text=course_name)
        course_label.pack()


    button_return = tk.Button(text="이전", command=course_system)
    button_return.pack(side=tk.BOTTOM)

def save_courses():#수강관리시스템에서 수강신청메뉴로들어가서 저장하는 코드
    with open("courses.pickle", "wb") as f:
        pickle.dump(selected_course, f)


def load_courses():#저장되어있는 코드를 불러오는 코드
    try:
        with open("courses.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


def course_course():#체크박스를 생성하는 코드
    delete_menu()
    global checkbox
    checkboxes=[]
    def hide_checkboxes():
        for cb in checkboxes:
            cb.pack_forget()
            course_system()
            button_return2.pack_forget()

    for i, course_name in enumerate(course):
        checkbox = tk.Checkbutton(text=course_name, command=lambda idx=i: select_course(idx))
        checkbox.pack()
        checkboxes.append(checkbox)
    button_return2.config(command=hide_checkboxes)
    button_return2.pack(side=tk.BOTTOM)
    


def select_course(idx):#체크박스가 체크되어있을때 저장하는 코드
    course_name = list(course_timetable.keys())[idx]
    if course_name not in selected_course:
        selected_course.append(course_name)
    else:
        selected_course.remove(course_name)


    

def back_main_menu():#메인메뉴로 돌아가는코드
    if button1 is not None:
        button1.pack()
    delete_menu()

def deleted1_student():
    delete_menu()
    update_student_list()
    student_listbox.pack()
    student_listbox.delete(0,tk.END)
    with open('student.txt', 'r') as file:
        lines=file.readlines()
    for line in lines:
        line = line.strip()
        name,number,phone = line.split(',')[0:3]
        info = f"Name: {name}, Number: {number}, Phone: {phone}"
        student_listbox.insert(tk.END, info)

    selected_indices = student_listbox.curselection()
    if selected_indices:
        with open('student.txt','r') as file:
            lines=file.readlines()
            
        with open('student.txt','w') as file:
             for index, line in enumerate(lines):
                    if index not in selected_indices:
                        file.write(line)
            
        names.clear()
        numbers.clear()
        phones.clear()

        with open('student.txt', 'r') as file:
            for line in file:
                name, number, phone = line.strip().split(',')
                names.append(name)
                numbers.append(number)
                phones.append(phone)
                
        for i in range(len(names)):
            info = f"Name: {names[i]}, Number: {numbers[i]}, Phone: {phones[i]}"
            student_listbox.insert(tk.END, info)
    button_return.pack()

    
def delete_menu():#모든메뉴를 삭제하는 코드
   for widget in window.winfo_children():
        if isinstance(widget, (tk.Entry, tk.Button, tk.Label)):
            widget.pack_forget()
        



def update_student_list():#학생삭제에서 업데이트 하는 메뉴
    student_listbox.delete(0, tk.END)

    for name, number, phone in zip(names, numbers, phones):
        info = f"Name: {name}, Number: {number}, Phone: {phone}"
        student_listbox.insert(tk.END, info) 

def login():#로그인코드
    global entry_number1,entry_password1,student_number1,password1
    student_number1 = tk.Label(text="학번:")
    student_number1.pack()
    entry_number1 = tk.Entry()
    entry_number1.pack()
    password1 = tk.Label(text="비밀번호")
    password1.pack()
    entry_password1=tk.Entry()
    entry_password1.pack()
    answer_button.configure(command=lambda: login_collect((entry_number1.get()),entry_password1.get()))
    answer_button.pack()
    button_return.pack()
        
    def login_collect(number,password):
        with open("student.txt", "r") as file:
            for line in file:
                line = line.strip()
                stored_student_number, stored_password = line.split(",")[1:3]
                
                if number == stored_student_number and password == stored_password:
                    messagebox.showinfo("로그인 성공","로그인에 성공하셨습니다")
                    student_number1.pack_forget()
                    entry_number1.pack_forget()
                    entry_password1.pack_forget()
                    password1.pack_forget()
                    button_return.pack()
                    delete_menu()
                    course_system()
                    return
        
                else:
                    entry_number1.delete(0,tk.END)
                    entry_password1.delete(0,tk.END)
                    messagebox.showinfo("로그인 실패","로그인에 ")

def grade_system_():
    if button1 is not None:
        button1.pack_forget()
    if button2 is not None:
        button2.pack_forget()
    if button3 is not None:
        button3.pack_forget()
    button3_1.pack(side=tk.TOP)
    button3_2.pack(side=tk.TOP)
    button3_3.pack(side=tk.TOP)
    button3_4.pack(side=tk.TOP)
    button3_5.pack(side=tk.TOP)
    button_return.pack_forget()
    student_listbox.pack_forget()
    delete_button.pack_forget()
    delete_entry()

    
def save_grades():
    grades = {}
    for course, entry in grades_entries.items():
        grade = entry.get()
        grades[course] = grade

course_list = ["프로그래밍 입문", "크리에이티브디자인", "AI응용수학", "DU실용영어", "AI융합비전설계", "나의대학생활과진로", "컴퓨팅사과와코딩", "DU사랑빛자유프로젝트"]

def grade_input():  
    for course in course_list:
    entry_label = tk.Label(window, text=course)
    entry_label.pack()
    entry = tk.Entry(window)
    entry.pack()
    grades_entries[course] = entry
    submit_button = tk.Button(window, text="저장", command=save_grades)
    submit_button.pack()




    
main_menu_frame = tk.Frame(window)
main_menu_frame.pack()
    
main_frame = tk.Frame(window)
main_frame.pack()

student_system_frame=tk.Frame(window)
student_system_frame.pack()

grade_system_frame=tk.Frame(window)
grade_system_frame.pack()




button1=tk.Button(window,text="학생관리시스템",command=student_system)
button1.pack()

button2=tk.Button(window,text="수강정보시스템",command=course_system)
button2.pack_forget()

button3=tk.Button(window,text="성적정보확인시스템",command=grade_system)
button3.pack_forget()

button1_1=tk.Button(window,text="학생추가",command=add_student)
button1_1.pack_forget()

button1_2=tk.Button(window,text="학생삭제",command=deleted1_student)
button1_2.pack_forget()

button1_3=tk.Button(window,text="학생확인",command=grade_system)
button1_3.pack_forget()

button1_4=tk.Button(text="메인메뉴로 돌아가기",command=back_main_menu)
button1_4.pack_forget()

button1_5=tk.Button(text="수강정보추가",command=course_course)
button1_5.pack_forget()

button2_1=tk.Button(text="수강정보확인",command=show_course_info)
button2_1.pack_forget()

button2_2=tk.Button(text="수강시간확인",command=update_timetable)
button2_2.pack_forget()

button2_3=tk.Button(text="수강정보")
button2_3.pack_forget()

button3=tk.Button(window,text="성적정보관리기능",command=grade_system)
button3.pack()

timetable_frame = tk.Frame(window)
timetable_frame.pack(padx=10, pady=10)
timetable_frame.pack_forget()

timetable_labels = [[tk.Label(timetable_frame, width=10, height=2, relief="solid") for _ in range(7)] for _ in range(10)]
for i, row in enumerate(timetable_labels):
    for j, label in enumerate(row):
        label.grid(row=i, column=j)

button3_1=tk.Button(window,text="성적입력",command=grade_input)
button3_1.pack_forget()

button3_2=tk.Button(window,text="성적수정")
button3_2.pack_forget()

button3_3=tk.Button(window,text="성적조회")
button3_3.pack_forget()

button3_4=tk.Button(window,text="성적통계")
button3_4.pack_forget()

button_return2=tk.Button(text="이전",command=course_system)
button_return2.pack_forget()


answer_button=tk.Button(text="확인")
answer_button.pack_forget()

button_return=tk.Button(text="이전화면",command=student_system)
button_return.pack_forget()

student_listbox = tk.Listbox(width=80)
student_listbox.pack_forget()

course_listbox =tk.Listbox(width=80)
course_listbox.pack_forget()

course_listbox.pack_forget()

delete_button=tk.Button(text="삭제")
delete_button.pack_forget

window.mainloop()
