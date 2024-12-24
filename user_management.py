from user import User
import json

class AuthManager:
    def __init__(self,filename):
        self.filename=filename

    def register(self, username, password):
        users = User.load_users_from_file(self.filename)
        if any(user.userName == username  for user in users):
            print("User name already exists. Please choose another")
            return  False
        new_user = User(username, password)
        new_user.write_to_file(self.filename)
        print("Registration successful!")
        return True

    def login(self, username, password):
        users = User.load_users_from_file(self.filename)
        for user in users:
            if user.userName == username:
                if user.check_password(password):
                    print("Login successful!")
                    return True
                else:
                    print("Incorrect password.")
                    return False
        print("Username not found.")
        return False

    def change_password(self, username, old_password, new_password):
        users = User.load_users_from_file(self.filename)
        for user in users:
            if user.userName == username:
                if user.check_password(old_password):
                    user.password_hash = user.hash_password(new_password)  # Update password hash
                    self.save_all_users(users)  # Save all users back to the file
                    print("Password changed successfully!")
                    return True
                else:
                    print("Old password is incorrect.")
                    return False
        print("Username not found.")
        return False

    def save_all_users(self, users):
        with open(self.filename, 'w') as file:
            for user in users:
                user_data = {"username": user.userName, 'password_hash': user.password_hash}
                file.write(json.dumps(user_data) + "\n")