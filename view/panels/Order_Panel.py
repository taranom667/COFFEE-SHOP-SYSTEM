from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from model.order import Order
from controller.order_controller import Order_Controller
from model.session import *


class Order_panel(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("0rder")
        self.window.geometry("1060x520")
        self.window.configure(background="#d9d9d9")

        self.table = Table(self.window,
                           ["Id", "Customer Name", "dish", "Status", "Total Price", "Delivery ID", "Date Time"],
                           [40, 100, 120, 100, 100, 80, 100],
                           270, 20,
                           16,
                           self.select_from_table)
        # if dash_role == "chef":

        self.id = LabelWithEntry(self.window, "ID", 20, 20, state="readonly")
        self.customer_name = LabelWithEntry(self.window, "CustomerName", 20, 60)
        self.dish = LabelWithEntry(self.window, "dish", 20, 100)
        # self.dish.set(Session.dish)
        self.status = LabelWithEntry(self.window, "Status", 20, 140)

        self.total_price = LabelWithEntry(self.window, "Total Price", 20, 180, data_type=IntVar)
        self.delivery_id = LabelWithEntry(self.window, "Delivery ID", 20, 220, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "Date Time", 20, 260)

        Button(self.window, text="Select order", width=19, command=self.select_order).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Order_Controller.save(self.customer_name.get(), self.dish.get(), self.status.get(),
                                                self.total_price.get(), self.delivery_id.get(), self.date_time.get())
        if status:
            messagebox.showinfo("order Save", message)
            self.reset_form()
        else:
            messagebox.showerror("order Save Error", message)

    def edit_click(self):
        status, message = Order_Controller.update(self.id.get(), self.customer_name.get(), self.dish.get(),
                                                  self.status.get(),
                                                  self.total_price.get(), self.delivery_id.get(), self.date_time.get())
        if status:
            messagebox.showinfo("order update", message)
            self.reset_form()
        else:
            messagebox.showerror("order update Error", message)

    def delete_click(self):
        status, message = Order_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("order Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("order Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.customer_name.clear()
        self.dish.clear()
        self.status.set("")
        self.total_price.clear()
        self.delivery_id.clear()
        self.date_time.clear()

        status, order_list = Order_Controller.get_all()
        self.table.refresh_table(order_list)

    def select_from_table(self, selected_order):
        if selected_order:
            status, order = Order_Controller.find_by_id(selected_order[0])
            if status:
                order = Order(*selected_order)
                self.id.set(order.id)
                self.customer_name.set(order.customer_name)
                self.dish.set(order.dish)
                self.status.set(order.status)
                self.total_price.set(order.total_price)
                self.delivery_id.set(order.delivery_id)
                self.date_time.set(order.date_time)

    def select_order(self):
        if self.id.get():
            status, Session.order = Order_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select order")

    def refresh(self):
        pass


'''
        Label(self.window,text="status").place(x=20, y=140)

        self.status=StringVar()
        ttk.Combobox(self.window, textvariable=self.status, values=["confrimed", "processing", "in transit", "ready","delivered", "cancel"], width=17).place(x=110, y=140)
           '''
