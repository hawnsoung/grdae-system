import tkinter as tk

window = tk.Tk()

window.title("Student Management System")
names=[]    #학생의 이름
numbers=[]  #학생의 학번
phones=[]   #학생의 핸드폰 번호
passwords = []   # 학생의 비밀번호
course=["프로그래밍 입문","크리에이티브디자인","ai응용수학","실용영어"]#학생의 수강정보
slected_course=[]
while True: #메인메뉴
    print("""=============
      1.학생정보 관리기능
      2.수강정보 관리기능
      3.성적정보 관리기능
      4.기타기능
      5.종료
        =============""")
    user_input=int(input("원하는 기능을 선택하세요"))
    if user_input==1:   #메인메뉴에서 1번이 선택될경우
        while True:
            print("""=============
                  1.학생 추가
                  2.학생 삭제
                  3.학생 확인
                  4.메인메뉴로 돌아가기
                =============""")
            user_input=int(input("원하는 기능을 선택하세요"))
            if user_input==1:   #학생정보 관리기능에서 1번이 선택될경우("학생추가")
                name=input("학생의 이름을 입력하세요")
                number=input("학생의 학번을 입력하세요")
                phone=input("학생의 전화번호를 입력하세요")
                password = input("학생의 비밀번호를 입력하세요: ")
                names.append(name)
                numbers.append(number)
                phones.append(phone)
                passwords.append(password)
                        
            elif user_input==2: #학생정보 관리기능에서 2번이 선택될경우("학생삭제")
                while True:
                    if len(names)==0:
                        print("등록된 학생이 없습니다")
                        break
                    for i in range(len(names)):
                        print(i+1,"."," ",names[i],numbers[i],phones[i],course)
                    user_input=int(input("삭제할 번호를 입력하세요"))
                    user_input -= 1
                    if user_input in range(len(names)):
                       del names[user_input]
                       del numbers[user_input]
                       del phones[user_input]
                       del passwords[user_input]
                    if user_input==10:
                        break
            elif user_input == 3:  # 학생정보 관리기능에서 3번이 선택될 경우("학생확인")
                while True:
                    search_input = input("검색할 학생의 학번을 입력하세요: ")
                    if search_input in numbers:
                        password_input = input("비밀번호를 입력하세요: ")
                        for i in range(len(names)):
                            if search_input in [names[i], numbers[i], passwords[i], course[i]]:
                                print(f"이름: {names[i]}, 학번: {numbers[i]}, 전화번호: {phones[i]}, 수강정보: {course[i]}")
                                found = True
                        break    
                    else:
                        print("검색 결과가 없거나 비밀번호가 일치하지 않습니다.")
                        break
            
            elif user_input == 4:  # 학생정보 관리기능에서 4번이 선택될 경우
                while True: #메인메뉴
                    print("""=============
                    1.학생정보 관리기능
                    2.수강정보 관리기능
                    3.성적정보 관리기능
                    4.기타기능
                    5.종료
                        =============""")
                    user_input=int(input("원하는 기능을 선택하세요"))
                    break
                        
    if user_input==2:   #메인메뉴에서 2번이 선택될 경우
        while True:
            print("""=================
            1.수강과목 등록
            2.수강과목 삭제
            =========================""")
            user_input=int(input("원하는 기능을 선택하세요"))
            if user_input==1:
                while True:
                        print("학생이 수강하고 있는 과목을 선택하세요")
                        for i in range(len(course)):
                            print("No. " + str(i+1) + ", " + course[i])
                        try:    
                            user_input=int(input("원하는 과목 번호를 선택하세요"))
                            print("과목선택이 완료 되었습니까: y/n")
                        
                            if user_input<1 or user_input>len(course) :
                                    print("잘못된 입력입니다")
                            else:
                                slected_course.append(user_input)
                                choice=input(user_input)
                                if choice.lower()=="y":
                                    print("학생의 수강정보 입력이 완료 되었습니다.")
                                    break
                        except ValueError:
                            print("잘못된 입력입니다.")
            if user_input==2:
                
                  
    elif user_input==5:
        break   
        
        
    
