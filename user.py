import hashlib
import json
import os


class User:
    def __init__(self,username,password):
        self.userName= username
        self.password_hash= self.hash_password(password)
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    def check_password(self,password):
        return self.password_hash==self.hash_password(password)
    def write_to_file(self,filename):
        user_Data={"username":self.userName,'password_hash':self.password_hash}
        #Append the user data to the file
        with open(filename,'a') as file:
            file.write(json.dumps(user_Data) +"\n")
    @staticmethod
    def load_users_from_file(filename):
        users=[]
        if not os.path.exists(filename):
            return users
        try:

            with open(filename,'r') as file:
                for line in file:
                    user_data  = json.loads(line.strip())
                    user = User(user_data['username'],'')
                    user.password_hash = user_data['password_hash']
                    users.append(user)
            return users
        except(json.JSONDecodeError, KeyError) as e:
            print(f"Error reading file {filename}:{e}")


