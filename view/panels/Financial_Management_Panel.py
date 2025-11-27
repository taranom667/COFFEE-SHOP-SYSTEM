from view.dashboards.DashboardView import *
from view.panels.Payment_Panel import *
from model.order import  Order
from repository.order_repository import *
from controller.order_controller import Order_Controller
from model.order import Order
class Financial_management():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("540x900")
        self.window.title("Financial_management")
        btn1 = Button(self.window, text="payments", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.payment)
        btn1.place(x=20, y=150, width=200, height=40)

        btn2 = Button(self.window, text="total sales", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.total_sales)
        btn2.place(x=20, y=200, width=200, height=40)

        btn3 = Button(self.window, text="net income", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.get_income)
        btn3.place(x=20, y=250, width=200, height=40)

    def payment(self):
        Payment_panel()

    def total_sales(self):
        data=Order_Controller.get_all()
        total=sum(item["total_price"] for item in data[1])

        return print(total)


    def get_income(self):
        pass

