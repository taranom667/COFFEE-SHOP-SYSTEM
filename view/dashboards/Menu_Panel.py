from rich.panel import Panel
from view.component.label_with_entry import LabelWithEntry
from view import *
from model.dish import Dish
from controller.dish_controller import Dish_Controller
from model.session import *


class Menu(Panel):
    def __init__(self):
        self.window = Tk()
        self.window.title("menu")
        self.window.geometry("1060x440")
        self.window.configure(background="#d9d9d9")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 100, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 140, data_type=IntVar)
        self.category = LabelWithEntry(self.window, "Category", 20, 180)
        self.available = LabelWithEntry(self.window, "Available", 20, 220, data_type=BooleanVar)
        self.ingredients = LabelWithEntry(self.window, "Ingredients", 20, 260)

        self.table = Table(self.window,
                           ["Id", "Name", "Quantity", "Price", "Category", "Available", "Ingredients"],
                           [40, 100, 100, 60, 100, 100, 100, 100, 60],
                           270, 20,
                           16,
                           self.select_from_table)

        Button(self.window, text="Select dish", width=19, command=self.select_dish).place(x=20, y=380)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=380)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=420)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=420)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=420)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = Dish_Controller.save(self.name.get(), self.quantity.get(), self.price.get(),
                                               self.category.get(),
                                               self.available.get(), self.ingredients.get())
        if status:
            messagebox.showinfo("dish Save", message)
            self.reset_form()
        else:
            messagebox.showerror("dish Save Error", message)

    def edit_click(self):
        status, message = Dish_Controller.update(self.id.get(), self.name.get(), self.quantity.get(), self.price.get(),
                                                 self.category.get(), self.available.get(), self.ingredients.get())
        if status:
            messagebox.showinfo("dish update", message)
            self.reset_form()
        else:
            messagebox.showerror("dish update Error", message)

    def delete_click(self):
        status, message = Dish_Controller.delete(self.id.get())
        if status:
            messagebox.showinfo("dish Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("dish Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.name.clear()
        self.quantity.clear()
        self.price.clear()
        self.category.clear()
        self.available.clear()
        self.ingredients.clear()

        status, dish_list = Dish_Controller.get_all()
        self.table.refresh_table(dish_list)

    def select_from_table(self, selected_dish):
        if selected_dish:
            status, dish = Dish_Controller.find_by_id(selected_dish[0])
            if status:
                dish = Dish(*selected_dish)
                self.id.set(dish.id)
                self.name.set(dish.name)
                self.quantity.set(dish.quantity)
                self.price.set(dish.price)
                self.category.set(dish.category)
                self.available.set(dish.available)
                self.ingredients.set(dish.ingredients)

    def select_dish(self):
        if self.id.get():
            status, Session.dish = Dish_Controller.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select dish")

    def refresh(self):
        pass
