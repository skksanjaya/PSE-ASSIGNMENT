import sqlite3
# from passlib.context import CryptContext

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
   
     # User Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SysUser (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Address TEXT,       
            Email TEXT NOT NULL UNIQUE,
            RoleID TEXT NOT NULL , --1-Admin,2-Cust
            PasswordHash TEXT NOT NULL,
            Phone TEXT,            
            CreatedDate TEXT DEFAULT (datetime('now'))
        )
    """)


    try:
        cursor.execute("SELECT COUNT(*) FROM SysUser WHERE RoleID = '1'")
        if cursor.fetchone()[0] == 0:
            #pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
            default_admin_password = hash("admin123");             
            cursor.execute(
                "INSERT INTO SysUser (Name, Address, Email, RoleID, PasswordHash, Phone) VALUES (?, ?, ?, ?, ?, ?)",
                ('Admin', 'N/A', 'admin@sysrent.com', '1', default_admin_password, 'N/A')
            )
            print("Default admin account created.")
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while creating the admin account: {e}")

    
 # Car Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SysCar (
            CarID INTEGER PRIMARY KEY AUTOINCREMENT,
            Make TEXT NOT NULL,
            Model TEXT NOT NULL,
            Year INTEGER NOT NULL,
            Mileage INTEGER DEFAULT 0,
            Available INTEGER NOT NULL DEFAULT 1,-- '1-available','2-maintainance'
            MinDays INTEGER NOT NULL DEFAULT 1,
            MaxDays INTEGER NOT NULL DEFAULT 30,
            DailyRate REAL NOT NULL,
            CreatedBy TEXT NOT NULL,       
            CreatedDate TEXT DEFAULT (datetime('now')),
            ModifiedBy TEXT,       
            ModifiedDate TEXT    

        )
    """)

# Booking Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SysBooking (
            BookID INTEGER PRIMARY KEY AUTOINCREMENT,
            CustID INTEGER NOT NULL,  
            CarID INTEGER NOT NULL,
            StartDate TEXT NOT NULL,      -- ISO 'YYYY-MM-DD'
            EndDate TEXT NOT NULL,
            Status TEXT NOT NULL , --'1-pending','2-approved','3-rejected','4-active','5-completed','6-cancelled'
            CreatedBy TEXT NOT NULL,       
            CreatedDate TEXT DEFAULT (datetime('now')),
            ApproveBy TEXT ,       
            ApproveDate TEXT,       
            FOREIGN KEY (CarID) REFERENCES Car(CarID) ON UPDATE CASCADE ON DELETE RESTRICT,
            FOREIGN KEY (CustID) REFERENCES User(UserID) ON UPDATE CASCADE ON DELETE RESTRICT
        )
    """)



    # Payment table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SysPayment (
            PayID INTEGER PRIMARY KEY AUTOINCREMENT,
            BookID INTEGER NOT NULL,
            Amount REAL NOT NULL,
            Status TEXT NOT NULL, --'1-Pending, 2-Complte'
            CreatedBy TEXT NOT NULL,       
            CreatedDate TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (BookID) REFERENCES Booking(BookID) ON UPDATE CASCADE ON DELETE CASCADE
        )
    """)

    # ExtraCharge Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SysCharge (
            ChargeID INTEGER PRIMARY KEY AUTOINCREMENT,
            BookID INTEGER NOT NULL,
            Amount REAL NOT NULL,
            CreatedBy TEXT NOT NULL,       
            CreatedDate TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (BookID) REFERENCES Booking(BookID) ON UPDATE CASCADE ON DELETE CASCADE
        )
    """)


    
    conn.commit()
    conn.close()
