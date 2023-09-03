from Car import Car
from UserAccount import UserAccount
from Refuel import Refuel

class View:
    def print_msg(self,msg):
        print(msg)

    def get_str(self, msg):
        self.print_msg(msg)
        return input()

class Model:
    def __init__(self, name):
        self.name = name

class ModelStorage:

    def __init__(self):
        self.storage = []

    def append(self, model):
        self.storage.append(model)

class Controller:
    def __init__(self):
        self.view = View()
        self.model_storage = ModelStorage()
        self.user_account = None

    def create_user_account(self):
        login = self.view.get_str("Enter login: ")
        password = self.view.get_str("Enter password: ")
        self.user_account = UserAccount(login, password)
        self.user_account.validate_password()

    def menu(self):
        while True:
            self.view.print_msg("APP Menu: ")
            self.view.print_msg("1. Enter model")
            self.view.print_msg("2. Display information about cars")
            self.view.print_msg("6. Exit")

            choice = self.view.get_str("Enter your choice: ")

            if choice == "1":
                if self.user_account:
                    car_name = self.view.get_str("Enter name: ")
                    car = Car(car_name, self.user_account)
                    refuel = Refuel(None, None, None, self.user_account, car)
                    refuel.enter_information_about_refuel()
                    self.user_account.add_new_car(car)
                    self.view.print_msg(f"Car {car_name} added to your account.")
                else:
                    self.view.print_msg("Please create a user account first.")

            elif choice == "2":
                if self.user_account:
                    self.user_account.display_cars()
                    car_choice = self.view.get_str("0 to go back: ")
                    if car_choice.isdigit():
                        car_choice = int(car_choice)
                        if 0 < car_choice <= len(self.user_account.cars):
                            car = self.user_account.cars[car_choice - 1]
                            print(f"Car: {car.name}")
                            print(f"Burning 100 km: {car.burning_100_km()}")
                            print(f"Drive in 1 liter: {car.drive_in_1_liter()}")
                            print(f"Average history: {car.average_history}")
                        elif car_choice == 0:
                            continue
                        else:
                            self.view.print_msg("Invalid car number.")
                    else:
                        self.view.print_msg("Invalid input. Please enter a valid car number.")
                else:
                    self.view.print_msg("Please log in first.")

    def control(self):
        self.create_user_account()
        self.menu()

# main
if __name__ == '__main__':
    Controller().control()