from user_authentication.user import User

class UserManager:
    def __init__(self):
        self.users=[]
        # REGISTERING A NEW USER
    def register_user(self,username,password):
        # CHECK IF THE USER HAS ALREADY REGISTERED
        if any(user.userName==username for user in self.users):
            print("Username already exist")
            return False
        new_user=User(username,password)
        self.users.append(new_user)
        print("User registered successfully")
        return True
    def authenticate_user(self,username,password):
        for user in self.users:
            if user.userName==username and user.check_password(password):
                return  True
            return False






