class Car:
    def __init__(self, name, user_account):
        self.name = name
        self.user_account = user_account
        self.refueling_history = []

    def add_refuel(self, refuel):
        self.refueling_history.append(refuel)

