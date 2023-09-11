from Car import Car


class UserAccount:
    def __init__(self, login ="", password =""):
        self.login = login
        self.password = password
        self.cars = []
    def add_new_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars

    def display_cars(self):
        pass

    def validate_password(self):
        pass



