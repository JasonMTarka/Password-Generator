from random import choice, shuffle
import tkinter as tk
import pyperclip

# Class which builds UI
class MainApplication:

	def __init__(self):
		self.init_UI()

	def init_UI(self):
		greeting = tk.Label(root,text="Generate random passwords!", width=40, borderwidth=0, pady=10)
		greeting.pack(pady=5)

		e = tk.Entry(root, width=35, borderwidth=2)
		e.pack()
		self.e = e

		# Creates six frames for UI layout
		frames = {}
		for i in range(1,7):
			frames[i] = PackedFrame(root)

		lc_var = tk.IntVar()
		lc_button = tk.Checkbutton(frames[1], text="Lowercase",variable=lc_var)
		lc_button.pack(side="left",pady=2,padx=3)
		lc_button.select()
		self.lc_var = lc_var

		uc_var = tk.IntVar()
		uc_button = tk.Checkbutton(frames[1], text="Uppercase",variable=uc_var)
		uc_button.pack(side="right",pady=2,padx=3)
		uc_button.select()
		self.uc_var = uc_var

		num_var = tk.IntVar()
		num_button = tk.Checkbutton(frames[2], text="Numbers",variable=num_var)
		num_button.pack(side="left",pady=2,padx=1)
		num_button.select()
		self.num_var = num_var

		sym_var = tk.IntVar()
		sym_button = tk.Checkbutton(frames[2], text="Symbols",variable=sym_var)
		sym_button.pack(side="right",pady=2,padx=11)
		self.sym_var = sym_var

		min_num_label = tk.Label(frames[3],text="Select minimum amount of numbers:")
		min_num_label.pack(side="left")
		min_num_options = [i for i in range(0,5)]
		min_num_clicked = tk.IntVar()
		min_num_clicked.set(min_num_options[1])
		min_num_bar = tk.OptionMenu(frames[3],min_num_clicked,*min_num_options)
		min_num_bar.configure(activebackground="#d4d4ff")
		min_num_bar.pack(side="left",pady=5)
		self.min_num_clicked = min_num_clicked

		min_sym_label = tk.Label(frames[4],text="Select minimum amount of symbols:")
		min_sym_label.pack(side="left")
		min_sym_options = [i for i in range(0,5)]
		min_sym_clicked = tk.IntVar()
		min_sym_clicked.set(min_sym_options[1])
		min_sym_bar = tk.OptionMenu(frames[4],min_sym_clicked,*min_sym_options)
		min_sym_bar.configure(activebackground="#d4d4ff")
		min_sym_bar.pack(side="right",pady=5)
		self.min_sym_clicked = min_sym_clicked

		len_label = tk.Label(frames[5],text="Select length of password (between 8-32 characters):")
		len_label.pack(side="left")
		len_options = [i for i in range(8,33)]
		len_clicked = tk.IntVar()
		len_clicked.set(len_options[0])
		len_bar = tk.OptionMenu(frames[5], len_clicked, *len_options)
		len_bar.configure(activebackground="#c9c9f2")
		len_bar.pack(side="right",pady=5)
		self.len_clicked = len_clicked

		generate_button = HoverButton(frames[6],text="Generate", padx=25, pady=4,borderwidth=3,command=pass_gen)
		generate_button.configure(activebackground="#c9c9f2")
		generate_button.pack(padx=5,pady=5,side="left")

		copy_button = HoverButton(frames[6], text="Copy Password", padx=15, pady=4, borderwidth=3,command= lambda: pyperclip.copy(app.e.get()))
		copy_button.configure(activebackground="#d4d4ff")
		copy_button.pack(padx=5,pady=5,side="right")

# Class for changing button color when highlighting with cursor
class HoverButton(tk.Button):

	def __init__(self,master, **kwargs):
		tk.Button.__init__(self,master=master,**kwargs)
		self.defaultBackground=self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self,z):
		self["background"] = self["activebackground"]

	def on_leave(self,z):
		self["background"] = self.defaultBackground

# Class which automatically packs frames on instantiation
class PackedFrame(tk.Frame):

	def __init__(self,master,**kwargs):
		tk.Frame.__init__(self,master=master,**kwargs)
		self.pack()

# Primary password generator function
def pass_gen():

	# Creates a random password with the selected parameters:
	def simple_generation():
		password = []

		if app.num_var.get() == 1:
			for i in range(0,int(app.min_num_clicked.get())):
				password.append(choice(NUMS))
		if app.sym_var.get() == 1:
			for i in range(0,int(app.min_sym_clicked.get())):
				password.append(choice(SYMBOLS))
		while len(password) < app.len_clicked.get():
			password.append(choice(source))

		shuffle(password)

		return password

	# Sends the finished password to the GUI and resets the password source:
	def password_delivery(password):
		app.e.delete(0,tk.END)
		app.e.insert(0,"".join(password))
		source = "" #Resets source variable for the next password

	# Following code collects parameters and adds them to a source variable from which passwords are generated:
	source = ""
	NUMS = "0123456789"
	LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
	UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	SYMBOLS = "!@#$%^&*"

	if app.lc_var.get() == 1:
		source += LOWERCASE

	if app.uc_var.get() == 1:
		source += UPPERCASE

	if app.num_var.get() == 1:
		source += NUMS

	if app.sym_var.get() == 1:
		source += SYMBOLS

	# Generates and delivers a password according to the selected parameters
	if source:
		password = simple_generation()
		password_delivery(password)

	else:
		app.e.delete(0,tk.END)
		app.e.insert(0,"Please select at least one category.")

# Function which sets up the interactive window
def main():
	global root, app
	root = tk.Tk()
	app = MainApplication()
	root.title("Password Generator")
	root.geometry('400x310')
	root.resizable(height = False, width = False)
	root.mainloop()

if __name__ == "__main__":
	main()
