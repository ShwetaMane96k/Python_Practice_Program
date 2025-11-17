def student_marks():
    n = int(input("Enter number of students: "))
    students = {}
    for _ in range(n):
        name = input("Enter student name: ")
        marks = list(map(int, input(f"Enter marks of {name} (3 subjects, space-separated): ").split()))
        students[name] = marks

    avg_list = [sum(marks)/len(marks) for marks in students.values()]
    avg_dict = {name: sum(marks)/len(marks) for name, marks in students.items()}
    highest_tuple = tuple((name, max(marks)) for name, marks in students.items())

    print("\nAverage Marks List:", avg_list)
    print("Average Marks Dictionary:", avg_dict)
    print("Highest Marks Tuple:", highest_tuple)


def word_analysis():
    sentence = input("Enter a sentence: ")

    long_words = [word for word in sentence.split() if len(word) > 3]
    word_lengths = {word: len(word) for word in sentence.split()}
    unique_tuple = tuple(word.upper() for word in set(sentence.split()))

    print("\nLong Words List:", long_words)
    print("Word Lengths Dictionary:", word_lengths)
    print("Unique Uppercase Tuple:", unique_tuple)


def employee_bonus():
    n = int(input("Enter number of employees: "))
    employees = {}
    for _ in range(n):
        name = input("Enter employee name: ")
        salary = float(input(f"Enter salary of {name}: "))
        employees[name] = salary

    new_salaries = [sal * 1.1 if sal > 50000 else sal for sal in employees.values()]
    salary_dict = {name: (sal * 1.1 if sal > 50000 else sal) for name, sal in employees.items()}
    bonus_tuple = tuple((name, sal * 0.1) for name, sal in employees.items() if sal > 50000)

    print("\nNew Salaries List:", new_salaries)
    print("Salary Dictionary:", salary_dict)
    print("Bonus Tuple:", bonus_tuple)


# ---------------- MENU ----------------
while True:
    print("\n========= MENU =========")
    print("1. Student Marks Processing")
    print("2. Word Analysis in Sentence")
    print("3. Employee Salary Bonus")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        student_marks()
    elif choice == '2':
        word_analysis()
    elif choice == '3':
        employee_bonus()
    elif choice == '4':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")

