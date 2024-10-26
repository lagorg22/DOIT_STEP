# დავალება 1.
# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით,
# როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები. შექმენით
# რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.


class BankAccount:
    def __init__(self, account_number: str, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance: float = 0.0

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            print('Deposit successful.\n')
            return True
        else:
            print('You can only deposit positive amount.\n')
            return False

    def  withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            print('Withdraw successful.\n')
            return True
        else:
            print(f'Sorry {self.account_holder} Insufficient balance.\n')
            return False


bank_acc1 = BankAccount('123', 'Lasha')
bank_acc1.deposit(200)
bank_acc1.deposit(100)
bank_acc1.withdraw(200)
bank_acc1.withdraw(4030)

bank_acc2 = BankAccount('111', 'Irakli')
bank_acc2.deposit(9999999)
for i in range(1_000_000):
    if not bank_acc2.withdraw(i**i):
        break
