from dataclasses import dataclass

from account import Account


# class implement transaction Protocol
@dataclass
class Deposit:
    account: Account
    amount: int

    @property
    def transfer_details(self) -> str:
        return f"${self.amount} to account {self.account.name}"

    def execute(self):
        self.account.deposit(self.amount)
        print(f"Deposited {self.transfer_details}")

    def undo(self):
        self.account.withdraw(self.amount)
        print(f"undo deposit of  {self.transfer_details}")

    def redo(self):
        self.account.deposit(self.amount)
        print(f"redo deposit of  {self.transfer_details}")


@dataclass
class Withdrawal:
    account: Account
    amount: int

    @property
    def transfer_details(self) -> str:
        return f"${self.amount} to account {self.account.name}"

    def execute(self):
        self.account.withdraw(self.amount)
        print(f"Withdrawal {self.transfer_details}")

    def undo(self):
        self.account.deposit(self.amount)
        print(f"undo deposit of  {self.transfer_details}")

    def redo(self):
        self.account.withdraw(self.amount)
        print(f"redo deposit of  {self.transfer_details}")


@dataclass
class Transfer:
    from_account: Account
    to_account: Account
    amount: int

    @property
    def transfer_details(self) -> str:
        return f"${self.amount} from account {self.from_account.name} to account {self.to_account.name}"

    def execute(self):
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)

        print(f"transfer {self.transfer_details}")

    def undo(self):
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)

        print(f"undo transfer {self.transfer_details}")

    def redo(self):
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)

        print(f"redo transfer {self.transfer_details}")
