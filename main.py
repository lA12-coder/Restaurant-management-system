from user_authentication.user_management import UserManager
import tkinter as tk
from tkinter import messagebox, simpledialog

class RestaurantApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant management system")
        #screen_width= self.root.winfo_screenwidth()
       # screen_height = self.root.winfo_screenheight()
        #self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.geometry('800x400')
        self.user_manager=UserManager()
        self.create_widget()
        self.root.configure(bg='light blue')
        #self.restaurant = Restaurant("My Restaurant")

    def create_widget(self):
        #let us create he ui element here
        self.label=tk.Label(self.root,text='Welcome to Ethiel Restaurant Management system',bg='light blue')
        self.label.pack()
        # Adding the login button
        self.login_button=tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(padx=20,pady=10,)
        # Adding the register button
        self.register_button=tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack(padx=20, pady=10)

    def login(self):
        # Prompt the use to enter their username
        username=simpledialog.askstring("Login", "Enter username")
        password = simpledialog.askstring("Login", "Enter password", show='*')
        if self.user_manager.authenticate_user(username,password):
            messagebox.showerror("Login","Login failed. Check your user name and password. ")

    def register(self):
        username=simpledialog.askstring("Register", "Enter username")
        password= simpledialog.askstring("Register", "Enter password" , show='*')
        if self.user_manager.register_user(username,password):
            messagebox.showinfo("Register", "User registered successfully")


# main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()






