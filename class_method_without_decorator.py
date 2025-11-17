class Student:
        school_name="JSPM NTC"
        def __init__(self,name,marks):
            self.name=name
            self.marks=marks
                            #Class Method Without Decorator
        def change_school(cls,new_name):
            cls.school_name=new_name
                            #Static Method Withot Decorator
        def is_pass(marks):

            return marks>=40
                            #Calling Without Manually Without Decorator 
Student.change_school =classmethod(Student.change_school)
Student.is_pass=staticmethod(Student.is_pass)
s1=Student("Shweta",88)
s2=Student("Dhanashri",55)
print("Before :",Student.school_name)
Student.change_school("SPPU Affiliated College")
print("After :",Student.school_name)
print(s1.name,"Pass :",Student.is_pass(s1.marks))
print(s2.name,"Pass :",Student.is_pass(s2.marks))