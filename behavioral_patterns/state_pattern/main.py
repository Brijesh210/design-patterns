class VendingMachine:
    def __init__(self):
        self.state = NoMoneyState(self)
        self.balance = 0

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def select_item(self, item):
        self.state.select_item(item)
        self.state.dispense_item()

    def set_state(self, state):
        self.state = state

    def add_balance(self, amount):
        self.balance += amount

    def deduct_balance(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


class State:
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self, amount):
        pass

    def select_item(self, item):
        pass

    def dispense_item(self):
        pass


class NoMoneyState(State):
    def insert_money(self, amount):
        self.vending_machine.add_balance(amount)
        self.vending_machine.set_state(HasMoneyState(self.vending_machine))
        print(f"Inserted PLN{amount}. Balance: PLN{self.vending_machine.get_balance()}")


class HasMoneyState(State):
    def select_item(self, item):
        item_price = ItemDatabase.get_price(item)
        if self.vending_machine.get_balance() >= item_price:
            self.vending_machine.deduct_balance(item_price)
            self.vending_machine.set_state(NoMoneyState(self.vending_machine))
            print(f"Dispensing {item} \nremaining balance: PLN{self.vending_machine.get_balance()}\n")
        else:
            print("Insert more money")

    def dispense_item(self):
        print("Select item")


class ItemDatabase:
    @staticmethod
    def get_price(item):
        prices = {
            "chips": 5.0,
            "chocolate": 3.0,
            "drink": 4.0
        }
        return prices.get(item, 0.0)


vending_machine = VendingMachine()
vending_machine.insert_money(6.0)
vending_machine.select_item("chips")
