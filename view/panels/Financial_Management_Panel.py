from  view.dashboards.DashboardView import *
class Financial_management():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("540x900")
        self.window.title("Chef Dashboard")
        btn1 = Button(self.window, text="payments", width=8, font=("Arial", 14), bg="DodgerBlue4",
                      command=self.employee_managerpanel)
        btn1.place(x=20, y=150, width=200, height=40)

        btn2 = Button(self.window, text="total sales", width=8, font=("Arial", 14), bg="DodgerBlue4", command=self.menu)
        btn2.place(x=20, y=200, width=200, height=40)

        btn3 = Button(self.window, text="net income", width=8, font=("Arial", 12), bg="DodgerBlue4",
                      command=self.financial_management)
        btn3.place(x=20, y=250, width=200, height=40)
0
