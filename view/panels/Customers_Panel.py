from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from model.customer import Customer
from controller.customer_controller import Customer_Controller
from model.session import *


class Customer_panel(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("customer panel")
        self.window.geometry("760x470")
        self.window.configure(background="#d9d9d9")

        self.id = LabelWithEntry(self.window, "ID", 20, 20, state="readonly")
        self.first_name = LabelWithEntry(self.window, "First_Name ", 20, 60)
        self.last_name = LabelWithEntry(self.window, "Last_Name", 20, 100, data_type=IntVar)
        self.phone_number = LabelWithEntry(self.window, "Phone_Number", 20, 140, data_type=IntVar)
        self.order_id = LabelWithEntry(self.window, "Order_Id", 20, 180)

        self.table = Table(self.window,
                           ["ID", "First_Name ", "Last_Name", "Phone_Number", "Order_Id"],
                           [40, 100, 100, 100, 100],
                           270, 20,
                           16,
                           self.select_from_table)

        Button(self.window, text="Select customer", width=19,bg="DodgerBlue4" ,command=self.select_customer).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Customer_Controller.save(self.first_name.get(), self.last_name.get(), self.phone_number.get(),
                                                   self.order_id.get())
        if status:
            messagebox.showinfo("customer Save", message)
            self.reset_form()
        else:
            messagebox.showerror("customer Save Error", message)

    def edit_click(self):
        status, message = Customer_Controller.update(self.first_name, self.last_name.get(), self.phone_number.get(),
                                                     self.order_id.get())
        if status:
            messagebox.showinfo("customer update", message)
            self.reset_form()
        else:
            messagebox.showerror("customer update Error", message)

    def delete_click(self):
        status, message = Customer_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("customer Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("customer Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.phone_number.clear()
        self.order_id.clear()

        status, customer_list = Customer_Controller.get_all()
        self.table.refresh_table(customer_list)

    def select_from_table(self, selected_customer):
        if selected_customer:
            status, customer = Customer_Controller.find_by_id(selected_customer[0])
            if status:
                customer = Customer(*selected_customer)
                self.id.set(customer.id)
                self.first_name.set(customer.first_name)
                self.last_name.set(customer.last_name)
                self.phone_number.set(customer.phone_number)
                self.order_id.set(customer.order_id)

    def select_customer(self):
        if self.id.get():
            status, Session.customer = Customer_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select customer")

    def refresh(self):
        pass
