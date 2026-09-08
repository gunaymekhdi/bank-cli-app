from models.account import Account

class User:

    def __init__(self,user_id,full_name, email,pin_code,password_hash,accounts):
        self.user_id=user_id
        self.full_name=full_name
        self.email=email
        self.pin_code=pin_code
        self.password_hash=password_hash
        self.accounts=None if accounts is None else accounts



    def add_account(self, account):
        self.accounts.append(account)



    def to_dict(self):
        return{
            "user_id": self.user_id,
            "full_name": self.full_name,
            "email": self.email,
            "fin_code": self.pin_code,
            "password_hash": self.password_hash,
            "accounts":[account.to_dict() for account in self.accounts]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
           user_id= data["user_id"],
           full_name=data["full_name"],
           email=data["email"],
           fin_code=data["fin_code"],
           password_hash=data["password_hash"],
           accounts=[Account.from_dict(c) for c in data.get("accounts", [])]
        )
