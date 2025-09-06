from database import create_connection
import sqlite3

class SysBooking():
    # View List
    def view_bookings(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM SysBooking")
            bookings = cursor.fetchall()
            return bookings
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()
     # Add record 
    def add_booking(self, CustID, CarID, StartDate, EndDate, CreatedBy):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO SysBooking (CustID, CarID, StartDate, EndDate, Status, CreatedBy) VALUES (?, ?, ?, ?, ?, ?)",
                (CustID, CarID, StartDate, EndDate, '1', CreatedBy)
            )
            conn.commit()
            print("Added successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Update Record
    def update_status(self, BookID, Status, ApproveBy=None):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            if ApproveBy:
                cursor.execute(
                    "UPDATE SysBooking SET Status = ?, ApproveBy = ?, ApproveDate = datetime('now') WHERE BookID = ?",
                    (Status, ApproveBy, BookID)
                )
            else:
                cursor.execute(
                    "UPDATE SysBooking SET Status = ? WHERE BookID = ?",
                    (Status, BookID)
                )
            conn.commit()
            print("Updated successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()

    # Bookings witout Overdue
    def Current_bookings(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM SysBooking WHERE EndDate >= DATE('now')")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()
    # Bookings with Overdue
    def Overdue_bookings(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            query = """
                SELECT 
                    T1.BookID, T1.CustID, T1.CarID, T1.StartDate, T1.EndDate, T1.Status, 
                    CAST(JULIANDAY('now') - JULIANDAY(T1.EndDate) AS INTEGER) AS ExtraDays, 
                    (JULIANDAY('now') - JULIANDAY(T1.EndDate)) * T2.DailyRate AS ExtraCharge
                FROM 
                    SysBooking AS T1
                INNER JOIN 
                    SysCar AS T2 ON T1.CarID = T2.CarID
                WHERE 
                    T1.EndDate < DATE('now')
            """
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()
