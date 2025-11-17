def calculate_grade(marks):
    "Returns Grade Based On Marks"
    if marks>=90:
        return"A"
    elif marks>=75:
        return"B"
    elif marks>=60:
        return"c"
    else:
        return "Fail"
    
    student={
        "Shweta":95,
        "Dhanashri":82,
        "Vaishnavi":47,
        "Prachi":65
    }
    for name,marks in student.items():
        grade=calculate_grade(marks)
        print(f"{name} scored{marks}= Grade :{grade}")
        count=1
        while count<=3:
            print("This is attempt numbers :",count)
            count=1
        try:
            num=int(input("Enter a number to divide by 100 :"))
            result=100/num
            print("Result is :",result)
        except ZeroDivisionError:
            print("Error : Division By Zero Not Allowed !")
        except ValueError:
            print("Error:Please Enter A Valid Integer !")