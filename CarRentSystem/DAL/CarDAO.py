from database import create_connection
import sqlite3

class SysCar():
    # View List
    def view_cars(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM SysCar")
            cars = cursor.fetchall()
            return cars
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()
     # Add record 
    def add_car(self, Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO SysCar (Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (Make, Model, Year, Mileage, Available, MinDays, MaxDays, DailyRate, CreatedBy)
            )
            conn.commit()
            print("Added successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Update Record
    def update_car(self, CarID, Make=None, Model=None, Year=None, Mileage=None, Available=None, MinDays=None, MaxDays=None, DailyRate=None, ModifiedBy=None):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            query = "UPDATE SysCar SET ModifiedBy = ?, ModifiedDate = datetime('now')"
            params = [ModifiedBy]

            if Make is not None:
                query += ", Make = ?"
                params.append(Make)
            if Model is not None:
                query += ", Model = ?"
                params.append(Model)
            if Year is not None:
                query += ", Year = ?"
                params.append(Year)
            if Mileage is not None:
                query += ", Mileage = ?"
                params.append(Mileage)
            if Available is not None:
                query += ", Available = ?"
                params.append(Available)
            if MinDays is not None:
                query += ", MinDays = ?"
                params.append(MinDays)
            if MaxDays is not None:
                query += ", MaxDays = ?"
                params.append(MaxDays)
            if DailyRate is not None:
                query += ", DailyRate = ?"
                params.append(DailyRate)

            query += " WHERE CarID = ?"
            params.append(CarID)

            cursor.execute(query, tuple(params))
            conn.commit()
            print("Updated successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Delete Record
    def delete_car(self, CarID):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM SysCar WHERE CarID = ?", (CarID,))
            conn.commit()
            print("Deleted successfully.")
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()