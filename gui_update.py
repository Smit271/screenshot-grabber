from email.mime import image
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkinter import font
from ss import Take
from datetime import datetime
from login_api import Login
from PIL import Image, ImageTk
from pystray import MenuItem as item
import pystray 
import customtkinter

# Frames logic
# First Frame Class
class FirstFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.e_name = ""
		self.e_id = ""
		self.e_email = ""

		# ----- Background Image settings ----- #
		img = ImageTk.PhotoImage(Image.open("./assets/image_1.png"), Image.ANTIALIAS)
		lbl = tk.Label(self, image=img)
		lbl.img = img  # Keep a reference in case this code put is in a function.
		lbl.place(relx=0.5, rely=0.5, anchor='center') 
		# -------------------------------------- #
		L1 = customtkinter.CTkLabel(self, text="Email")
		L1.place(x = 200, y = 200)
		T1 = customtkinter.CTkEntry(self, width = 200)
		T1.place(x = 350, y = 200)

		L2 = customtkinter.CTkLabel(self, text="Password")
		L2.place(x = 200, y = 250)
		T2 = customtkinter.CTkEntry(self, width = 200, show = '*')
		T2.place(x = 350, y = 250)

		label = customtkinter.CTkLabel(self, text="Enter Credentials")
		label.place(x = 300, y = 350)

		def infinite_loop():
			# print(condition)
			# print(u_name)
			# print("Running infinite_loop")
			if condition:
				a = Take(self.e_name, self.e_id)
				a.main()
				# after(miliseconds, function)
				self.after(5000, infinite_loop) # 5000 : 5 Secs
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
				FirstFrame.hide_window()
				# self.hide_and_return()
				# print(f"Start time : {t}")
			else:
				messagebox.showinfo("Error", "Wrong Credentials")
		
		# button_image_1 = PhotoImage(
		# 	file= "./assets/button_2.png")
		b1 = customtkinter.CTkButton(self,
		 		text="Start",
				command=verify,
				width=20, 
				height=20)
		b1.place(x = 625, y = 400)

		def quit():
			t = datetime.now()
			# print(f"Exit time : {t}")
			app.destroy()
		b2 = customtkinter.CTkButton(self, text="Exit", command=quit, width=20, height=20)
		b2.place(x = 625, y = 450)
	def hide_and_return(self):
		app.iconify() # Will minimize the app
		SecondFrame.show_me()

	# Define a function for quit the window
	def quit_window(icon, item):
		icon.stop()
		app.destroy()

	# Define a function to show the window again
	def show_window(icon, item):
		icon.stop()
		app.after(0,app.deiconify())
	def hide_window():
		app.withdraw()
		image=Image.open("icon-1.ico")
		menu=(item('Quit', FirstFrame.quit_window), item('Open', FirstFrame.show_window))
		icon=pystray.Icon("name", image, "Application", menu)
		icon.run()

# Second Frame Class
class SecondFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# ----- Background Image settings ----- #
		img = ImageTk.PhotoImage(Image.open("./assets/image_1.png"), Image.ANTIALIAS)
		lbl = tk.Label(self, image=img)
		lbl.img = img  # Keep a reference in case this code put is in a function.
		lbl.place(relx=0.5, rely=0.5, anchor='center') 
		# -------------------------------------- #

		label = customtkinter.CTkLabel(self, text=f"Welcome")
		label.place(x = 250, y = 170)

		label = customtkinter.CTkLabel(self, text=f"Now you can start your work")
		label.place(x = 230, y = 230)

		def quit():
			t = datetime.now()
			print(f"Exit time : {t}")
			app.destroy()
		b2 = customtkinter.CTkButton(self,
									text="Exit",
									command=quit,
									width=20,
									height=20)
		b2.place(x = 650, y = 450)
	def show_me():
		app.update()
		app.deiconify()

# Main Class
class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# tk.Tk.title("App")
		# creating window
		customtkinter.set_appearance_mode("System")
		customtkinter.set_default_color_theme("blue")
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
app.title("Application")
app.geometry("700x500")
app.resizable(0, 0)
app.protocol('WM_DELETE_WINDOW', FirstFrame.hide_window)
app.mainloop()
