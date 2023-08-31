from UserAccount import UserAccount
from Car import Car
from Refuel import Refuel


def main():
    user = None  # Zmienna przechowująca obiekt UserAccount

    while True:
        print("Fuel Consumption APP Menu: ")
        print("1. Enter your Login and Password")
        print("2. Register Refueling")
        print("3. Calculate Current Fuel Consumption")
        print("4. Calculate Average Fuel Consumption")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if user is None:
                login = input("Request Login, your password is your e-mail: ")
                password = input("Request Password: ")
                user = UserAccount(login, password)
                user.validate_password()
                print("Login successful.")
            else:
                print("You are already logged in.")

        elif choice == "2":
            if user is not None:
                # Dodaj nowy samochód do konta użytkownika
                user.add_new_car()

                # Tworzymy instancję Car na podstawie wprowadzonych danych
                car = user.get_cars()[-1]  # Zakładamy, że użytkownik dodał ostatnio dodany samochód

                # Wprowadź informacje o tankowaniu
                refuel = Refuel(None, None, None, user, car)
                refuel.enter_information_about_refuel()

                # Dodaj informacje o tankowaniu do historii samochodu
                car.add_refuel(refuel)

                print("Refueling registered.")
            else:
                print("You need to log in first.")

        # Tutaj możesz dodać pozostałe opcje menu (obliczenia, wyjście, itp.)

        elif choice == "5":
            print("Exiting the Fuel Consumption App.")
            break


if __name__ == '__main__':
    main()
