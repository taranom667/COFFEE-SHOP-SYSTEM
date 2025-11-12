from  view.dashboards.DashboardView import *
class manager_dashboard():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x700")
        self.window.title("manager panel")
        self.window.configure(bg="#efefef")
        self.window.geometry("700x700")

        Label(self.window, text="Management", font=("Times New Roman", 40, "italic"), fg="Black").place(x=30, y=70)

        Button(self.window, text="Employees", width=8, font=("Arial", 14), bg="DodgerBlue4").place(
            x=140, y=300,
            width=100,
            height=35

        Button(self.window, text="menu", width=8, font=("Arial", 14), bg="DodgerBlue4").place(
            x=140, y=300,
            width=100,
            height=35)

        Button(self.window, text="inventory", width=8, font=("Arial", 14), bg="DodgerBlue4").place(
            x=140, y=300,
            width=100,
            height=35)

        Button(self.window, text="Financial_Managment", width=8, font=("Arial", 14), bg="DodgerBlue4").place(
            x=140, y=300,
            width=100,
            height=35)

        Button(self.window, text="", width=8, font=("Arial", 14), bg="DodgerBlue4").place(
            x=140, y=300,
            width=100,
            height=35)
        self.window.mainloop()