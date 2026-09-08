class Card:
    def __init__(self, card_number, cvc, expiration_date, pin_code):
        self.card_number= card_number
        self.cvc= cvc
        self.expiration_date= expiration_date
        self.pin_code = pin_code

    def __str__(self):
        return f"Card number: {self.card_number}, Cvc: {self.cvc}, Expiration date: {self.expiration_date}, Pin code: {self.pin_code}"


    def to_dict(self):
        return {
              "card_number": self.card_number,
              "cvc": self.cvc,
              "expiration_date": self.expiration_date,
              "pin_code": self.pin_code
        }



    @classmethod
    def from_dict(cls, data):
        return cls(
            card_number=data["card_number"],
            cvc=data["cvc"],
            expiration_date=data["expiration_date"],
            pin_code=data["pin_code"]
        )
        


