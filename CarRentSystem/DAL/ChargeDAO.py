from database import create_connection
import sqlite3

class SysCharge():
     # Add record 
    def add_charge(self, BookID, Amount, CreatedBy):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO SysCharge (BookID, Amount, CreatedBy) VALUES (?, ?, ?)",
                (BookID, Amount, CreatedBy)
            )
            conn.commit()
            print("Added successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()

