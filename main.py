
from Refuel import Refuel
from Car import Car


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

    def control(self):
        while True:
            self.view.print_msg("APP Menu: ")
            self.view.print_msg("1. Enter model")
            self.view.print_msg("6. Exit")

            choice = self.view.get_str("Enter your choice: ")

            if choice == "1":
                car = self.model_storage.append(Model(self.view.get_str("Enter name:")))
            elif choice == "6":
                view.print_msg("Exiting the Fuel Consumption App.")
            break


# main
if __name__ == '__main__':
    Controller().control()
