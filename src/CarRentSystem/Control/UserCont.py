from DAL.UserDAO import SysUser
from passlib.context import CryptContext

import io, contextlib



class UserService:
    # Create CryptContext once 
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self):
        self.user = SysUser()

    def add_user(self, Name, Address, Email, RoleID, Password, Phone):

        # Silence passlib/bcrypt stderr noise if needed
        with contextlib.redirect_stderr(io.StringIO()):
            hashed_password = self._pwd_context.hash(Password)
        self.user.add_user(Name, Address, Email, RoleID, hashed_password, Phone)

    def user_exists(self, Email):
        return self.user.check_user_exists(Email)

    def login(self, Email, Password):
        user_data = self.user.get_user_by_email(Email)
        if not user_data:
            print("User with that email does not exist.")
            return None

        user_id, stored_password_hash, role_id = user_data
        # Verify password (quietly ignore bcrypt warnings in frozen apps)
        with contextlib.redirect_stderr(io.StringIO()):
            valid = self._pwd_context.verify(Password, stored_password_hash)
        if valid:
            print("Login successful!")
            return f"{user_id}|{role_id}"
        else:
            print("Incorrect password.")
            return None
