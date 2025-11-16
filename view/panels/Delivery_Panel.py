from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from model.delivery import Delivery
from controller.delivery_controller import Delivery_Controller
from model.session import *


class Delivery_panel(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("delivery panel")
        self.window.geometry("760x470")
        self.window.configure(background="#d9d9d9")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.order_id = LabelWithEntry(self.window, "Order ID", 20, 60)
        self.rider = LabelWithEntry(self.window, "Rider", 20, 100, data_type=IntVar)
        self.status = LabelWithEntry(self.window, "Status", 20, 140, data_type=IntVar)
        self.address = LabelWithEntry(self.window, "Address", 20, 180)

        self.table = Table(self.window,
                           ["Id", "Order ID", "Rider", "Status", "Address"],
                           [40, 100, 100, 60, 100],
                           270, 20,
                           16,
                           self.select_from_table)

        Button(self.window, text="Select delivery", width=19, command=self.select_delivery).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Delivery_Controller.save(self.order_id.get(), self.rider.get(),self.status.get(),self.address.get())
        if status:
            messagebox.showinfo("delivery Save", message)
            self.reset_form()
        else:
            messagebox.showerror("delivery Save Error", message)

    def edit_click(self):
        status, message = Delivery_Controller.update(self.id.get(), self.order_id.get(),self.rider.get(), self.status.get(), self.address.get())
        if status:
            messagebox.showinfo("delivery update", message)
            self.reset_form()
        else:
            messagebox.showerror("delivery update Error", message)

    def delete_click(self):
        status, message = Delivery_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("delivery Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("delivery Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.order_id.clear()
        self.rider.clear()
        self.status.clear()
        self.address.clear()


        status, delivery_list = Delivery_Controller.get_all()
        self.table.refresh_table(delivery_list)

    def select_from_table(self, selected_delivery):
        if selected_delivery:
            status, delivery = Delivery_Controller.find_by_id(selected_delivery[0])
            if status:
                delivery = Delivery(*selected_delivery)
                self.id.set(delivery.id)
                self.order_id.set(delivery.order_id)
                self.status.set(delivery.status)
                self.address.set(delivery.address)



    def select_delivery(self):
        if self.id.get():
            status, Session.delivery = Delivery_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select delivery")

    def refresh(self):
        pass
