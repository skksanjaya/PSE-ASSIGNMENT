from database import create_connection
import sqlite3

class SysPayment():
     # Add record 
    def add_payment(self, BookID, Amount, Status, CreatedBy):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO SysPayment (BookID, Amount, Status, CreatedBy) VALUES (?, ?, ?, ?)",
                (BookID, Amount, Status, CreatedBy)
            )
            conn.commit()
            print("Payment added and sent!")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Update Record
    def update_status(self, PayID, Status):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE SysPayment SET Status = ? WHERE PayID = ?",
                (Status, PayID)
            )
            conn.commit()
            print("Updated successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Vew record from ID
    def view_payments_by_user_id(self, logged_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            query = """
                SELECT 
                    T1.PayID, T1.BookID, T1.Amount, T1.Status, T1.CreatedBy,
                    T2.CarID, T2.StartDate, T2.EndDate
                FROM 
                    SysPayment AS T1
                JOIN 
                    SysBooking AS T2
                ON 
                    T1.BookID = T2.BookID
                WHERE 
                    T2.CreatedBy = ?
            """
            cursor.execute(query, (logged_id,))
            payments = cursor.fetchall()
            return payments
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()        