class Student:
    grade_scale={"A":85,"B":70,"C":55,"D":40}
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def find_grade(marks):
        for grade,cutoff in Student.grade_scale.items():
            if marks>=cutoff:
                return grade
    @classmethod
    def update_scale(cls,new_scale):
        cls.grade_scale=new_scale
s1=Student("Shweta",90)
s2=Student("Dhanashri",60)
print(s1.name,"Grade :",Student.find_grade(s2.marks))
Student.update_scale({"A :",80,"B :",65,"C :",50,"D :",35})
print("Updated Scale :",Student.update_scale)
