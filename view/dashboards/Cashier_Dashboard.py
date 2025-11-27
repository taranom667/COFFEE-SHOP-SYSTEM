from view.dashboards.DashboardView import *
# from view.panels.sefarsh import Sefaresh
from view.panels.Order_Panel import Order_panel
from view.panels.Menu_Panel import Menu
from view.panels.Delivery_Panel import Delivery_panel
from model.session import Session


class cashier_dashboard():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("540x900")

        Label(self.window, text="Cashier PANEL", font=("Times New Roman", 40, "italic"), fg="Black").place(x=30, y=70)

        btn1 = Button(self.window, text="Orders", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.orders)
        btn1.place(x=20, y=200, width=200, height=40)

        btn2 = Button(self.window, text="menu", width=8, font=("Arial", 14), bg="DodgerBlue4", command=self.menu)
        btn2.place(x=20, y=250, width=200, height=40)

        btn3 = Button(self.window, text="deliveries", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.delivery_panel)
        btn3.place(x=20, y=300, width=200, height=40)

        btn4 = Button(self.window, text="sabt sefaresh", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.get_order)
        btn4.place(x=20, y=350, width=200, height=40)
        self.window.mainloop()

    def orders(self):
        Order_panel()

    def menu(self):
        Menu()

    def delivery_panel(self):
        Delivery_panel()

    def get_order(self):
        pass
        # Sefaresh()

