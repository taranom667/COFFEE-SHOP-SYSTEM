from view.component.label_with_entry import LabelWithEntry
from view import *
from controller.raw_material_controller import Raw_material_Controller
from rich.panel import Panel
from model.session import *
from tkinter import *
from tkinter import messagebox

class Inventory_management(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("Inventory")
        self.window.geometry("1260x620")
        self.window.configure(background="#d9d9d9")

        self.table = Table(self.window,
                           ["Id", "Name", "Category", "Unit", "Quantity ", "Price", "Purchase_date", "Expiry_date",
                            "Location"],
                           [40, 100, 120, 100, 100, 80, 100, 100, 100],
                           270, 20,
                           16,
                           self.select_from_table)

        self.id = LabelWithEntry(self.window, "ID", 20, 20, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.category = LabelWithEntry(self.window, "Category", 20, 100)
        self.unit = LabelWithEntry(self.window, "Unit", 20, 140)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 180, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 220, data_type=IntVar)
        self.purchase_date = LabelWithEntry(self.window, "Purchase_date", 20, 260)
        self.expiry_date = LabelWithEntry(self.window, "Expiry_date", 20, 300)
        self.location = LabelWithEntry(self.window, "Location", 20, 340)

        Button(self.window, text="Select  Raw_material", width=19, command=self.select_from_table).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Raw_material_Controller.save(self.name.get(), self.category.get(), self.unit.get(),
                                                       self.quantity.get(), self.price.get(), self.purchase_date.get(),
                                                       self.expiry_date.get(), self.location.get())
        if status:
            messagebox.showinfo(" Raw_material Save", message)
            self.reset_form()
        else:
            messagebox.showerror(" Raw_material Save Error", message)

    def edit_click(self):
        status, message = Raw_material_Controller.update(self.id.get(), self.name.get(), self.category.get(),
                                                         self.unit.get(),
                                                         self.quantity.get(), self.price.get(),
                                                         self.purchase_date.get(),
                                                         self.expiry_date.get(), self.location.get())
        if status:
            messagebox.showinfo(" Raw_material update", message)
            self.reset_form()
        else:
            messagebox.showerror(" Raw_material update Error", message)

    def delete_click(self):
        status, message = Raw_material_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo(" Raw_material Delete", message)
            self.reset_form()
        else:
            messagebox.showerror(" Raw_material Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.name.clear()
        self.category.clear()
        self.unit.clear()
        self.quantity.clear()
        self.price.clear()
        self.purchase_date.clear()
        self.expiry_date.clear()
        self.location.clear()

        status, Raw_material_list = Raw_material_Controller.get_all()
        self.table.refresh_table(Raw_material_list)

    def select_from_table(self, selected_Raw_material):
        if selected_Raw_material:
            status, Raw_material = Raw_material_Controller.find_by_id(selected_Raw_material[0])
            if status:
                Raw_material = Raw_material(*selected_Raw_material)
                self.id.set(Raw_material.id)
                self.name.set(Raw_material.customer_name)
                self.category.set(Raw_material.dish)
                self.unit.set(Raw_material.status)
                self.quantity.set(Raw_material.total_price)
                self.price.set(Raw_material.delivery_id)
                self.purchase_date.set(Raw_material.date_time)
                self.expiry_date.set(Raw_material.expiry_date)
                self.location.set(Raw_material.location)

    def select_Raw_material(self):
        if self.id.get():
            status, Session.Raw_material = Raw_material_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select  Raw_material")

    def refresh(self):
        pass

