import tkinter as tk

window = tk.Tk()

window.title("Student Management System")
names=[]    #학생의 이름
numbers=[]  #학생의 학번
phones=[]   #학생의 핸드폰 번호
passwords = []   # 학생의 비밀번호
course=["프로그래밍 입문","크리에이티브디자인","AI응용수학","DU실용영어","AI융합비전설계","나의대학생활과진로","컴퓨팅사과와코딩","DU사랑빛자유프로젝트"]  #학생의 수강정보
selected_course=[]
grades = {}
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
                    user_input=input("삭제할 번호를 입력하세요 (n을 입력하면 뒤로 돌아갑니다): ")
                    if user_input == 'n':
                        break
                    try:
                        user_input = int(user_input)
                    except ValueError:
                        print("올바른 번호를 입력하세요.")
                        continue
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
                break
                        
    elif user_input == 2:  # 메인메뉴에서 2번이 선택될 경우
        while True:
            print("""=================
            1. 수강과목 등록
            2. 수강과목 삭제
            3. 메인메뉴로 돌아가기
            =========================""")
            user_input = int(input("원하는 기능을 선택하세요: "))

            if user_input == 1:  # 수강과목 등록
                while True:
                    print("학생이 수강하고 있는 과목을 선택하세요")
                    for i in range(len(course)):
                        print("No. " + str(i + 1) + ", " + course[i])
                    try:
                        selected_subject_index = int(input("원하는 과목 번호를 선택하세요: "))
                        if selected_subject_index < 1 or selected_subject_index > len(course):
                            print("잘못된 입력입니다.")
                        else:
                            selected_course.append(course[selected_subject_index - 1])
                            choice = input("과목 선택이 완료되었습니까? (y/n): ")
                            if choice.lower() == "y":
                                print("학생의 수강정보 입력이 완료되었습니다.")
                                break
                    except ValueError:
                        print("잘못된 입력입니다.")

            elif user_input == 2:  # 수강과목 삭제
                if len(selected_course) == 0:
                    print("수강 중인 과목이 없습니다.")
                else:
                    print("수강 중인 과목:")
                    for i, subject in enumerate(selected_course, 1):
                        print(f"{i}. {subject}")
                    try:
                        selected_subject_index = int(input("삭제할 과목 번호를 선택하세요: "))
                        if selected_subject_index < 1 or selected_subject_index > len(selected_course):
                            print("잘못된 입력입니다.")
                        else:
                            deleted_subject = selected_course.pop(selected_subject_index - 1)
                            print(f"{deleted_subject} 과목이 삭제되었습니다.")
                    except ValueError:
                        print("잘못된 입력입니다.")

            elif user_input == 3:  # 메인메뉴로 돌아가기
                break
            
    elif user_input == 3:   # 메인메뉴에서 3번이 선택될 경우
        while True:
            print("""=============
                  1. 성적입력
                  2. 성적수정
                  3. 성적조회
                  4. 성적통계
                  5. 메인메뉴로 돌아가기
                =============""")
            
            user_input = int(input("원하는 기능을 선택하세요: "))
            
            if user_input == 1:
                def enter_grades():
                    numbers = input("학생의 학번을 입력하세요: ")
                    print("수강 가능한 과목:")
                    for i, subject in enumerate(course, 1):
                        print(f"{i}. {subject}")
                    subject_index = int(input("성적을 입력할 과목의 번호를 선택하세요: ")) - 1
                    selected_subject = course[subject_index]
                    grade = input("성적을 입력하세요: ")
                
                    if numbers in grades:
                        grades[numbers][selected_subject] = grade
                    else:
                        grades[numbers] = {selected_subject: grade}

                    print("성적이 입력되었습니다.")

                enter_grades()

            elif user_input == 2:
                def modify_grades():
                    numbers = input("학생의 학번을 입력하세요: ")
                    course = input("과목명을 입력하세요: ")

                    if numbers in grades and course in grades[numbers]:
                        new_grade = input("수정할 성적을 입력하세요: ")
                        grades[numbers][course] = new_grade
                        print("성적이 수정되었습니다.")
                    else:
                        print("입력한 학생의 성적 정보가 존재하지 않습니다.")

                modify_grades()

            elif user_input == 3:
                def view_grades():
                    numbers = input("성적을 조회할 학생의 학번을 입력하세요: ")

                    if numbers in grades:
                        for course, grade in grades[numbers].items():
                            print(f"과목: {course}, 성적: {grade}")
                    else:
                        print("입력한 학번의 학생의 성적 정보가 존재하지 않습니다.")

                view_grades()

            elif user_input == 4:
                def calculate_statistics():
                    print("수강 가능한 과목:")
                    for i, subject in enumerate(course, 1):
                        print(f"{i}. {subject}")
                    subject_index = int(input("성적 통계를 조회할 과목의 번호를 선택하세요: ")) - 1
                    selected_subject = course[subject_index]

                    if selected_subject in course:
                        grades_for_course = [float(grade) for student_grades in grades.values() if selected_subject in student_grades for grade in student_grades.values() if grade.isdigit()]
                        if grades_for_course:
                            average = sum(grades_for_course) / len(grades_for_course)
                            maximum = max(grades_for_course)
                            minimum = min(grades_for_course)
                             
                            print(f"{selected_subject} 과목의 성적 통계:")
                            print(f"평균: {average}, 최고점: {maximum}, 최저점: {minimum}")
                          
                        else:
                            print(f"{selected_subject} 과목의 성적 정보가 존재하지 않습니다.")
                    else:
                        print(f"{selected_subject} 과목은 존재하지 않습니다.")

                calculate_statistics()

            elif user_input == 5:  # 성적정보 관리기능에서 5번이 선택될 경우
                break  # 메인메뉴로 돌아가기

    elif user_input == 4:   # 메인메뉴에서 4번이 선택될 경우
        print("""=============
        1. 공지사항 등록
        2. 공지사항 조회
        3. 공지사항 삭제
        4. 메인메뉴로 돌아가기
        =============""")
        user_input = int(input("원하는 기능을 선택하세요: "))

        if user_input == 1:  # 공지사항 등록
            notice = input("등록할 공지사항을 입력하세요: ")
            print("공지사항이 등록되었습니다.")

        elif user_input == 2:  # 공지사항 조회
            if not notice:
                print("등록된 공지사항이 없습니다.")
            else:
                print("등록된 공지사항:")
                print(notice)

        elif user_input == 3:  # 공지사항 삭제
            notice = ""
            print("공지사항이 삭제되었습니다.")

        elif user_input == 4:  # 메인메뉴로 돌아가기
            continue

    elif user_input == 5:   # 메인메뉴에서 5번이 선택될 경우
        print("프로그램을 종료합니다.")
        break

window.mainloop()