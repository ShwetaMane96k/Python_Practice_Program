class Employee :
    def __init__(self,emp_id,emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
    def show_employee(self):
        print(f"Employee Id :{self.emp_id} | Employee Name :{self.emp_name}")
class Attendance :
    def __init__(self,days_present):
        self.days_present = days_present
    def show_attendance(self):
        print(f"Days Present : {self.days_present}/30")
class Payroll(Employee , Attendance):
    def __init__(self, emp_id, emp_name, days_present, Salary_per_day):
        Employee .__init__(self,emp_id, emp_name)
        Attendance.__init__(self,days_present)
        self.salary_per_day = Salary_per_day
    def calculate_salary(self):
        total_salary=self.days_present*self.salary_per_day
        return total_salary
    def show_payroll(self):
        self.show_employee()
        self.show_attendance()
        print(f"Salary per Day :₹{self.salary_per_day}")
        print(f"Total Salary :₹{self.calculate_salary()} ")
print("\n\n----Employee Payroll System----")
p1=Payroll(101,"Shweta Mane" , 27, 15000)
p1.show_payroll()
print("\n----METHOD RESOLUTION METHOD----")
print(Payroll.mro())
        