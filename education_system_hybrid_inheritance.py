class institute:
    def __init__(self , name):
        self.name = name
    def show_institute(self):
        print(f"Institute Name :{self.name}")
class course(institute):
    def __init__(self , name , course_name , duration):
        super().__init__(name)
        self.course_name = course_name
        self.duration = duration
    def show_course(self):
        print(f"Course :{self.course_name} | Duration : {self.duration}months")
class Student :
    def __init__(self , stud_name , roll_no):
        self.stud_name = stud_name
        self.roll_no = roll_no
    def show_student(self):
        print(f"Student Name : {self.stud_name} | Roll No :{self.roll_no}")
class Result(course , Student):
    def __init__(self, name, course_name, duration,stud_name, roll_no, marks):
        course.__init__(self, name,course_name, duration)
        Student.__init__(self,stud_name, roll_no)
        self.marks=marks
    def show_result(self):
        grade=self.calculate_grade()
        print(f"Marks:{self.marks}% | Grade : {grade}")
    def calculate_grade(self):
        if self.marks>=85:
            return "A+"
        elif self.marks>=70:
            return "A"
        elif self.marks>=60:
            return "B"
        else:
            return "C"
print("\n\n----ONLINE EDUCATION SYSTEM----")
r1=Result("JSPM NTC" ,"Data Science" , 6 , "Amit Patil" , 101 , 88)
r1.show_institute()
r1.show_course()
r1.show_student()
r1.show_result()
print("\n\n----METHOD RESOLUTION ORDER ----")
print(Result.mro())
       
