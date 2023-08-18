from bank_management.bank import Bank
from bank_management.controller import BankController
from bank_management.commands import Deposit, Transfer, Withdrawal


def main() -> None:

    bank = Bank()

    controller = BankController()

    account1 = bank.create_account("brijesh")
    account2 = bank.create_account("ismail")
    account3 = bank.create_account("sachin")

    controller.execute(Deposit(account1, 100000))
    controller.execute(Deposit(account2, 100000))
    controller.execute(Deposit(account3, 100000))

    controller.execute(Transfer(from_account=account1, to_account=account3, amount=4000))
    controller.undo()

    print(bank)


if __name__ == "__main__":
    main()
