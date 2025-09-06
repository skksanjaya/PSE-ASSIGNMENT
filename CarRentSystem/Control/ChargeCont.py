from DAL.ChargeDAO import SysCharge

class ChargeService():
    def __init__(self):
        self.charge = SysCharge()
    # Call Record Add function
    def add_charge(self, BookID, Amount, CreatedBy):
        try:
            Amount = float(Amount)
        except ValueError:
            print("Error: Invalid Amount")
            return

        if not all([BookID, Amount, CreatedBy]):
            print("Error: All fields are required.")
            return

        self.charge.add_charge(BookID, Amount, CreatedBy)

