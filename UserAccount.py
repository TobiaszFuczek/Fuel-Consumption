from Car import Car


class UserAccount:
    def __init__(self, login ="", password =""):
        self.login = login
        self.password = password
        self.cars = []
    def obj(self):
        car = Car(car_brand, user_account=self)
        car.registration_number =  registration_number
        self.cars.append(car)

    def get_cars(self):
        return self.cars
    def validate_password(self):
        while True:
            if len(self.password) >= 8 and any(c.isupper() for c in self.password) and any(sign in self.password for sign in ["!", ",", ".", "$", "%", "&", "*", "?"]):
                print("Password is correct")
                break
            else:
                print("Password is too short or wrong, please try again")
                self.password = input("Request Password: ")



