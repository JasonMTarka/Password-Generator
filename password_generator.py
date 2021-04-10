import tkinter as tk
import pyperclip
import os

from random import choice, shuffle


class MainApplication:
    # Class which builds UI
    def __init__(self, root):
        self.root = root
        self._initUI()

    def _password_delivery(self):
        # Bus between Password class and Tkinter UI
        password = Password(lowercase=self.lc_var.get(), uppercase=self.uc_var.get(), nums=self.num_var.get(), syms=self.sym_var.get(),
                            min_nums=self.min_num_clicked.get(), min_syms=self.min_sym_clicked.get(), pass_len=self.len_clicked.get())
        self.e.delete(0, tk.END)
        self.e.insert(0, password)

    def _initUI(self):
        greeting = tk.Label(self.root, text="Generate random passwords!", width=40, borderwidth=0, pady=10)
        greeting.pack(pady=5)

        e = tk.Entry(self.root, width=35, borderwidth=2)
        e.pack()
        self.e = e

        # Creates six frames for UI layout
        frames = {}
        for i in range(1, 7):
            frames[i] = PackedFrame(self.root)

        lc_var = tk.IntVar()
        lc_button = tk.Checkbutton(frames[1], text="Lowercase", variable=lc_var)
        lc_button.pack(side="left", pady=2, padx=3)
        lc_button.select()
        self.lc_var = lc_var

        uc_var = tk.IntVar()
        uc_button = tk.Checkbutton(frames[1], text="Uppercase", variable=uc_var)
        uc_button.pack(side="right", pady=2, padx=3)
        uc_button.select()
        self.uc_var = uc_var

        num_var = tk.IntVar()
        num_button = tk.Checkbutton(frames[2], text="Numbers", variable=num_var)
        num_button.pack(side="left", pady=2, padx=1)
        num_button.select()
        self.num_var = num_var

        sym_var = tk.IntVar()
        sym_button = tk.Checkbutton(frames[2], text="Symbols", variable=sym_var)
        sym_button.pack(side="right", pady=2, padx=11)
        self.sym_var = sym_var

        min_num_label = tk.Label(frames[3], text="Select minimum amount of numbers:")
        min_num_label.pack(side="left")
        min_num_options = [i for i in range(0, 5)]
        min_num_clicked = tk.IntVar()
        min_num_clicked.set(min_num_options[1])
        min_num_bar = tk.OptionMenu(frames[3], min_num_clicked, *min_num_options)
        min_num_bar.configure(activebackground="#d4d4ff")
        min_num_bar.pack(side="left", pady=5)
        self.min_num_clicked = min_num_clicked

        min_sym_label = tk.Label(frames[4], text="Select minimum amount of symbols:")
        min_sym_label.pack(side="left")
        min_sym_options = [i for i in range(0, 5)]
        min_sym_clicked = tk.IntVar()
        min_sym_clicked.set(min_sym_options[1])
        min_sym_bar = tk.OptionMenu(frames[4], min_sym_clicked, *min_sym_options)
        min_sym_bar.configure(activebackground="#d4d4ff")
        min_sym_bar.pack(side="right", pady=5)
        self.min_sym_clicked = min_sym_clicked

        len_label = tk.Label(frames[5], text="Select length of password (between 8-32 characters):")
        len_label.pack(side="left")
        len_options = [i for i in range(8, 33)]
        len_clicked = tk.IntVar()
        len_clicked.set(len_options[0])
        len_bar = tk.OptionMenu(frames[5], len_clicked, *len_options)
        len_bar.configure(activebackground="#c9c9f2")
        len_bar.pack(side="right", pady=5)
        self.len_clicked = len_clicked

        generate_button = HoverButton(frames[6], text="Generate", padx=25, pady=4, borderwidth=3, command=self._password_delivery)
        generate_button.configure(activebackground="#c9c9f2")
        generate_button.pack(padx=5, pady=5, side="left")

        copy_button = HoverButton(frames[6], text="Copy Password", padx=15, pady=4, borderwidth=3, command=lambda: pyperclip.copy(self.e.get()))
        copy_button.configure(activebackground="#d4d4ff")
        copy_button.pack(padx=5, pady=5, side="right")


class Password:
    def __init__(self, lowercase=1, uppercase=1, nums=1, syms=0,
                 min_nums=2, min_syms=2, pass_len=8, value=None):
        self.nums = nums
        self.syms = syms
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.min_nums = min_nums
        self.min_syms = min_syms
        self.pass_len = pass_len
        self.value = value
        if self.value is None:
            self.generate()

    def __repr__(self):
        return f"""Password(lowercase={self.lowercase}, uppercase={self.uppercase}, nums={self.nums}, syms={self.syms},
                 min_nums={self.min_nums}, min_syms={self.min_syms}, pass_len={self.pass_len}, value={self.value})"""

    def __str__(self):
        if self.value:
            return self.value
        else:
            return "Please select at least one character set."

    def __len__(self):
        return self.pass_len

    def __getitem__(self, position):
        return self.value[position]

    def __add__(self, other):
        try:
            return self.value + other.value
        except AttributeError as e:
            return f"AttributeError: {other} has no attribute {e}!"

    def generate(self):
        def _constructor():
            temp_password = []
            if self.nums:
                for i in range(0, self.min_nums):
                    temp_password.append(choice(NUMS))
            if self.syms:
                for i in range(0, self.min_syms):
                    temp_password.append(choice(SYMBOLS))
            while len(temp_password) > self.pass_len:
                temp_password.pop()
            while len(temp_password) < self.pass_len:
                temp_password.append(choice(source))
            shuffle(temp_password)
            return temp_password

        source = ""
        LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
        UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMS = "0123456789"
        SYMBOLS = "!@#$%^&*"

        if self.lowercase:
            source += LOWERCASE
        if self.uppercase:
            source += UPPERCASE
        if self.nums:
            source += NUMS
        if self.syms:
            source += SYMBOLS

        if source:
            password = _constructor()
            self.value = "".join(password)


class HoverButton(tk.Button):
    # Class for changing button color when highlighting with cursor
    def __init__(self, master, **kwargs):
        tk.Button.__init__(self, master=master, **kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, z):
        self["background"] = self["activebackground"]

    def on_leave(self, z):
        self["background"] = self.defaultBackground


class PackedFrame(tk.Frame):
    # Class which automatically packs frames on instantiation
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master=master, **kwargs)
        self.pack()


def main():
    # Function which sets up the interactive window
    root = tk.Tk()
    MainApplication(root)
    root.title("Password Generator")
    root.iconbitmap(os.environ.get("PASSWORD_GEN_KEY_ICON"))
    root.geometry('400x310')
    root.resizable(height=False, width=False)
    root.mainloop()


if __name__ == "__main__":
    main()
