class User_Account:
    def __init__(self, login = str, password = str,):
        self.login = login
        self.password = password
        self.cars = []
    def add_new_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars
    def validate_password(self):
        if self.password >= 8:
            for x in self.password:
                if 'A'<=x<='Z':
                    special_sign = ["!", ",", ".", "$", "%", "&", "*", "?"]
                    invalid = False
                    for signs in self.password:
                        if signs not in special_sign:
                            print(f"Please try again, use only {special_sign}")
                            invalid = True
                            break
                    if not invalid:
                        print("Valid Password")
                else:
                    return False
