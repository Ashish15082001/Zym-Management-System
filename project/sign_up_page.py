import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from project.text_sharper import *
from tkinter import messagebox
import shelve
from person import *


def object_factory(class_, *vargs, **kwargs):
    return class_(*vargs, **kwargs)


def save_to_database(filename, object_, log_):
    db = shelve.open(filename)
    if object_.password in db:
        messagebox.showerror('Error', 'Password already exists.')

    else:
        db[object_.password] = object_
        db.close()
        messagebox.showinfo('Info', 'SignUP was successfully done. Please login again.')
        log_.root.destroy()


class SignUpPage:

    def __init__(self, title_, geometry_, icon_, photo_):
        self.root = tk.Tk()
        MakeTkDPIAware(self.root)

        self.root.title(title_)
        self.root.resizable(0, 0)
        self.root.geometry(geometry_)
        self.root.iconbitmap(icon_)
        self.canvas = tk.Canvas()

        self.photo = ImageTk.PhotoImage(Image.open(photo_))

        self.main_frame = ttk.Frame(self.root)
        self.member_details_frame = tk.LabelFrame(self.main_frame, text='Member Details')
        self.contact_details_frame = tk.LabelFrame(self.main_frame, text='Contact Details')
        self.guardian_details_frame = tk.LabelFrame(self.main_frame, text='Guardian Details')
        self.password_frame = tk.LabelFrame(self.main_frame, text='Set Password')

        self.sign_up_label = ttk.Label(self.main_frame)

        self.first_name_entry = tk.Entry(self.member_details_frame)
        self.last_name_entry = tk.Entry(self.member_details_frame)
        self.height_entry = tk.Entry(self.member_details_frame)
        self.weight_entry = tk.Entry(self.member_details_frame)
        self.admission_No_entry = tk.Entry(self.member_details_frame)
        self.DOB_entry = tk.Entry(self.member_details_frame)

        self.first_name_label = ttk.Label(self.member_details_frame)
        self.last_name_label = ttk.Label(self.member_details_frame)
        self.height_label = ttk.Label(self.member_details_frame)
        self.weight_label = ttk.Label(self.member_details_frame)
        self.admission_no_label = ttk.Label(self.member_details_frame)
        self.DOB_label = ttk.Label(self.member_details_frame)
        self.gender_label = ttk.Label(self.member_details_frame)

        self.male_radiobutton = ttk.Radiobutton(self.member_details_frame)
        self.female_radiobutton = ttk.Radiobutton(self.member_details_frame)
        self.other_radiobutton = ttk.Radiobutton(self.member_details_frame)

        self.gender = tk.StringVar()

        self.address_label = ttk.Label(self.contact_details_frame)
        self.phonenumber_label = ttk.Label(self.contact_details_frame)
        self.email_label = ttk.Label(self.contact_details_frame)

        self.address_entry = tk.Entry(self.contact_details_frame)
        self.phonenumber_entry = tk.Entry(self.contact_details_frame)
        self.email_entry = tk.Entry(self.contact_details_frame)

        self.father_name_label = ttk.Label(self.guardian_details_frame)
        self.father_occupation_label = ttk.Label(self.guardian_details_frame)

        self.father_name_entry = tk.Entry(self.guardian_details_frame)
        self.father_occupation_entry = tk.Entry(self.guardian_details_frame)

        self.password_label = ttk.Label(self.password_frame)
        self.passwordconfirm_label = ttk.Label(self.password_frame)

        self.password_entry = tk.Entry(self.password_frame)
        self.passwordconfirm_entry = tk.Entry(self.password_frame)

        self.sign_up_button = tk.Button(self.main_frame)

        self.set_radiobutton()

    def signUpCallback(self):
        if self.first_name_entry.get() == '' or self.last_name_entry.get() == '' or self.height_entry.get() == '' or \
                self.weight_entry.get() == '' or self.admission_No_entry.get() == '' or self.DOB_entry.get() == '' or \
                self.gender.get() not in ('Male', 'Female', 'Other') \
                or self.address_entry.get() == '' or self.email_entry.get() == '' or self.password_entry.get() == '' or \
                self.passwordconfirm_entry.get() == '' or self.phonenumber_entry.get() == '' or self.father_name_entry.get() == '' \
                or self.father_occupation_entry.get() == '':

            messagebox.showwarning('Warning', 'All Details are compulsory')

        else:
            answer = messagebox.askokcancel('SignUP Confirmation Window',
                                            'Are you sure? Do Check whether all mentioned details are '
                                            'correct.')
            if answer == 1:
                if self.password_entry.get() != self.passwordconfirm_entry.get():
                    messagebox.showwarning('Warning', 'New password and Confirmed password are not same.')
                else:
                    person = object_factory(Person, self.first_name_entry.get(), self.last_name_entry.get(),
                                            self.height_entry.get(), self.weight_entry.get(),
                                            self.admission_No_entry.get(),
                                            self.DOB_entry.get(), self.gender.get(), self.address_entry.get(),
                                            self.phonenumber_entry.get(), self.email_entry.get(), self.father_name_entry.get(),
                                            self.father_occupation_entry.get(), self.passwordconfirm_entry.get())

                    save_to_database('zym_database', person, self)
                    print(person)

    def set_radiobutton(self):
        self.male_radiobutton.configure(text='Male', value='Male', variable=self.gender)
        self.male_radiobutton.place(x=435, y=240)

        self.female_radiobutton.configure(text='Female', value='Female', variable=self.gender)
        self.female_radiobutton.place(x=500, y=240)

        self.other_radiobutton.configure(text='Other', value='Other', variable=self.gender)
        self.other_radiobutton.place(x=570, y=240)

    def set_background(self, height_, width_):
        self.canvas.configure(height=height_, width=width_)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.pack()

    def set_frame(self):
        self.main_frame.configure(height=850, width=1450)
        self.main_frame.place(x=200, y=50)

        self.member_details_frame.configure(height=400, width=700)
        self.member_details_frame.place(x=25, y=70)

        self.contact_details_frame.configure(height=400, width=650)
        self.contact_details_frame.place(x=775, y=70)

        self.guardian_details_frame.configure(height=130, width=1400)
        self.guardian_details_frame.place(x=25, y=480)

        self.password_frame.configure(height=130, width=1400)
        self.password_frame.place(x=25, y=620)

    def set_entry(self):
        self.first_name_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5,
                                        insertofftime=100,
                                        insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.first_name_entry.place(x=15, y=60)

        self.last_name_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5,
                                       insertofftime=100,
                                       insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.last_name_entry.place(x=15, y=150)

        self.height_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5, insertofftime=100,
                                    insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.height_entry.place(x=15, y=240)

        self.weight_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5, insertofftime=100,
                                    insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.weight_entry.place(x=15, y=330)

        self.admission_No_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5,
                                          insertofftime=100,
                                          insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.admission_No_entry.place(x=435, y=60)
        self.DOB_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5,
                                 insertofftime=100,
                                 insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.DOB_entry.place(x=435, y=150)

        self.address_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5,
                                     insertofftime=100,
                                     insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.address_entry.place(x=15, y=60)

        self.phonenumber_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=20, insertwidth=5,
                                         insertofftime=100,
                                         insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.phonenumber_entry.place(x=15, y=150)

        self.email_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5, insertofftime=100,
                                   insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.email_entry.place(x=15, y=240)

        self.father_name_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5,
                                         insertofftime=100,
                                         insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.father_name_entry.place(x=15, y=60)

        self.father_occupation_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5,
                                               insertofftime=100,
                                               insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.father_occupation_entry.place(x=765, y=60)

        self.password_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5,
                                      insertofftime=100,
                                      insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.password_entry.place(x=15, y=60)

        self.passwordconfirm_entry.configure(font=('@Yu Gothic Light', '15', 'bold'), width=51, insertwidth=5,
                                             insertofftime=100,
                                             insertontime=150, insertbackground='#3F0B85', fg='#3F0B85')
        self.passwordconfirm_entry.place(x=765, y=60)

    def set_labels(self):
        self.sign_up_label.configure(text='SIGN UP WINDOW', foreground='#91060F', font=('Cambria', '25'))
        self.sign_up_label.place(x=600, y=10)

        self.first_name_label.configure(text='First Name', foreground='#91060F', font=('Cambria', '15'))
        self.first_name_label.place(x=15, y=30)

        self.last_name_label.configure(text='Last Name', foreground='#91060F', font=('Cambria', '15'))
        self.last_name_label.place(x=15, y=120)

        self.height_label.configure(text='height ( in feet and inches )', foreground='#91060F', font=('Cambria', '15'))
        self.height_label.place(x=15, y=210)

        self.weight_label.configure(text='Weight ( in kg )', foreground='#91060F', font=('Cambria', '15'))
        self.weight_label.place(x=15, y=300)

        self.admission_no_label.configure(text='Admission No', foreground='#91060F', font=('Cambria', '15'))
        self.admission_no_label.place(x=435, y=30)

        self.DOB_label.configure(text='Date Of Birth :', foreground='#91060F', font=('Cambria', '15'))
        self.DOB_label.place(x=435, y=120)

        self.gender_label.configure(text='Gender :', foreground='#91060F', font=('Cambria', '15'))
        self.gender_label.place(x=435, y=210)

        self.address_label.configure(text='Address', foreground='#91060F', font=('Cambria', '15'))
        self.address_label.place(x=15, y=30)

        self.phonenumber_label.configure(text='Phone Number', foreground='#91060F', font=('Cambria', '15'))
        self.phonenumber_label.place(x=15, y=120)

        self.email_label.configure(text='Email', foreground='#91060F', font=('Cambria', '15'))
        self.email_label.place(x=15, y=210)

        self.father_name_label.configure(text="Father's Name", foreground='#91060F', font=('Cambria', '15'))
        self.father_name_label.place(x=15, y=30)

        self.father_occupation_label.configure(text="Father's Occupation", foreground='#91060F', font=('Cambria', '15'))
        self.father_occupation_label.place(x=765, y=30)

        self.password_label.configure(text="New Password", foreground='#91060F', font=('Cambria', '15'))
        self.password_label.place(x=15, y=30)

        self.passwordconfirm_label.configure(text="Confirm New Password", foreground='#91060F', font=('Cambria', '15'))
        self.passwordconfirm_label.place(x=765, y=30)

    def set_buttons(self):
        self.sign_up_button.configure(text='Sign Up', activeforeground='#91060F', cursor='hand2', width=15,
                                      fg='#AD0712', overrelief='raised', command=self.signUpCallback, relief='groove',
                                      font=('Calibre Light', '20'), highlightcolor='black')
        self.sign_up_button.place(x=630, y=780)

    def run(self):
        self.set_background(1920, 1980)  # dimensions
        self.set_frame()
        self.set_entry()
        self.set_labels()
        self.set_buttons()
        self.root.mainloop()
