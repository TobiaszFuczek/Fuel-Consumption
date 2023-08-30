from Car import Car


class User_Account:
    def __init__(self, login ="", password =""):
        self.login = login
        self.password = password
        self.cars = []
    def add_new_car(self):
        car_brand = input("Enter car brand: ")
        registration_number = input("Enter registration number: ")
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


if __name__ == '__main__':
    login = input("Request Login, your password is your e-mail: ")
    password = input("Request Password: ")
    user = User_Account(login, password)
    user.validate_password()
    user.add_new_car()
