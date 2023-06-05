import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("200x300")
window.title("학생 수강 정보 관리 시스템")

names = []  # 학생의 이름
numbers = ['1']  # 학생의 학번
phones = []  # 학생의 핸드폰 번호
course = ["프로그래밍 입문", "크리에이티브디자인", "ai응용수학", "실용영어"]  # 학생의 수강정보
passwords = ['1']
selected_course = []
students = {}
filename = r"C:\Users\hawns\OneDrive\문서\GitHub\grdae-system\student.txt"

entry_name = None  # entry_name 변수 초기화
entry_number = None  # entry_number 변수 초기화
entry_phone = None  # entry_phone 변수 초기화
entry_password = None  # entry_password 변수 초기화
entry_number1 = None


def student_system():
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
    delete_entry()
def add_student():
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
def save(name,number,phone,password):
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
       

def course_system():
    delete_menu()
    button2_1.pack()
    button2_2.pack()
    button1_4.pack()
    button1_5.pack()

def hide_checkboxes():
    for cb in checkboxes:
        cb.pack_forget()

def course_course():
    delete_menu()
    global checkbox
    checkboxes=[]
    def hide_checkboxes():
        for cb in checkboxes:
            cb.pack_forget()
            course_system()

    for i, course_name in enumerate(course):
        checkbox = tk.Checkbutton(text=course_name, command=lambda idx=i: select_course(idx))
        checkbox.pack()
        checkboxes.append(checkbox)
    button_return2.config(command=hide_checkboxes)
    button_return2.pack(side=tk.BOTTOM)


def select_course(index):
    course_name = course[index]
    if course_name in selected_course:
        selected_course.remove(course_name)
        messagebox.showinfo("알림", f"{course_name}이(가) 선택 해제되었습니다.")
    else:
        selected_course.append(course_name)
        messagebox.showinfo("알림", f"{course_name}이(가) 선택되었습니다.")


def back_main_menu():
    if button1 is not None:
        button1.pack()
    delete_menu()









def slected_courses():
    delete_menu()
    course_listbox.pack()
    course_listbox.delete(0, tk.END)
    selected_indices = course_listbox.curselection()
    if selected_indices:
        for i in course:
            info=f"수강과목:", course[i]
            course_listbox.insert(tk.END, info)

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

    
def delete_menu():
    button1_1.pack_forget()
    button1_2.pack_forget()
    button1_3.pack_forget()
    button1_4.pack_forget()
    button2_1.pack_forget()
    button2_2.pack_forget()
    button2_3.pack_forget()
    button1_5.pack_forget()
    student_listbox.pack_forget()
    delete_button.pack_forget()
    button_return.pack_forget()
    answer_button.pack_forget()   

def delete_entry():
        global entry_name
        entry_name.pack_forget()
        entry_number.pack_forget()
        entry_phone.pack_forget()
        label_name.pack_forget()
        student_number.pack_forget()
        phone_number.pack_forget()
        password.pack_forget()
        entry_password.pack_forget()
        answer_button.pack_forget()
        entry_name.delete(0,tk.END)
        entry_number.delete(0,tk.END)
        entry_phone.delete(0,tk.END)
        entry_password.delete(0,tk.END)
        entry_number1.pack_forget()
        entry_password1.pack_forget()
        student_number1.pack_forget()
        password1.pack_forget()
        



def update_student_list():
    student_listbox.delete(0, tk.END)

    for name, number, phone in zip(names, numbers, phones):
        info = f"Name: {name}, Number: {number}, Phone: {phone}"
        student_listbox.insert(tk.END, info) 

def login():
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

def grade_system():
    delete_menu()
    login()

    


   
        


    
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

button2_1=tk.Button(text="수강정보확인")
button2_1.pack_forget()

button2_2=tk.Button(text="수강시간확인")
button2_2.pack_forget()

button2_3=tk.Button(text="수강정보")
button2_3.pack_forget()

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
