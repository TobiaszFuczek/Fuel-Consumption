class Refuel:
    def __init__(self, date_time, amount_liters, kilometers, user, car):
        self.datetime = date_time
        self.amount_liters = amount_liters
        self.kilometers = kilometers
        self.user = user
        self.car = car

    def enter_information_about_refuel(self):
        self.date_time = input("Enter date and time in formatt (DD-MM-YYYY) and (HH:MM): ")
        self.amount_liters = float(input("Enter amount liters refueled: "))
        self.kilometers = float(input("Enter kilometers driven: "))


