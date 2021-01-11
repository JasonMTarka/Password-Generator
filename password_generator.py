from random import choice
from tkinter import *
import pyperclip

root = Tk()
root.title("Password Generator")
root.geometry('400x310')
root.maxsize(400,310)

#Class for changing button color when highlighting with cursor
class HoverButton(Button):

	def __init__(self,master, **kwargs):
		Button.__init__(self,master=master,**kwargs)
		self.defaultBackground=self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self,z):
		self["background"] = self["activebackground"]

	def on_leave(self,z):
		self["background"] = self.defaultBackground

#Primary password generator function
def pass_gen():

	#Creates a random password with the selected parameters:
	def simple_generation():
		password = []
		for i in range(0,int(len_clicked.get())):
			password.append(choice(source))
		return password

	#Sends the finished password to the GUI and resets the password source:
	def password_delivery(password):
		e.delete(0,END)
		e.insert(0,"".join(password))
		source = "" #Resets source variable for the next password

	#Checks a password to see if there are enough numbers according to parameters:
	def number_check(password):
		filtered_list = [True for i in password if i in "0123456789"]
		if len(filtered_list) < min_num_clicked.get():
			return False
		else:
			return True

	#Checks a password to see if there are enough symbols according to parameters:
	def sym_check(password):
		filtered_list = [True for i in password if i in "!@#$%&*"]
		if len(filtered_list) < min_sym_clicked.get():
			return False
		else:
			return True

	#Following code collects parameters and adds them to a source variable from which passwords are generated:
	source = ""

	if lc_var.get() == 1:
		source += "abcdefghijklmnopqrstuvwxyz"

	if uc_var.get() == 1:
		source += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if num_var.get() == 1:
		source += "0123456789"

	if sym_var.get() == 1:
		source += "!@#$%^&*"

	#Generates and checks passwords until it finds one that satisfies all conditions:
	if source:
		looper = True
		while looper:
			trial_password = simple_generation()
			if (min_num_clicked.get() > 0) and (num_var.get() == 1):
				if number_check(trial_password):
					if (min_sym_clicked.get() > 0) and (sym_var.get() == 1):
						if sym_check(trial_password):
							password_delivery(trial_password)
							break
						else:
							pass
					else:
						password_delivery(trial_password)
						break
				else:
					pass

			elif (min_sym_clicked.get() > 0) and (sym_var.get() == 1):
				if sym_check(trial_password):
					password_delivery(trial_password)
					break
				else:
					pass
			else:
				password_delivery(trial_password)
				break
	else:
		e.delete(0,END)
		e.insert(0,"Please select at least one category.")

#Function for copying the finished password to clipboard
def copier():
	pyperclip.copy(e.get())

#Below are buttons for the GUI
greeting = Label(root,text="Generate random passwords!", width=40, borderwidth=0, pady=10)
greeting.pack(pady=5)

e = Entry(root, width=35, borderwidth=2)
e.pack()

frame1 = Frame(root)
frame1.pack()

lc_var = IntVar()
lc_button = Checkbutton(frame1, text="Lowercase",variable=lc_var)
lc_button.pack(side="left",pady=2,padx=3)
lc_button.select()

uc_var = IntVar()
uc_button = Checkbutton(frame1, text="Uppercase",variable=uc_var)
uc_button.pack(side="right",pady=2,padx=3)
uc_button.select()

frame2 = Frame(root)
frame2.pack()

num_var = IntVar()
num_button = Checkbutton(frame2, text="Numbers",variable=num_var)
num_button.pack(side="left",pady=2,padx=1)
num_button.select()

sym_var = IntVar()
sym_button = Checkbutton(frame2, text="Symbols",variable=sym_var)
sym_button.pack(side="right",pady=2,padx=11)

frame3 = Frame(root)
frame3.pack()

min_num_label = Label(frame3,text="Select minimum amount of numbers:")
min_num_label.pack(side="left")
min_num_options = [0,1,2,3]
min_num_clicked = IntVar()
min_num_clicked.set(min_num_options[1])
min_num_bar = OptionMenu(frame3,min_num_clicked,*min_num_options)
min_num_bar.configure(activebackground="#d4d4ff")
min_num_bar.pack(side="left",pady=5)

frame4 = Frame(root)
frame4.pack()

min_sym_label = Label(frame4,text="Select minimum amount of symbols:")
min_sym_label.pack(side="left")
min_sym_options = [0,1,2,3]
min_sym_clicked = IntVar()
min_sym_clicked.set(min_sym_options[1])
min_sym_bar = OptionMenu(frame4,min_sym_clicked,*min_sym_options)
min_sym_bar.configure(activebackground="#d4d4ff")
min_sym_bar.pack(side="right",pady=5)

frame5 = Frame(root)
frame5.pack()

len_label = Label(frame5,text="Select length of password (between 8-32 characters):")
len_label.pack(side="left")
len_options = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
len_clicked = IntVar()
len_clicked.set(len_options[0])
len_bar = OptionMenu(frame5, len_clicked, *len_options)
len_bar.configure(activebackground="#c9c9f2")
len_bar.pack(side="right",pady=5)

frame6 = Frame(root)
frame6.pack()

generate_button = HoverButton(frame6,text="Generate", padx=25, pady=4,borderwidth=3,command=pass_gen)
generate_button.configure(activebackground="#c9c9f2")
generate_button.pack(padx=5,pady=5,side="left")

copy_button = HoverButton(frame6, text="Copy Password", padx=15, pady=4, borderwidth=3,command=copier)
copy_button.configure(activebackground="#d4d4ff")
copy_button.pack(padx=5,pady=5,side="right")

root.mainloop()
