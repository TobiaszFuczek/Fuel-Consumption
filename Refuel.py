class Refuel:
    def __init__(self, date_time, amount_liters, kilometers, user, car):
        self.date_time = date_time
        self.amount_liters = amount_liters
        self.kilometers = kilometers
        self.user = user
        self.car = car

    def enter_information_about_refuel(self):
        self.date_time = "Enter date and time in formatt (DD-MM-YYYY) and (HH:MM): "
        self.amount_liters = "Enter amount liters refueled: "
        self.kilometers = "Enter kilometers driven: "
        self.car.add_refuel(self)


