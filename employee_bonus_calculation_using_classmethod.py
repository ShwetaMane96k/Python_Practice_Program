class Employee:
    company_name="Infosys"
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod 
    def change_company(cls,new_company):
        cls.company_name=new_company
    @staticmethod
    def calculate_bonus(salary):
        return salary *0.10 if salary>50000 else salary*0.05
emp1=Employee("Shweta",800000)
emp2=Employee("Dhanashri",40000)
print(f"{emp1.name} Bonus :",Employee.calculate_bonus(emp1.salary))
print(f"{emp2.name} Bonus :",Employee.calculate_bonus(emp2.salary))
Employee.change_company("TCS")
print("Updated Company :",Employee.company_name)
