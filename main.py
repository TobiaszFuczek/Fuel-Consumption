from Car import Car
from UserAccount import UserAccount


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

    def menu(self):
        while True:
            self.view.print_msg("APP Menu: ")
            self.view.print_msg("1. Enter model")
            self.view.print_msg("6. Exit")

            choice = self.view.get_str("Enter your choice: ")

            if choice == "1":
                if self.user_account:
                    car_name = self.view.get_str("Enter name: ")
                    self.user_account.add_new_car(Car(car_name, self.user_account))
                    self.view.print_msg(f"Car {car_name} added to your account.")
                else:
                    self.view.print_msg("Please create a user account first.")
            elif choice == "6":
                self.view.print_msg("Exiting the Fuel Consumption App.")
                break

    def control(self):
        self.create_user_account()
        self.menu()

# main
if __name__ == '__main__':
    Controller().control()
