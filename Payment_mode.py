class Payment:
    def transaction_charge(self,amount):
        return 0
class CreditCardPayment(Payment):
    def transaction_charge(self, amount):
        return amount*0.02
class PayPalPayment(Payment):
    def transaction_charge(self, amount):
        return amount*0.03
class UPIPayment(Payment):
    def transaction_charge(self, amount):
        return amount*0.01
amount=1000
credit=CreditCardPayment()
PayPal=PayPalPayment()
UPI=UPIPayment()
print("Credit Card Charges : ₹",credit.transaction_charge(amount))
print("PayPal Charges : ₹",PayPal.transaction_charge(amount))
print("UPI : ₹",UPI.transaction_charge(amount))
        