'''
This file contains the PasswordManagerApp class which represents the password manager application.
'''
from tkinter import Tk, Label, Entry, Button, messagebox
from password_manager import PasswordManager
class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.password_manager = PasswordManager()
        self.create_account_label = Label(self.root, text="Create Account")
        self.create_account_label.pack()
        self.username_label = Label(self.root, text="Username")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()
        self.password_label = Label(self.root, text="Password")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()
        self.create_account_button = Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()
        self.login_label = Label(self.root, text="Login")
        self.login_label.pack()
        self.login_username_label = Label(self.root, text="Username")
        self.login_username_label.pack()
        self.login_username_entry = Entry(self.root)
        self.login_username_entry.pack()
        self.login_password_label = Label(self.root, text="Password")
        self.login_password_label.pack()
        self.login_password_entry = Entry(self.root, show="*")
        self.login_password_entry.pack()
        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack()
        self.add_password_label = Label(self.root, text="Add Password")
        self.add_password_label.pack()
        self.website_label = Label(self.root, text="Website")
        self.website_label.pack()
        self.website_entry = Entry(self.root)
        self.website_entry.pack()
        self.password_label = Label(self.root, text="Password")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()
        self.add_password_button = Button(self.root, text="Add Password", command=self.add_password)
        self.add_password_button.pack()
        self.retrieve_password_label = Label(self.root, text="Retrieve Password")
        self.retrieve_password_label.pack()
        self.retrieve_website_label = Label(self.root, text="Website")
        self.retrieve_website_label.pack()
        self.retrieve_website_entry = Entry(self.root)
        self.retrieve_website_entry.pack()
        self.retrieve_password_button = Button(self.root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_password_button.pack()
        self.password_manager.load_accounts()
    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.password_manager.create_account(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Failed to create account.")
    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if self.password_manager.login(username, password):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    def add_password(self):
        website = self.website_entry.get()
        password = self.password_entry.get()
        if self.password_manager.add_password(website, password):
            messagebox.showinfo("Success", "Password added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add password.")
    def retrieve_password(self):
        website = self.retrieve_website_entry.get()
        password = self.password_manager.retrieve_password(website)
        if password:
            messagebox.showinfo("Success", f"Password for {website}: {password}")
        else:
            messagebox.showerror("Error", "Failed to retrieve password.")