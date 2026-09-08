from datetime import datetime

class Transaction:
  def __init__(self,transaction_id, sender_account, receiver_account, amount, currency, timestamp,status):
    self.transaction_id= transaction_id
    self.sender_account= sender_account
    self.receiver_account= receiver_account
    self.amount= amount
    self.currency= currency
    self.timestamp= timestamp
    self.status = status

    def __str__(self):

        return f"Transaction ID: {self.transaction_id}, Sender Account Number: {self.sender_account}, Receiver Account Number: {self.receiver_account}, Amount: {self.amount}, Currency: {self.currency}, Timestamp: {self.timestamp}, Status: {self.status}"
    

    def to_dict(self):
        return {
           "transaction_id": self.transaction_id,
           "sender_account": self.sender_account,
           "receiver_account": self.receiver_account,
           "amount": self.amount,
           "currency": self.currency,
           "timestamp": self.timestamp,
           "status": self.status
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            transaction_id=data["transaction_id"],
            sender_account=data["sender_account"],
            receiver_account=data["receiver_account"],
            amount=data["amount"],
            currency=data["currency"],
            timestamp=data["timestamp"],
            status=data["status"]
        )



