from view.dashboards.DashboardView import *
from view.panels.Delivery_Panel import Delivery_panel


class Delivery_dashboard():
    def __init__(self):

        self.window = Tk()
        self.window.geometry("540x900")

        Label(self.window, text="Delivery PANEL", font=("Times New Roman", 40, "italic"), fg="Black").place(x=30, y=70)

        btn1 = Button(self.window, text="deliveries", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.delivery_panel)
        btn1.place(x=20, y=200, width=200, height=40)

    def delivery_panel(self):
        Delivery_panel()

