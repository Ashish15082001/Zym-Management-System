import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from project.text_sharper import *
from tkinter import Menu
from tkinter import messagebox
import shelve


def display_details(self, password_, filename_):
    db = shelve.open(filename_)

    tk.Label(self.personal_details_label_frame, text=f'First Name    :   {db[password_].firstname}',
             font=('Calibre Light', '15')).place(x=15, y=15)

    tk.Label(self.personal_details_label_frame, text=f'Gender    :   {db[password_].gender}',
             font=('Calibre Light', '15')).place(x=600, y=15)

    tk.Label(self.personal_details_label_frame, text=f'Last Name     :   {db[password_].lastname}',
             font=('Calibre Light', '15')).place(x=15, y=55)

    tk.Label(self.personal_details_label_frame, text=f'Height   :   {db[password_].height}',
             font=('Calibre Light', '15')).place(x=15, y=95)

    tk.Label(self.personal_details_label_frame, text=f'Weight   :   {db[password_].weight}',
             font=('Calibre Light', '15')).place(x=15, y=135)

    tk.Label(self.personal_details_label_frame, text=f'Admission no     :   {db[password_].admission_no}',
             font=('Calibre Light', '15')).place(x=15, y=175)

    tk.Label(self.personal_details_label_frame, text=f'Date Of Birth    :   {db[password_].DOB}',
             font=('Calibre Light', '15')).place(x=15, y=215)

    tk.Label(self.personal_details_label_frame, text=f'Phone Number     :   {db[password_].phoneNumber}',
             font=('Calibre Light', '15')).place(x=15, y=255)

    tk.Label(self.personal_details_label_frame, text=f'Address     :   {db[password_].address}',
             font=('Calibre Light', '15')).place(x=15, y=295)

    tk.Label(self.personal_details_label_frame, text=f'Email      :   {db[password_].email}',
             font=('Calibre Light', '15')).place(x=15, y=335)

    tk.Label(self.guardian_details_label_frame, text=f'Father Name     :   {db[password_].fathername}',
             font=('Calibre Light', '15')).place(x=15, y=15)

    tk.Label(self.guardian_details_label_frame, text=f'Father Occupation    :   {db[password_].fatheroccupation}',
            font=('Calibre Light', '15')).place(x=15, y=55)


class MainWindow():
    def __init__(self, title_, geometry_, icon_, password_, filename_):
        self.root = tk.Tk()
        MakeTkDPIAware(self.root)

        self.root.title(title_)
        self.root.resizable(0, 0)
        self.root.geometry(geometry_)
        self.root.iconbitmap(icon_)

        self.menubar = Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Save As')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Print')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit')

        self.menubar.add_cascade(label='File', menu=self.file_menu)

        self.about_menu = Menu(self.menubar, tearoff=0)
        self.about_menu.add_command(label='Developers')
        self.about_menu.add_command(label='Software')
        self.menubar.add_cascade(label='About', menu=self.about_menu)

        self.tabControl = ttk.Notebook(self.root)  # Create Tab Control
        self.profile_tab = ttk.Frame(self.tabControl)  # Create a tab
        self.tabControl.add(self.profile_tab, text='Profile')  # Add the tab
        self.tabControl.pack(expand=1, fill="both")
        self.zym_details_tab = ttk.Frame(self.tabControl)  # Add a second tab
        self.tabControl.add(self.zym_details_tab, text='Zym details')

        self.profile_label_frame = tk.LabelFrame(self.profile_tab, text='Your profile details')
        self.zym_details_label_frame = tk.LabelFrame(self.zym_details_tab, text='Zym details')

        self.personal_details_label_frame = tk.LabelFrame(self.profile_label_frame, text='Your personal details')
        self.guardian_details_label_frame = tk.LabelFrame(self.profile_label_frame, text='Your guardian details')

        self.set_frame()
        display_details(self, password_, filename_)

    def set_frame(self):
        self.profile_label_frame.configure(height=720, width=1170)
        self.profile_label_frame.place(x=15, y=15)

        self.zym_details_label_frame.configure(height=720, width=1170)
        self.zym_details_label_frame.place(x=15, y=15)

        self.personal_details_label_frame.configure(height=400, width=1135)
        self.personal_details_label_frame.place(x=15, y=15)

        self.guardian_details_label_frame.configure(height=150, width=1135)
        self.guardian_details_label_frame.place(x=15, y=500)

    def run(self):
        self.root.mainloop()

