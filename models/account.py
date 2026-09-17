from models.card import Card


class Account:

    def __init__(self, account_number, balance, currency, cards):
        self.account_number=account_number
        self.balance=balance
        self.currency=currency
        self.cards=None if cards is None else cards


    def __str__(self):
        return f"Account number: {self.account_number}, Balance: {self.balance}, Currency: {self.currency}, Cards: {self.cards}"



    def deposit(self,amount):
        self.balance+=amount
        return self.balance


    def withdraw(self,amount):

        if amount>self.balance:
            raise ValueError("Insufficient balance.")
         
        else:
            self.balance-=amount
 
    def to_dict(self):
        return{
            "account_number": self.account_number,
            "balance": self.balance,
            "currency": self.currency,
            "cards": [card.to_dict() for card in self.cards]
        }    


    @classmethod
    def from_dict(cls, data):
        return cls(
            account_number= data["account_number"],
            balance=data["balance"],
            currency=data["currency"],
            cards=[Card.from_dict(c) for c in data.get("cards", [])]
        )    
    