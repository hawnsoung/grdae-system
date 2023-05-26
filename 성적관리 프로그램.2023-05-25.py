
import tkinter as tk

window = tk.Tk()
window.geometry("200x300")
window.title("학생 수강 정보 관리 시스템")

names=[]    #학생의 이름
numbers=['1'] #학생의 학번
phones=[]   #학생의 핸드폰 번호
course=["프로그래밍 입문","크리에이티브디자인","ai응용수학","실용영어"]#학생의 수강정보
passwords=['1']
slected_course=[]



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

def back_main_menu():
    button1.pack()
    button2.pack()
    button3.pack()
    delete_menu()

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
    selected_indices = student_listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            student_listbox.delete(index)
            names.pop(index)
            numbers.pop(index)
            phones.pop(index)

def delete_student():
    delete_menu()
    student_listbox.pack()
    student_listbox.delete(0, tk.END)
      
    for name,number,phone in zip(names,numbers,phones):
        info = f"Name: {name}, Number: {number}, Phone: {phone}"
        student_listbox.insert(tk.END, info)
    delete_button.pack()
    delete_button.configure(command=lambda:deleted1_student())
    button_return.pack()
    button_return.configure(command=lambda:student_system())
    
def delete_menu():
    button1_1.pack_forget()
    button1_2.pack_forget()
    button1_3.pack_forget()
    button1_4.pack_forget()
    button2_1.pack_forget()
    button2_2.pack_forget()
    student_listbox.pack_forget()
    delete_button.pack_forget()
    button_return.pack_forget()
    answer_button.pack_forget()
    

    
    

def delete_entry():
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
    
    
    

    

def save(name,number,phone,password):
    names.append(name)
    numbers.append(number)
    phones.append(phone)
    passwords.append(password)
    student_system()


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
    
def login_collect(number,password):
    if number in numbers and password in passwords:
        student_number1.pack_forget()
        entry_number1.pack_forget()
        entry_password1.pack_forget()
        password1.pack_forget()
        button_return.pack()
        delete_menu()
        course_system()
        
    else:
        print("잘못된 접근입니다")

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
button2.pack()

button3=tk.Button(window,text="성적정보확인시스템",command=grade_system)
button3.pack()

button1_1=tk.Button(window,text="학생추가",command=add_student)
button1_1.pack_forget()

button1_2=tk.Button(window,text="학생삭제",command=delete_student)
button1_2.pack_forget()

button1_3=tk.Button(window,text="학생확인",command=grade_system)
button1_3.pack_forget()

button1_4=tk.Button(text="메인메뉴로 돌아가기",command=back_main_menu)
button1_4.pack_forget()

button1_5=tk.Button(text="수강정보추가")
button1_5.pack_forget()

button2_1=tk.Button(text="수강정보확인")
button2_1.pack_forget()

button2_2=tk.Button(text="수강시간확인")
button2_2.pack_forget()


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
