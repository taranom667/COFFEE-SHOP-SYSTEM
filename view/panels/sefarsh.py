from tkinter import *

from model.session import Session
from view import *

class Sefaresh:
    def __init__(self):
        self.window = Tk()
        self.window.title("sabt sefaresh")
        self.window.geometry("300x470")
        self.window.configure(background="#d9d9d9")

        self.Latte = BooleanVar()
        self.Cappuccino = BooleanVar()
        self.Hot_chocolate = BooleanVar()
        self.Iced_Americano = BooleanVar()
        self.Iced_Latte = BooleanVar()
        self.Chocolate_cake = BooleanVar()
        self.classic_cake = BooleanVar()

        items = [
            ("Latte", self.Latte),
            ("Cappuccino", self.Cappuccino),
            ("Hot_chocolate", self.Hot_chocolate),
            ("Iced_Americano", self.Iced_Americano),
            ("Iced_Latte", self.Iced_Latte),
            ("Chocolate_cake", self.Chocolate_cake),
            ("classic_cake", self.classic_cake)
        ]

        y = 20
        for name, var in items:
            Checkbutton(self.window, text=name, variable=var,
                        font=("Times New Roman", 10, "italic")
                        ).place(x=20, y=y)
            y += 40

        Button(self.window, text="Done", command=self.show).place(x=20, y=350)

        self.window.mainloop()

    def show(self):
        self.selected = []

        if self.Latte.get(): self.selected.append("Latte")
        if self.Cappuccino.get(): self.selected.append("Cappuccino")
        if self.Hot_chocolate.get(): self.selected.append("Hot_chocolate")
        if self.Iced_Americano.get(): self.selected.append("Iced_Americano")
        if self.Iced_Latte.get(): self.selected.append("Iced_Latte")
        if self.Chocolate_cake.get(): self.selected.append("Chocolate_cake")
        if self.classic_cake.get(): self.selected.append("classic_cake")

        print( self.selected)
        Session.dish=self.selected


