class Bank :
    def __init__(self,bank_name):
        self.bank_name=bank_name
    def bank_info(self):
        print(f"Bank Name :{self.bank_name}")

class Customer(Bank):
    def __init__(self, bank_name , cust_name , cust_id):
        super().__init__(bank_name)
        self.cust_name = cust_name
        self.cust_id = cust_id

    def customer_info(self):
        print(f"Customer Name :{self.cust_name} | Customer Id : {self.cust_id}")
class KYC :
    def kyc_verified(self):
        print("\nKYC Verififcation : Completed")
class Account(Customer , KYC):
    def __init__(self, bank_name, cust_name, cust_id ,acc_no,balance ):
        super().__init__(bank_name, cust_name, cust_id)
        self.acc_no=acc_no
        self.balance=balance
    def account_info(self):
        print(f"Account No :{self.acc_no},Balance :₹{self.balance}")
    def kyc_verified(self):
        print("KYC verification : Verified Through Online Portal")
class Loan(Bank):
    def __init__(self, bank_name,loan_type,amount):
        super().__init__(bank_name)
        self.loan_type=loan_type
        self.amount = amount
    def loan_info(self):
        print(f"Loan Type:{self.loan_type},Amount :₹{self.amount}")
class tansaction(Account):
    def __init__(self, bank_name, cust_name, cust_id, acc_no, balance):
        super().__init__(bank_name, cust_name, cust_id, acc_no, balance)
    def deposite(self,amt):
        self.balance+=amt
        print(f"Deposited ₹{amt}successfully.New Balance ₹{self.balance}")
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance = amt
            print(f"Withdrawn ₹ {amt}.Remaining Balance : ₹ {self.balance}")
        else:
            print("Insufficient Balance ")
print("\n----Bank Management System----")
acc1=Account("SBI Bank","Amit","C101",123456,500000)
acc1.bank_info()
acc1.customer_info()
acc1.account_info()
acc1.kyc_verified()
print("\n----Loan Information")
loan1=Loan("SBI Bank","Home Loan",8000000)
loan1.bank_info()
loan1.loan_info()
print("\n----Transaction Details ----")
t1=tansaction("SBI Bank","Amit","c101",123456,500000)
t1.deposite(100000)
t1.withdraw(20000)
print("\n----MRO----")
print(tansaction.mro())
        