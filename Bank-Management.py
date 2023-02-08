class Bank:
    def __init__ (self,balance):
        self.balance=balance
        self.minWithdraw=100
        self.mxWithdraw=1000
    def current_balance(self):
        return "Your current balance is {value}".format(value=self.balance)
    def withdraw_balance(self,withrdraw_amount):
        if(withrdraw_amount<self.minWithdraw):
            txt="You can not withdraw less than {value} amount"
            print(txt.format(value=self.minWithdraw))
        elif (withrdraw_amount>self.mxWithdraw):
            txt="You can not withdraw more than {value} amount"
            print(txt.format(value=self.mxWithdraw))
        elif (withrdraw_amount>self.balance):
            txt="You do not have necessary amount to withdraw {value} amount"
            print(txt.format(value=self.mxWithdraw))
        else:
            self.balance=self.balance-withrdraw_amount
            return "You have withdraw {value} amount".format(value=withrdraw_amount)
    def deposite(self,dep_amount):
        self.balance=self.balance+dep_amount
        return "You have deposited {value} amount".format(value=dep_amount)

myBank=Bank(0)
while True:
    print("1.Deposite Amount")
    print("2.Withdraw Amount")
    print("3.Check Amount")
    print("4.Exit")
    print("5.Enter choice:",end="")
    choice=int(input())
    if choice==1:
        print("Enter the amount you want to enter:",end="")
        am=int(input())
        if(am<=0):
            print("You must enter greater than zero amount")
        else:
            print(myBank.deposite(am))
    elif choice==2:
        print("Enter the amount you want to withdraw:",end="")
        am=int(input())
        if(am<=0):
            print("You must enter greater than zero amount")
        else:
            print(myBank.withdraw_balance(am))
    elif choice==3:
        print(myBank.current_balance())
    elif choice==4:
        break
    else:
        print("Invalid Choice\n")

