from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from controller.employee_controller import Employee_Controller
from model.session import *
from model.employee import Employee

class Employee_manager(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("Employee Managerpanel")
        self.window.geometry("1060x540")
        self.window.configure(background="AntiqueWhite1")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.role = LabelWithEntry(self.window, "Role", 20, 140)
        self.username = LabelWithEntry(self.window, "Username", 20, 180)
        self.password = LabelWithEntry(self.window, "Password", 20, 220)
        self.salary = LabelWithEntry(self.window, "Salary", 20, 260, data_type=IntVar)
        self.phone_number = LabelWithEntry(self.window, "Phone_number", 20, 300)

        self.search_role = LabelWithEntry(self.window, "Role", 300, 20, distance=50,
                                          on_keypress_function=self.search_role)

        self.table = Table(self.window,
                           ["Id", "FirstName", "LastName", "Role", "Username", "Password", "Salary", "Phone_number"],
                           [40, 100, 100, 60, 100, 100, 100, 100, 60],
                           300, 50,
                           16,
                           self.select_from_table)


        Button(self.window, text="Refresh", width=7,bg="#97C6E0", font=("Arial", 14) , command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7,bg="#97C6E0" , font=("Arial", 14), command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7,bg="#97C6E0" , font=("Arial", 14), command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7,bg="#97C6E0", font=("Arial", 14) , command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Employee_Controller.save(self.first_name.get(), self.last_name.get(), self.role.get(),
                                                   self.username.get(),
                                                   self.password.get(), self.salary.get(), self.phone_number.get())
        if status:
            messagebox.showinfo("Employee Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Save Error", message)

    def edit_click(self):
        status, message = Employee_Controller.update(self.id.get(), self.first_name.get(),
                                                     self.last_name.get(),
                                                     self.role.get(), self.username.get(), self.password.get(),
                                                     self.salary.get(), self.phone_number.get(), )
        if status:
            messagebox.showinfo("Employee update", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee update Error", message)

    def delete_click(self):
        status, message = Employee_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Employee Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.role.clear()
        self.username.clear()
        self.password.clear()
        self.salary.clear()
        self.phone_number.clear()

        status, employee_list = Employee_Controller.get_all()
        self.table.refresh_table(employee_list)

    def select_from_table(self, selected_employee):
        if selected_employee:
            status, employee = Employee_Controller.find_by_id(selected_employee[0])
            if status:
                employee =Employee(*selected_employee)
                self.id.set(employee.id)
                self.first_name.set(employee.first_name)
                self.last_name.set(employee.last_name)
                self.role.set(employee.role)
                self.salary.set(employee.salary)
                self.username.set(employee.username)
                self.password.set(employee.password)

                self.phone_number.set(employee.phone_number)

    def select_employee(self):
        if self.id.get():
            status, Session.employee = Employee_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select Employee")

    def refresh(self):
        pass
    def search_role(self):
         status, employee_list = Employee_Controller.find_by_role(self.search_role.get())
         if status and employee_list:
                self.table.refresh_table(employee_list)

