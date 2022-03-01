import tkinter as tk
from tkinter import ttk, messagebox
from ss import Take
from datetime import datetime
from login_api import Login

# Frames logic
# First Frame Class
class FirstFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.e_name = ""
		self.e_id = ""
		self.e_email = ""

		L1 = tk.Label(self, text="Employee_Id", font = ("Arial Bold", 15))
		L1.place(x = 50, y = 50)
		T1 = tk.Entry(self, width = 30, bd = 5)
		T1.place(x = 200, y = 50)

		L2 = tk.Label(self, text="Password", font = ("Arial Bold", 15))
		L2.place(x = 50, y = 100)
		T2 = tk.Entry(self, width = 30, bd = 5, show = '*')
		T2.place(x = 200, y = 100)

		label = tk.Label(self, text="Enter Credentials", font = ("Arial Bold", 15)	)
		label.place(x = 230, y = 230)

		def infinite_loop():
			print(condition)
			print(u_name)
			print("Running infinite_loop")
			if condition:
				a = Take(u_name, self.e_id)
				a.main()
				self.after(5000, infinite_loop)
			else:
				self.after(5000, infinite_loop)
				
		def verify():
			l = Login(T1.get(), T2.get())
			r = l.login()
			if r['status'] == 200:
				global condition, u_name, id
				condition = True
				u_name = T1.get()
				id = r['data']['id']
				self.e_id = r['data']['id']
				self.e_name = r['data']['employeeName']
				self.e_email = r['data']['email']
				controller.show_frame(SecondFrame)
				infinite_loop()
				t = datetime.now()
				print(f"Start time : {t}")
			else:
				messagebox.showinfo("Error", "Wrong Credentials")
		b1 = tk.Button(self, text="Start", command=verify)
		b1.place(x = 650, y = 400)

		def quit():
			t = datetime.now()
			print(f"Exit time : {t}")
			app.destroy()
		b2 = tk.Button(self, text="Exit", command=quit)
		b2.place(x = 650, y = 450)

# Second Frame Class
class SecondFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text=f"Welcome", font = ("Arial Bold", 15))
		label.place(x = 150, y = 100)

		label = tk.Label(self, text=f"Now you can start your work", font = ("Arial Bold", 15))
		label.place(x = 230, y = 230)

		def quit():
			t = datetime.now()
			print(f"Exit time : {t}")
			app.destroy()
		b2 = tk.Button(self, text="Exit", command=quit)
		b2.place(x = 650, y = 450)

# Main Class
class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# creating window
		window = tk.Frame(self)
		window.pack()

		window.grid_rowconfigure(0, minsize = 500)
		window.grid_columnconfigure(0, minsize = 800)

		self.frames	= {}
		for F in (FirstFrame, SecondFrame):
			frame = F(window, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame(FirstFrame)
	def show_frame(self, page):
		frame = self.frames[page]
		frame.tkraise()

app = Application()
app.mainloop()
