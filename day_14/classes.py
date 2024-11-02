
class Person:
    def __init__(self, name: str, deposit: float=1000, loan: float=0):
        self.name = name
        self.__deposit = deposit
        self.__loan = loan

    def __str__(self):
        return (f'Name: {self.name}, '
                f'Deposit: {self.__deposit}, '
                f'Loan: {self.__loan}\n')

    @property
    def deposit(self):
        return self.__deposit

    @deposit.setter
    def deposit(self, amount: float):
        self.__deposit = amount

    @property
    def loan(self):
        return self.__loan

    @loan.setter
    def loan(self, amount: float):
        self.__loan = amount

    def can_afford(self, price: float):
        return price <= self.deposit


class House:
    def __init__(self, id: str, price: float):
        self.id = id
        self.price = price
        self.__owner: Person = None
        self.__status = 'For Sale'

    def __str__(self):
        return (f'ID: {self.id}, '
                f'Price: {self.price}, '
                f'Owner: {self.__owner.name if self.__owner else None}, '
                f'Status: {self.__status}\n')

    def sale(self, buyer: Person, loan_amount: float=None):
        if loan_amount:
            self.__loan_sale(buyer, loan_amount)
        else:
            self.__ordinary_sale(buyer)

    def __ordinary_sale(self, buyer: Person):
        if buyer.can_afford(self.price):
            if self.__owner:
                self.__owner.deposit += self.price
            buyer.deposit -= self.price
            self.__owner = buyer
            self.__status = 'Sold'
        else:
            print(f'Buyer {buyer.name} can not afford this house.\n')

    def __loan_sale(self, buyer: Person, loan_amount: float):
        if buyer.can_afford(self.price - loan_amount):
            if self.__owner:
                self.__owner.deposit += self.price
            buyer.deposit += loan_amount
            buyer.deposit -= self.price
            buyer.loan += loan_amount
            self.__owner = buyer
            self.__status = 'Sold With Loan.'
        else:
            print(f'Buyer {buyer.name} can not afford the house with this loan amount.\n')