from database import create_connection
import sqlite3

class SysUser():
    # Add record 
    def add_user(self,Name, Address,Email,RoleID,PasswordHash,Phone):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO SysUser (Name, Address,Email,RoleID,PasswordHash,Phone) VALUES (?, ?,?, ?,?, ?)",
                (Name, Address,Email,RoleID,PasswordHash,Phone)
            )
            conn.commit()
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
        finally:
            conn.close()
    # Check Record found
    def check_user_exists(self, Email):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT 1 FROM SysUser WHERE Email = ?", (Email,))
            if cursor.fetchone():
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return False
        finally:
            conn.close()
    # Get record by ID
    def get_user_by_email(self, Email):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT UserID, PasswordHash, RoleID FROM SysUser WHERE Email = ?", (Email,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"SQL error: {e}")
            return None
        finally:
            conn.close()