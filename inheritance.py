class Mpesa:
    def __init__(self,account_bal,phone_number):
        self.account_bal = account_bal
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_bal >= amount:
            self.account_bal -= amount
            print(f"{amount} KES sent to {recipient}")
        else:
            print("Insufficient balance")

class Personal_Mpesa(Mpesa):
    def __init__(self,account_bal, phone_number, id_number):
        super(). __init__(account_bal, phone_number)
        self.id_number = id_number
    def buy_airtime(self,amount):
        if self.account_bal >= amount:
            self.account_bal -= amount
            print(f"{amount}KES airtime bought succesfully.")
        else:
            print("Insufficient balance")

class Business_Mpesa(Mpesa):
    def __init__(self, account_bal, phone_number, business_name):
        super().__init__(account_bal, phone_number)
        self.business_name = business_name
    def receive_money(self,amount):
        self.account_bal += amount
        print(f"{amount} Kes received succesfully")

personal = Personal_Mpesa(500, 723456787,76543223)
personal.send_money(480,735336447)
personal.buy_airtime(25)

biz = Business_Mpesa (677, 732467983, "LYD Enterprises")
biz.receive_money(20000)
