import tkinter as tk
from tkinter import *

from PIL import ImageTk,Image
from view import *

from view import DashboardView
from view.component.label_with_entry import LabelWithEntry
from controller.employee_controller import Employee_Controller
from model.session import Session


class LoginView:
    def __init__(self):
        self.employee_controller = Employee_Controller()
        self.window = Tk()
        self.window.title("COFFEE SHOP LOGIN")
        self.window.configure(background="#efefef")
        self.window.geometry("700x700")

        img = Image.open("./view/images/pic2.png")
        img = ImageTk.PhotoImage(img)
        Label(self.window, image=img).place(x=20, y=20)

        self.username = LabelWithEntry(self.window, "Username", 400, 100, )
        self.password = LabelWithEntry(self.window, "Password", 400, 150)

        self.username.set("tari")
        self.password.set("slriuhf")
        self.window.mainloop()
        '''
        Button(self.window, text="Login", width=8, font=("Arial", 14), command=self.login).place(x=50, y=380, width=200,
                                                                                                 height=70)

        

    def login(self):
        status, employee = self.employee_controller.find_by_username_and_password(self.username.get(),
                                                                                  self.password.get())

        if status:
            self.window.destroy()
            Session.employee = employee
            DashboardView()
        else:
            messagebox.showerror("Login Error", "Access Denied !!!")
'''