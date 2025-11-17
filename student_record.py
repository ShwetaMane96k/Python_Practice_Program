def student_generator(students):
    for name,age,marks in students:
        yield{
            "name": name,
            "age": age,
            "marks": marks,
            "status":"pass"if marks>=40 else "Fail"
          }
        students=[
            ("shweta",21,85),
            ("Dhanashri",22,80),
            ("Vaishnavi",20,75),
            ("Sakshi",21,35),
            ("Gautami",20,45)
        ]
        gen=student_generator(students)
        print("Fetching student record (One By One):\n")
        for student in gen:
            print(student)

def topper_generator(students):
    max_marks=max(s[2]for s in students)
    for s in students:
        yield s
        print("\nTopperr(s):")
        for topper in topper_generator(students):
            print(topper)
        