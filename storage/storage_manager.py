import json
import os
from models.user import User
from models.account import Account
from models.card import Card
from models.transaction import Transaction

class StorageManager:
    def __init__(self, filepath="bank_data.json"):
        self.filepath=filepath

    def save_data(self, users):
        data = []
        for user in users:
            user_data = {
                "username": user.username,
                "password_hash": user.password_hash,
                "accounts": []
            }

            for account in user.accounts:
                account_data={
                    "account_number": account.account_number,
                    "currency": account.currency,
                    "balance": account.balance,
                    "transactions": []
                }

                for transaction in account.transactions:
                    transaction_data = {
                        "amount": transaction.amount,
                        "transaction_type": transaction.transaction_type,
                        "from_account": transaction.from_account,
                        "to_account": transaction.to_account,
                        "timestamp": str(transaction.timestamp)
                    }

                    account_data["transactions"].append(transaction_data)

                user_data["accounts"].append(account_data)

            data.append(user_data)

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)



    def load_data(self):

        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

        users = []

        for user_dict in data:
            user = User(
                username=user_dict["username"],
                password_hash=user_dict["password_hash"]
            )


            for acc_dict in user_dict.get("accounts" , [] ):
                account = Account(
                    account_number=acc_dict["account_number"],
                    currency=acc_dict.get("currency", "AZN"),
                    balance=acc_dict.get("balance", 0.0)
                )

                for transaction_dict in acc_dict.get("transactions", []):
                    transaction = Transaction(
                        amount=transaction_dict["amount"],
                        transaction_type=transaction_dict["transaction_type"],
                        from_account=transaction_dict.get("from_account"),
                        to_account=transaction_dict.get("to_account")
                    )

                    if "timestamp" in transaction_dict:
                        transaction.timestamp = transaction_dict["timestamp"]

                    account.transactions.append(transaction)

                user.accounts.append(account)

            users.append(user)

        return users