from DAL.PaymentDAO import SysPayment

class PaymentService():
    def __init__(self):
        self.payment = SysPayment()
    # Call Record Add function
    def add_payment(self, BookID, Amount, Status, CreatedBy):
        try:
            Amount = float(Amount)
        except ValueError:
            print("Error: Invalid Amount ")
            return

        if not all([BookID, Amount, Status, CreatedBy]):
            print("Error: All fields are required.")
            return
        
        self.payment.add_payment(BookID, Amount, Status, CreatedBy)
    # Call Record Update function
    def update_status(self, PayID, Status):
        if Status not in ['1', '2']:
            print("Error: Invalid status.")
            return

        self.payment.update_status(PayID, Status)

    # Call Vew record from ID
    def view_user_payments(self, logged_id):
        payments = self.payment.view_payments_by_user_id(logged_id)
        
        if payments:
            print("\n***** View Payment Records *****")
            for paymentRec in payments:
                print(f"Payment ID: {paymentRec[0]}, Booking ID: {paymentRec[1]}, Amount: ${paymentRec[2]}, Status: {paymentRec[3]}, Car ID: {paymentRec[5]}, Start: {paymentRec[6]}, End: {paymentRec[7]}")
        else:
            print("No records found")