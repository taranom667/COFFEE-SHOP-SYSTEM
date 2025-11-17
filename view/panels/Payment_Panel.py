from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from model.payment import Payment
from controller.payment_controller import Payment_Controller
from model.session import *


class Payment_panel(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("payment_panel")
        self.window.geometry("1360x470")
        self.window.configure(background="#d9d9d9")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.order_id = LabelWithEntry(self.window, "order_id", 20, 60)
        self.total_price = LabelWithEntry(self.window, "total_price", 20, 100, data_type=IntVar)
        self.payment_type = LabelWithEntry(self.window, "payment_type", 20, 140, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "date_time", 20, 180)
        self.customer_id = LabelWithEntry(self.window, "customer_id", 20, 220, data_type=BooleanVar)
        self.status = LabelWithEntry(self.window, "status", 20, 260)
        self.factor_id = LabelWithEntry(self.window, "factor_id", 20, 300)

        self.table = Table(self.window,
                           ["Id", "order_id", "total_price", "payment_type", "date_time", "customer_id", "status","factor_id"],
                           [40, 100, 100, 60, 100, 100, 100, 100],
                           270, 20,
                           16,
                           self.select_from_table)

        Button(self.window, text="Select payment", width=19, command=self.select_payment).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Payment_Controller.save(self.order_id.get(), self.total_price.get(), self.payment_type.get(),
                                                  self.date_time.get(), self.customer_id.get(), self.status.get(),
                                                  self.factor_id.get())
        if status:
            messagebox.showinfo("payment Save", message)
            self.reset_form()
        else:
            messagebox.showerror("payment Save Error", message)

    def edit_click(self):
        status, message = Payment_Controller.update(self.id.get(), self.order_id.get(), self.total_price.get(), self.payment_type.get(),
                                                  self.date_time.get(), self.customer_id.get(), self.status.get(),
                                                  self.factor_id.get())
        if status:
            messagebox.showinfo("payment update", message)
            self.reset_form()
        else:
            messagebox.showerror("payment update Error", message)

    def delete_click(self):
        status, message = Payment_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("payment Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("payment Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.order_id.clear()
        self.total_price.clear()
        self.payment_type.clear()
        self.date_time.clear()
        self.customer_id.clear()
        self.status.clear()
        self.factor_id.clear()


        status, payment_list = Payment_Controller.get_all()
        self.table.refresh_table(payment_list)

    def select_from_table(self, selected_payment):
        if selected_payment:
            status, payment = Payment_Controller.find_by_id(selected_payment[0])
            if status:
                payment = Payment(*selected_payment)
                self.id.set(payment.id)
                self.order_id.set(payment.order_id)
                self.total_price.set(payment.total_price)
                self.payment_type.set(payment.payment_type)
                self.date_time.set(payment.date_time)
                self.customer_id.set(payment.customer_id)
                self.status.set(payment.status)
                self.factor_id.set(payment.factor_id)

    def select_payment(self):
        if self.id.get():
            status, Session.payment = Payment_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select payment")

    def refresh(self):
        pass
