import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("성적정보 관리 프로그램")

# Define functions
def enter_grades():
    # Function code for entering grades
    pass

def modify_grades():
    # Function code for modifying grades
    pass

def view_grades():
    # Function code for viewing grades
    pass

def calculate_statistics():
    # Function code for calculating statistics
    pass

def main_menu():
    # Function code for the main menu
    menu_label = tk.Label(window, text="메인메뉴", font=("Helvetica", 16))
    menu_label.pack()

    options = [
        "성적입력",
        "성적수정",
        "성적조회",
        "성적통계",
        "메인메뉴로 돌아가기"
    ]

    for i, option in enumerate(options, 1):
        option_label = tk.Label(window, text=f"{i}. {option}")
        option_label.pack()

    # Function to handle the user's selection
    def handle_selection():
        selected_option = option_var.get()

        if selected_option == 1:
            enter_grades()
        elif selected_option == 2:
            modify_grades()
        elif selected_option == 3:
            view_grades()
        elif selected_option == 4:
            calculate_statistics()
        elif selected_option == 5:
            main_menu()  # Go back to the main menu

    option_var = tk.IntVar()
    option_var.set(1)  # Set the default option

    option_menu = tk.OptionMenu(window, option_var, *range(1, len(options) + 1))
    option_menu.pack()

    select_button = tk.Button(window, text="선택", command=handle_selection)
    select_button.pack()

# Function code for entering grades
def enter_grades():
    # Create a new window for entering grades
    grades_window = tk.Toplevel(window)
    grades_window.title("성적입력")
    pass

# Function code for modifying grades
def modify_grades():
    # Create a new window for modifying grades
    modify_window = tk.Toplevel(window)
    modify_window.title("성적수정")
    pass

# Function code for viewing grades
def view_grades():
    # Create a new window for viewing grades
    view_window = tk.Toplevel(window)
    view_window.title("성적조회")
    pass

# Function code for calculating statistics
def calculate_statistics():
    # Create a new window for calculating statistics
    stats_window = tk.Toplevel(window)
    stats_window.title("성적통계")
    pass

# Run the main menu
main_menu()

# Start the Tkinter event loop
window.mainloop()
