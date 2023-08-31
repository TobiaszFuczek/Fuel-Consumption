from UserAccount import UserAccount
from Refuel import Refuel
from Car import Car

def main():
    user = None  # Variable storing the object UserAccount

    while True:
        print("Fuel Consumption APP Menu: ")
        print("1. Enter your Login and Password")
        print("2. Register Refueling")
        print("3. Calculate Current Fuel Consumption")
        print("4. Calculate Average Fuel Consumption")
        print("5. Preview in Register Refueling")
        print("6. Exit")

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
                # Add new car to user account
                user.add_new_car()

                # Create a Car instance based on the data entered
                car = user.get_cars()[-1]  # Zakładamy, że użytkownik dodał ostatnio dodany samochód

                # Enter information about refueled
                refuel = Refuel(None, None, None, user, car)
                refuel.enter_information_about_refuel()

                # Add information about refuel to car history
                car.add_refuel(refuel)

                print("Refueling registered.")
            else:
                print("You need to log in first.")

        elif choice == "5":
            if user is not None:
                cars = user.get_cars()
                if cars:
                    print("Cars in your account:")
                    for i, car in enumerate(cars, 1):
                        print(f"{i}. Car Name: {car.name}, Registration Number: {car.registration_number}")
                else:
                    print("You haven't registered any cars yet.")
            else:
                print("You need to log in first.")
        # Here can you add other options menu (calculation, output, etc.)

        elif choice == "6":
            print("Exiting the Fuel Consumption App.")
            break


if __name__ == '__main__':
    main()
