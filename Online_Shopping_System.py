class Customer :
    def __init__(self,name,total_purchase):
        self.name=name
        self.total_purchase=total_purchase
    def get_discount(self):
        return self.total_purchase*0.02
    def final_amount(self):
        discount=self.get_discount()
        return self.total_purchase-discount
class PremiumCustomer(Customer):
    def get_discount(self):
        base_discount=super().get_discount()
        extra_discount=self.total_purchase*0.03
        return base_discount+extra_discount
class CorporateCustomer(Customer):
    def get_discount(self):
        return self.total_purchase*0.10
cust1=Customer("Amol",10000)
cust2=PremiumCustomer("Vishal",20000)
cust3=CorporateCustomer("TCS Pvt Ltd",50000)
print(f"{cust1.name} pays :  ₹ {cust1.final_amount():.2f}")
print(f"{cust2.name} pays :  ₹ {cust2.final_amount():.2f}")
print(f"{cust3.name} pays :  ₹ {cust3.final_amount():.2f}")