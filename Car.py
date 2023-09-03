class Car:
    def __init__(self, name, user_account):
        self.name = name
        self.user_account = user_account
        self.refueling_history = []
        self.kilometers = 0
        self.amount_liters = 0
    def add_refuel(self, refuel):
        self.refueling_history.append(refuel)
        self.kilometers += refuel.kilometers
        self.amount_liters += refuel.amount_liters
    def burning_100_km(self):
        if self.kilometers > 0:
            return (self.amount_liters / self.kilometers) * 100
        else:
            return 0

    def drive_in_1_liter(self):
        if self.amount_liters > 0:
            return self.kilometers / self.amount_liters
        else:
            return 0

    @property
    def average_history(self):
        if self.refueling_history:
            total_liters = sum([entry.amount_liters for entry in self.refueling_history])
            total_kilometers = sum([entry.kilometers for entry in self.refueling_history])
            return total_liters / total_kilometers if total_kilometers > 0 else 0
        else:
            return 0

