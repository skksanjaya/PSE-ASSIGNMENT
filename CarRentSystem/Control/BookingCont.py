from DAL.BookingDAO import SysBooking
import datetime

class BookingService():
    def __init__(self):
        self.booking = SysBooking()
    # Call Records View function
    def view_bookings(self):
        bookings = self.booking.view_bookings()
        if bookings:
            print("\n***** View Bookings *****")
            for booking in bookings:
                print(f"Booking ID: {booking[0]}, Customer ID: {booking[1]}, Car ID: {booking[2]}, Start Date: {booking[3]}, End Date: {booking[4]}, Status: {booking[5]}")
        else:
            print("No bookings")
    # Call Record Add function
    def add_booking(self, CustID, CarID, StartDate, EndDate, CreatedBy):
        try:
            start_date = datetime.datetime.strptime(StartDate, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(EndDate, '%Y-%m-%d').date()
            if start_date >= end_date:
                print("Error: End date must be greater than start date.")
                return
        except ValueError:
            print("Error: Invalid format - must be 'YYYY-MM-DD'.")
            return

        self.booking.add_booking(CustID, CarID, StartDate, EndDate, CreatedBy)
    # Call Record Update function
    def update_status(self, BookID, Status, ApproveBy=None):
        if Status not in ['1', '2', '3', '4', '5', '6']:
            print("Error: Invalid status")
            return
        
        self.booking.update_status(BookID, Status, ApproveBy)
    # Call Bookings witout Overdue
    def Current_bookings(self):
        bookings = self.booking.Current_bookings()
        if bookings:
            print("\n***** View ookings witout Overdue *****")
            for bookingRec in bookings:
                print(f"Booking ID: {bookingRec[0]}, Customer ID: {bookingRec[1]}, Car ID: {bookingRec[2]}, Start Date: {bookingRec[3]}, End Date: {bookingRec[4]}, Status: {bookingRec[5]}")
        else:
            print("No Bookings witout Overdue found.")
    # Call Bookings with Overdue
    def Overdue_bookings(self):
        bookings = self.booking.Overdue_bookings()
        if bookings:
            print("\n***** Overdue Bookings *****")
            for bookingRec in bookings:

                print(f"Booking ID: {bookingRec[0]}, Customer ID: {bookingRec[1]}, Car ID: {bookingRec[2]}, Start Date: {bookingRec[3]}, End Date: {bookingRec[4]}, Status: {bookingRec[5]}, Extra Days: {bookingRec[6]}, Extra Charge: ${bookingRec[7]:.2f}")
        else:
            print("No overdue bookings found.")