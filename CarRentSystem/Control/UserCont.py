from DAL.UserDAO import SysUser
from passlib.context import CryptContext

class UserService():
    def __init__(self):
        self.user = SysUser() 
    # Call Record Add function    
    def add_user(self,Name, Address,Email,RoleID,PasswordHash,Phone):

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
        hashed_password = pwd_context.hash(PasswordHash);
        self.user.add_user(Name, Address,Email,RoleID,hashed_password,Phone);
    # Call Record found function
    def user_exists(self, Email):        
        return self.user.check_user_exists(Email)
    # Authentication
    def login(self, Email, Password):
        user_data = self.user.get_user_by_email(Email)

        if user_data:
            user_id, stored_password_hash, role_id = user_data
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
            if pwd_context.verify(Password, stored_password_hash):
                print("Login successful!")
                sessionData=str(user_id)+"|"+str(role_id);
                return sessionData
            else:
                print("Incorrect password.")
                return None
        else:
            print("User with that email does not exist.")
            return None
