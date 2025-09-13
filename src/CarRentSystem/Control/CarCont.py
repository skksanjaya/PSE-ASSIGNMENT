from DAL.CarDAO import SysCar

class CarService():
    def __init__(self):
        self.car = SysCar()
    # Call Records View function
    def view_cars(self):
        cars = self.car.view_cars()
        if cars:
            print("\n***** View Cars *****")
            for carList in cars:
                print(f"ID: {carList[0]}, Make: {carList[1]}, Model: {carList[2]}, Year: {carList[3]}, Mileage: {carList[4]} ,Daily Rate: ${carList[8]}, Available: {carList[5]}, Min Days: {carList[6]}, Max Days: {carList[7]}")
        else:
            print("No records found!")
    # Call Record Add function
    def add_car(self, Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy):
        # Input validation
        if not all([Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy]):
            print("Error: All values required.")
            return

        try:
            Year = int(Year)
            Mileage = int(Mileage)
            Available = int(Available)
            MinDays = int(MinDays)
            MaxDays = int(MaxDays)
            DailyRate = float(DailyRate)
        except ValueError:
            print("Error: Year, Mileage, Available, MinDays, MaxDays, and DailyRate must be numbers.")
            return

        self.car.add_car(Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy)
    # Call Record Update function
    def update_car(self, CarID, Make=None, Model=None, Year=None, Mileage=None, Available=None, MinDays=None, MaxDays=None, DailyRate=None, ModifiedBy=None):
        try:
            self.car.update_car(CarID, Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, ModifiedBy)
        except ValueError:
            print("Car can not Update ")
            return
        
    # Call Record Delete function
    def delete_car(self, CarID):
        try:
            self.car.delete_car(CarID)
        except ValueError:
            print("Car can not delete")