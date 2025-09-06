from database import create_table

# Import managers
from Control.UserCont import UserService 
from Control.CarCont import CarService
from Control.BookingCont import BookingService
from Control.PaymentCont import PaymentService
from Control.ChargeCont import ChargeService

logged_id = None
logged_role = None

def menu():
    print("\n==== Car Management System ====")
    print("1. New User")
    print("2. Login")
    print("3. Exit")

def menuAdmin():     
    print("1. View Car")
    print("2. Add Car")
    print("3. Update Car")
    print("4. Delete Class")
    print("5. Approve/Reject Booking")
    print("6. Complete without Overdue")
    print("7. Complete Overdue Bookings")
    print("8. Exit")

def menuCutomer():    
    print("1. View Car")
    print("2. Add Booking")
    print("3. Payment for approved booking")
    print("4. Exit")


def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-19): ")
        user=UserService()
        
        if choice == '1':
            name = input("Enter Customer name: ")
            address = input("Enter Address: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            password = input("Enter password: ")
            if (user.user_exists(email)):
                print("Email Already Exsists!")
            else:
                user.add_user(name, address, email,"2",password,phone)
                print("Added Successfully!")
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            user_id = user.login(email, password)
            if user_id:
                sessionVarieables = user_id.split('|')
                logged_id = sessionVarieables[0]
                logged_role = sessionVarieables[1]
                if logged_role == '1':
                    car_service = CarService()
                    booking_service = BookingService()
                    charge_service = ChargeService()
                    while True:
                        menuAdmin()
                        choice = input("Select an option (1-7): ")
                        if choice == '1':
                            car_service.view_cars()
                        elif choice == '2':
                            Make = input("Enter Make: ")
                            Model = input("Enter Model: ")
                            Year = input("Enter Year: ")
                            Mileage = input("Enter Mileage: ")
                            Available = input("Enter Available (1 for Available or 2 for Maintanance): ")
                            MinDays = input("Enter Min rent days: ")
                            MaxDays = input("Enter Max rent days: ")
                            DailyRate = input("Enter Daily Rate: ")
                            car_service.add_car(Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, logged_id)
                        elif choice == '3':
                            CarID = input("Enter Car ID : ")
                            Make = input("Enter new Make : ") or None
                            Model = input("Enter new Model : ") or None
                            Year = input("Enter new Year : ") or None
                            Mileage = input("Enter new Mileage : ") or None
                            Available = input("Enter new Available (1 for Available or 2 for Maintanance): ") or None
                            MinDays = input("Enter new Minimum rental days : ") or None
                            MaxDays = input("Enter new Maximum rental days : ") or None
                            DailyRate = input("Enter new Daily Rate : ") or None
                            car_service.update_car(CarID, Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, logged_id)
                        elif choice == '4':
                            CarID = input("Enter Car ID to delete: ")
                            car_service.delete_car(CarID)
                        elif choice == '5':
                            booking_service.view_bookings()
                            BookID = input("Enter Booking ID to update status: ")
                            status = input("Enter new status ('2-approved/3-rejected'): ")
                            booking_service.update_status(BookID, status, logged_id)
                        elif choice == '6':
                            booking_service.Current_bookings()
                            BookID = input("Enter Booking ID to complete: ")
                            booking_service.update_status(BookID, '5')
                        elif choice == '7':
                            booking_service.Overdue_bookings()
                            BookID = input("Enter Booking ID to complete: ")
                            Amount = input("Enter the extra charge amount: ")
                            if float(Amount) > 0:
                                charge_service.add_charge(BookID, Amount, logged_id)
                                booking_service.update_status(BookID, '5')
                        elif choice == '8':
                            print("Back to Main Menu")
                            break
                        else:
                            print("Wromg choice, try again.")
                else:
                    car_service = CarService()
                    booking_service = BookingService()
                    payment_service = PaymentService()
                    charge_service = ChargeService()
                    while True:
                        menuCutomer() 
                        choice = input("Select an option (1-4): ")
                        if choice == '1':
                            car_service.view_cars()
                        elif choice == '2':
                            CarID = input("Enter Car ID : ")
                            StartDate = input("Enter start date (YYYY-MM-DD): ")
                            EndDate = input("Enter end date (YYYY-MM-DD): ")
                            booking_service.add_booking(logged_id, CarID, StartDate, EndDate, logged_id)
                        elif choice == '3':
                            payment_service.view_user_payments(logged_id)
                            PayID = input("Enter Payment ID to Pay: ")
                            BookID = input("Enter Book ID to Pay: ")
                            payment_service.update_status(PayID, '2')
                            booking_service.update_status(BookID, '4')                        
                        elif choice == '4':
                            print("Back to Main Menu")
                            break
                        else:
                            print("Wromg choice, try again.")
            else:
                logged_id = None
                print("Login failed.")
        elif choice == '3':       
            print("End!")
            break
        else:
            print("Wrong choice, try again.")


if __name__ == "__main__":
    main()
