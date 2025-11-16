
from view import *
from view.panels.Employee_Manager_Panel import Employee_manager
from view.panels.Menu_Panel import Menu
from view.panels.Financial_Management_Panel import Financial_management
from view.panels.Inventory_Management_Panel import Inventory_management


class manager_dashboard():
    def __init__(self):
        self.window = Tk()
        self.window.title("manager panel")
        self.window.configure(bg="#efefef")
        self.window.geometry("400x400")

        Label(self.window, text="Management", font=("Times New Roman", 40, "italic"), fg="Black").place(x=30, y=70)

        btn1 = Button(self.window, text="Employees", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.employee_managerpanel)
        btn1.place(x=20, y=150, width=200, height=40)

        btn2 = Button(self.window, text="menu", width=8, font=("Arial", 14), bg="DodgerBlue4", command=self.menu)
        btn2.place(x=20, y=200, width=200, height=40)

        btn3 = Button(self.window, text="Financial_Managment", width=8, font=("Arial", 12), bg="DodgerBlue4",
                      command=self.financial_management)
        btn3.place(x=20, y=250, width=200, height=40)

        btn4 = Button(self.window, text="Inventory", width=8, font=("Arial", 12), bg="DodgerBlue4",
                      command=self.inventory_management)
        btn4.place(x=20, y=300, width=200, height=40)

    def employee_managerpanel(self):
        Employee_manager()

    def menu(self):
        Menu()

    def financial_management(self):
        Financial_management()

    def inventory_management(self):
        Inventory_management()
