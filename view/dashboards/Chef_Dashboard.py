from  view.dashboards.DashboardView import *
from view.panels.Order_Panel import  Order_panel
from view.panels.Menu_Panel import  Menu
from view.panels.Inventory_Management_Panel import Inventory_management

class chef_dashboard():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("540x900")
        self.window.title("Chef Dashboard")

        Label(self.window, text="CHEF PANEL", font=("Times New Roman", 40, "italic"), fg="Black").place(x=30, y=70)

        btn1 = Button(self.window, text="Orders", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.orders)
        btn1.place(x=20, y=200, width=200, height=40)

        btn2 = Button(self.window, text="menu", width=8, font=("Arial", 14), bg="DodgerBlue4", command=self.menu)
        btn2.place(x=20, y=250, width=200, height=40)

        btn3=Button(self.window, text="inventory", width=8, font=("Arial", 14), bg="DodgerBlue4", command=self.inventory_management)
        btn3.place(x=20, y=300, width=200, height=40)

        self.window.mainloop()

    def orders(self):
        Order_panel()

    def menu(self):
        Menu()

    def inventory_management(self):
        Inventory_management()
