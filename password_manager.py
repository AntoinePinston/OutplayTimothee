'''
This file contains the PasswordManager class which manages the passwords.
'''
import json
class PasswordManager:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()
    def create_account(self, username, password):
        if username in self.accounts:
            return False
        self.accounts[username] = password
        self.save_accounts()
        return True
    def login(self, username, password):
        if username in self.accounts and self.accounts[username] == password:
            return True
        return False
    def add_password(self, website, password):
        self.accounts[website] = password
        self.save_accounts()
        return True
    def retrieve_password(self, website):
        return self.accounts.get(website)
    def save_accounts(self):
        with open("accounts.json", "w") as file:
            json.dump(self.accounts, file)
    def load_accounts(self):
        try:
            with open("accounts.json", "r") as file:
                self.accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}