'''
This is the main file of the password manager application.
'''
from tkinter import Tk
from password_manager_app import PasswordManagerApp
def main():
    root = Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()