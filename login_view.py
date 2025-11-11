from  tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from view import *
from view.component.label_with_entry import LabelWithEntry
from controller.employee_controller import Employee_Controller
from model.session import Session
from view.dashboards.Chef_Dashboard import chef_dashboard
from view.dashboards.Manager_Dashboard import manager_dashboard
from  view.dashboards.Waiter_Dashboaard import waiter_dashboard
from  view.dashboards.Cashier_Dashboard import cashier_dashboard
from  view.dashboards.Courier_Dashboard import courier_dashboard

class LoginView:
    def __init__(self):
        self.employee_controller = Employee_Controller()
        self.window =Tk()
        self.window.title("COFFEE SHOP LOGIN")
        self.window.configure(background="#efefef")
        self.window.geometry("700x700")

        img = Image.open("./view/images/pic2.png")
        pic2 = ImageTk.PhotoImage(img)
        Label(self.window, image=pic2).place(x=20, y=20)

        self.username = LabelWithEntry(self.window, "Username", 400, 300)
        self.password = LabelWithEntry(self.window, "Password", 400, 350)


        Button(self.window, text="Login", width=8, font=("Arial", 14), command=self.login).place(x=490, y=400,
                                                                                                 width=100,
                                                                                                 height=35)

        self.window.mainloop()

    def login(self):
        status, employee = self.employee_controller.find_by_username_and_password(self.username.get(),
                                                                                  self.password.get())

        if status:
            self.window.destroy()
            Session.employee = employee
            dash_role=Session.employee.role
            if dash_role == "chef":
                chef_dashboard()
            elif dash_role == "manager":
                manager_dashboard()
            elif dash_role == "cashier":
                cashier_dashboard()
            elif dash_role == "manager":
                courier_dashboard()
            elif dash_role == "waiter":
                waiter_dashboard()


        else:
            messagebox.showerror("Login Error", "Access Denied !!!")
