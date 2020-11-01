import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from project.sign_up_page import SignUpPage
from project.text_sharper import *
from project.Main_WIndow import *


def SignUpWindowCaller():
    log.root.destroy()
    sign = SignUpPage(title_='Sign up page', geometry_='1850x950',
                      icon_='login_page_icon.ico', photo_='sign_up_page_background.jpeg')

    sign.run()


def LoginWindowCaller():
    db = shelve.open('zym_database')

    if log.entry1.get() == '' and log.entry2.get() == '':
        messagebox.showwarning('Login error', 'Please enter your name and password.')

    elif log.entry1.get() == '':
        messagebox.showwarning('Login error', 'Please enter your name.')

    elif log.entry2.get() == '':
        messagebox.showwarning('Login error', 'Please enter your password.')

    if log.entry1.get() != '' and log.entry2.get() != '':
        entered_name = log.entry1.get()
        entered_password = log.entry2.get()

        names = []

        for object in db.values():
            name = object.firstname + ' ' + object.lastname
            names.append(name)

        if entered_name not in names:
            messagebox.showwarning('Invalid Name', 'Name does not exist')

        elif entered_name in names and entered_password not in db:
            messagebox.showwarning('Invalid password', 'Password is incorrect')
        else:
            messagebox.showinfo('Login status', 'Login Successful.')
            log.root.destroy()
            mainWindow = MainWindow(title_='Main Window', geometry_='1200x800',
                                    icon_='main_window_icon_clv_2.ico', password_=entered_password,
                                    filename_='zym_database')
            mainWindow.run()



class LoginPage:

    def __init__(self, title_, geometry_, icon_, photo_):
        self.root = tk.Tk()
        MakeTkDPIAware(self.root)

        self.root.title(title_)
        self.root.resizable(0, 0)
        self.root.geometry(geometry_)
        self.root.iconbitmap(icon_)
        self.canvas = tk.Canvas()
        self.photo = ImageTk.PhotoImage(Image.open(photo_))
        self.frame = ttk.Frame(self.root)
        self.entry1 = tk.Entry(self.frame)
        self.entry2 = tk.Entry(self.frame)
        self.label1 = ttk.Label(self.frame)
        self.label2 = ttk.Label(self.frame)
        self.label3 = ttk.Label(self.frame)
        self.login_button = tk.Button(self.frame)
        self.sign_up_button = tk.Button(self.frame)

        self.set_background(670, 1191)  # dimensions
        self.set_frame()
        self.set_entry()
        self.set_labels()
        self.set_buttons()

    def set_background(self, height_, width_):
        self.canvas.configure(height=height_, width=width_)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.pack()

    def set_frame(self):
        self.frame.configure(height=500, width=400)
        self.frame.place(x=300, y=100)

    def set_entry(self):
        self.entry1.configure(font=('@Yu Gothic Light', '20', 'bold'), width=22, insertwidth=5, insertofftime=100,
                              insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.entry1.place(x=32, y=180)

        self.entry2.configure(font=('@Yu Gothic Light', '20', 'bold'), width=22, insertwidth=5, insertofftime=100,
                              insertontime=150, insertbackground='#3F0B85', fg='#3F0B85', show='*')
        self.entry2.place(x=32, y=300)

    def set_labels(self):
        self.label1.configure(text='LOGIN   WINDOW', foreground='#200045', font=('Cambria', '25'))
        self.label1.place(x=65, y=40)
        self.label2.configure(text='Enter Your Full Name', foreground='#200045', font=('Cambria', '15'))
        self.label2.place(x=30, y=150)
        self.label3.configure(text='Password', foreground='#200045', font=('Cambria', '15'))
        self.label3.place(x=30, y=270)

    def set_buttons(self):
        self.login_button.configure(text='LOGIN', activeforeground='#8254FF', cursor='hand2',
                                    width=12, fg='#200045', overrelief='raised', relief='groove',
                                    font=('Calibre Light', '15'), command=LoginWindowCaller)
        self.login_button.place(x=50, y=400)
        self.sign_up_button.configure(text='SIGN UP', activeforeground='#8254FF', cursor='hand2',
                                      width=12, fg='#200045', overrelief='raised', relief='groove',
                                      font=('Calibre Light', '15'), command=SignUpWindowCaller)
        self.sign_up_button.place(x=210, y=400)

    def run(self):
        self.root.mainloop()


log = LoginPage(title_='login page', geometry_='1000x670',
                icon_='login_page_icon.ico', photo_='loginbackground.png')

log.run()
# print('\n'.join(font.families()))
