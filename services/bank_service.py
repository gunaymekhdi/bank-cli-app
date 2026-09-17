from models.account import Account
from models.transaction import Transactionq97

from models.card import Card

class BankService:

    def __init__(self, auth_service):
        self.auth_service = auth_service


    def create_account(self, acoount_number, currency="AZN"):

        current_user= self.authservice.get_current_user
        if not current_user:
            raise ValueError("Hesab yaratmaq üçün əvvəlcə sistemə giriş etməlisiniz!")

        for account in current_user.accounts:
            if account.account_number==account_number:
                raise ValueError("Bu hesab nömrəsi artıq mövcuddur!")

        new_account= Account(
            account_number=account_number,
            currency=currency
        )
        
        current_user.accounts.append(new_account)

        return new_account


    def deposit(self, account_number, amount):
        current_user = self.auth_service.get_current_user()
        if not current_user:
            raise ValueError("Əməliyyat üçün əvvəlcə sistemə giriş etməlisiniz!")


        if amount<=0:
            raise ValueError("Məbləğ müsbət olmalıdır!")


        target_account = None
        for account in current_user.accounts:
            if account.account_number == account_number:
                target_account = account
                break

        if not target_account:
            raise ValueError("Hesab tapılmadı!")


        target_account.balance += amount

        transaction =Transaction(
            amount=amount,
            transaction_type ="deposit",
            from_account=None,
            to_account=account_number

        )

        target_account.transactions.append(transaction)

        return target_account



    def withdraw(self, account_number, amount):

        current_user = self.auth_service.get_current_user()
        if not current_user:
            raise ValueError("Əməliyyat üçün əvvəlcə sistemə giriş etməlisiniz!")


        if amount<=0:
            raise ValueError("Məbləğ müsbət olmalıdır!")
        
        target_account =None
        for account in current_user.accounts:
            if account.account_number == account_number:
                target_account = account
                break

        if not target_account:
            raise ValueError("Hesab tapılmadı!")

        if target_account.balance < amount:
            raise ValueError("Balansda kifayət qədər vəsait yoxdur!")


        target_account.balance -=amount

        transaction = Transaction(
            amount=amount,
            transaction_type="withdraw",
            from_account=account_number,
            to_account=None
        )

        target_account.transactions.append(transaction)

        return target_account




    def transfer(self, sender_account_number, receiver_account_number, amount):
        current_user = self.auth_service.get_current_user()
        if not current_user:
            raise ValueError("Əməliyyat üçün əvvəlcə sistemə giriş etməlisiniz!")


        if amount <= 0:
            raise ValueError("Köçürüləcək məbləğ müsbət olmalıdır!")


        if sender_account_number == receiver_account_number:
            raise ValueError("Eyni hesaba köçürmə edə bilməzsiniz!")


        sender_account = None
        for account in current_user.accounts:
            if account.account_number == sender_account_number:
                sender_account = account
                break

        if not sender_account:
            raise ValueError("Göndərən hesab tapılmadı və ya sizə aid deyil!")


        if sender_account.balance < amount:
            raise ValueError("Hesabınızda kifayət qədər balans yoxdur!")


        receiver_account = None
        for user in self.auth_service.users:
            for account in user.accounts:
                if account.account_number == receiver_account_number:
                    receiver_account = account
                    break

            if receiver_account:
                break


        if not receiver_account:
            raise ValueError("Alan hesab sistemdə tapılmadı!")


        sender_account.balance -= amount
        receiver_account.balance += amount


        sender_transaction = Transaction(
            amount=amount,
            transaction_type="transfer_out",
            from_account=sender_account_number,
            to_account=receiver_account_number
        )
        sender_account.transactions.append(sender_transaction)


        receiver_transaction = Transaction(
            amount=amount,
            transaction_type="transfer_in",
            from_account=sender_account_number,
            to_account=receiver_account_number
        )
        receiver_account.transactions.append(receiver_transaction)

        return True



    def get_account_history(self, account_number):
        current_user = self.auth_service.get_current_user()
        if not current_user:
            raise ValueError("Əməliyyat üçün əvvəlcə sistemə giriş etməlisiniz!")

        for account in current_user.accounts:
            if account.account_number == account_number:
                return account.transactions


        raise ValueError("Hesab tapılmadı!")

            












        


        

        




        
