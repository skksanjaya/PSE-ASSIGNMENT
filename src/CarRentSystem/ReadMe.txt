# Car Rental Management System(CLI-Application) Version: 1.0.0.

+ Course : MSE800 Professional Software Engineering.

****************************************************************************************

This project has implmented for manage Customers, Cars, Bookings and Payments.
System has two main roles "Customer" and "Admin".
Users can launch system via "Source Code" and a "Windows executable"

****************************************************************************************

For Application Users
-----------------------

# 1) Software Features

** User Functions **
- Register and create user account for Customers
- Login to System and access menus relavant to user roles (both Customer and Admin)

** Car Functions ** (Admin)   
- Maintain car inventory. Add, Update, Delete Cars
- View list of all Cars

** Booking Cars ** (Customer)
- View list of all cars
- Create booking for selected car
- View approved bookings 
- View calculated Total amount of booking 
- Make payment for booking (** Note : There is no payment gateway to make payment. Only Assumption. Payment record update in SysPayment table.)

** Manage Rentals ** (Admin)
- Approve/Reject pendng bookings
- Calculate Payment amount and send it to user on booking approval ( Insert goes to payment table with Amount)
- Make payment for extra charges when required (** Note : There is no payment gateway to make extra payment. Only Assumption. Payment record insert to the SysCharge table.)

# 2) How to run application
- Go to "CarRentSystem/dist/"
- Double click on CarRental.exe

# 3) Quick user guide
-1. Register/Login
# New User -> Enter name, address, email, phone, password. User created.
# Login -> Login with email and password. Menu visible accoring to user role

-2. Customer Path
# View Cars
# Create Booking -> Enter start/end dates. created booking with pending status
# Make Payment -> View approved bookings. Make payment/confirm. booking became active status

-3. Admin Path
# Manage Cars -> Add/Update/Delete Cars
# Approve/Reject Bookings --> Calculate total amount and send it to customer via system record. 
# Apply extra charge -> Calculate and view extra amount. Customer can pay amount and then record into table. 



For Software Developers
-----------------------
+ Technologies Used : Python 3.8+ * SQLite * PyInstaller for Windows EXE * passlib==1.7.2 and bcrypt==3.2.2 for hash password.
+ Software Architecture : Model View Controller (MVC) architecture ( UI -> Controller -> DAO -> SQLite DB )

# 1) Folder Structure

CarRentSystem/
- main.py
- requirements.txt
- users.db
- database.py
  - Control/BookingCont.py
  - Control/CarCont.py
  - Control/ChargeCont.py
  - Control/PaymentCont.py
  - Control/UserCont.py 
  - DAL/BookingDAO.py
  - DAL/CarDAO.py
  - DAL/ChargeDAO.py
  - DAL/PaymentDAO.py
  - DAL/UserDAO.py
  - dist/CarRental.exe

# Main Folders/Files

- main.py — # Entry point to the system. CLI menus for registration/login, car browsing, booking, payments.
- database.py — # Creates tables on first run. Create automatically admin account, if admin account not exisist. Login for admin -> Email : admin@sysrent.com, Password : admin123. I registered customer for Testing. Email : john@gmail.com, Password : zxc   
- Control/ — # services/controllers file folder. Application business logic and validations include here.
  - UserCont.py # User registration, User login/Authentication , User Role allocation
  - CarCont.py  # view,add,update,delete cars
  - BookingCont.py # create,view,approve,reject,status transitions of bookings
  - PaymentCont.py # create payment records for bookings
  - ChargeCont.py  # create additional charge records for bookings 
- DAL/ — # Data access layer. Included CRUD operations using SQL for all tables with seperate file. DAO classes: UserDAO.py, CarDAO.py, BookingDAO.py, PaymentDAO.py, ChargeDAO.py).
- requirements.txt — Required python packages for installation.
- dist/CarRental.exe — Windows executable create here.

# 2) Data Tables (SQLite) 
- SysUser
- SysCar
- SysBooking
- SysPayment
- SysCharge

# 3) Naming Conventions
	
- Control folder - # Put "Cont" suffix at file name.
- DAL     folder - # Put "DAO"  suffix at file name.
- Table   Names  - # Put "Sys"  Prefix at table name. 

# 4) License
********************************************************************************
MIT License

Copyright (c) 2025 skksanjaya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Academic Notice

This repository is created for Academic Assessment:
  MSE800 – Professional Software Engineering (Yoobee College of Creative Innovation)
  Assessment 1 – Car Rental System
Scope:
  Code is licensed under MIT 


**********************************************************************************
Credits
-------
Author    : Kasun Sanjaya
Programme : Master of Software Engineering (Yoobee College of Creative Innovation)
Contact   : 270609649@yoobeestudent.ac.nz





