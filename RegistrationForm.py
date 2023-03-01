import tkinter as t
import tkinter.messagebox


class RegistrationGUI:
    def __init__(self):
        self.main_window = t.Tk()
        self.main_window.geometry("500x600")
        self.main_window.title("Responsive Registration Form")
        px = 8
        py = 8

        # title label
        self.title_label = t.Label(
            self.main_window,
            text="Responsive Registration\nForm\n",
            font="arial 24 bold",
        )
        self.title_label.pack()

        # frames
        self.email_frame = t.Frame(self.main_window)
        self.password_frame = t.Frame(self.main_window)
        self.retype_pw_frame = t.Frame(self.main_window)
        self.name_frame = t.Frame(self.main_window)
        self.gender_frame = t.Frame(self.main_window)
        self.checks_frame = t.Frame(self.main_window)
        self.register_frame = t.Frame(self.main_window)

        self.email_frame.pack(padx=px, pady=py)  # padding
        self.password_frame.pack(padx=px, pady=py)
        self.retype_pw_frame.pack(padx=px, pady=py)
        self.name_frame.pack(padx=px, pady=py)
        self.gender_frame.pack(padx=px, pady=py)
        self.checks_frame.pack(padx=px, pady=py)
        self.register_frame.pack(padx=px, pady=py)

        # email input box
        self.prompt_email_label = t.Label(
            self.email_frame, text="Email:", font="arial 12 bold"
        )
        self.email_entry = t.Entry(self.email_frame, width=40, font="arial 12")
        self.prompt_email_label.pack(side="left")
        self.email_entry.pack(side="left")

        # password input box
        # with passwords masked (*****) validation
        self.prompt_password_label = t.Label(
            self.password_frame, text="Password:", font="arial 12 bold"
        )
        self.password_entry = t.Entry(
            self.password_frame,
            show="*",
            width=36,
            font="arial 12",  # show='*' to mask input
        )
        self.prompt_password_label.pack(side="left")
        self.password_entry.pack(side="left")

        # retype pw input box
        # with passwords masked (*****) validation
        self.prompt_retype_pw_label = t.Label(
            self.retype_pw_frame, text="Re-type Password:", font="arial 12 bold"
        )
        self.retype_pw_entry = t.Entry(
            self.retype_pw_frame,
            show="*",
            width=29,
            font="arial 12",  # show='*' to mask input
        )
        self.prompt_retype_pw_label.pack(side="left")
        self.retype_pw_entry.pack(side="left")

        # name input box(s)
        self.prompt_fname_label = t.Label(
            self.name_frame, text="First Name:", font="arial 12 bold"
        )
        self.fname_entry = t.Entry(self.name_frame, width=12, font="arial 12")
        self.prompt_fname_label.pack(side="left")
        self.fname_entry.pack(side="left")

        self.prompt_lname_label = t.Label(
            self.name_frame, text=" Last Name:", font="arial 12 bold"
        )
        self.lname_entry = t.Entry(self.name_frame, width=12, font="arial 12")
        self.prompt_lname_label.pack(side="left")
        self.lname_entry.pack(side="left")

        # gender radio buttons
        self.radio_var = t.StringVar()
        self.rb1 = t.Radiobutton(
            self.gender_frame,
            text="Male",
            variable=self.radio_var,
            value="Male",
            font="arial 12 bold",
        )
        self.rb2 = t.Radiobutton(
            self.gender_frame,
            text="Female",
            variable=self.radio_var,
            value="Female",
            font="arial 12 bold",
        )
        self.rb1.pack(side="left")
        self.rb2.pack(side="left")

        # checks check boxes
        self.cb_var1 = t.IntVar()  # one variable per check box
        self.cb_var2 = t.IntVar()
        self.cb1 = t.Checkbutton(
            self.checks_frame,
            text="I agree with terms and conditions",
            variable=self.cb_var1,
            font="arial 12 bold",
        )
        self.cb2 = t.Checkbutton(
            self.checks_frame,
            text="I want to receive the newsletter",
            variable=self.cb_var2,
            font="arial 12 bold",
        )
        self.cb1.pack()
        self.cb2.pack()

        # register button
        self.register_button = t.Button(
            self.register_frame,
            text="Register",
            command=self.confirmation,
            width=25,
            bg="gold",
            font="arial 20 bold",
        )
        self.register_button.pack()

        t.mainloop()

    def confirmation(self):
        # gender validation
        if self.radio_var.get() != "Null":
            self.gender_msg = "Gender is selected"
        else:
            self.gender_msg = "Please select a gender"

        # both checks validation
        if self.cb_var1.get() and self.cb_var2.get() == 1:
            self.checks_msg = "Both checkboxes are checked"
        else:
            self.checks_msg = "One or both checkboxes have not been checked"

        # passwords match validation
        if self.password_entry.get() == self.retype_pw_entry.get():
            self.pw_msg = "Password and re-type password match"
        else:
            self.pw_msg = "Password and re-type password do NOT match"

        tkinter.messagebox.showinfo(
            "Confirmation",
            self.gender_msg + "\n" + self.checks_msg + "\n" + self.pw_msg,
        )


myinstance = RegistrationGUI()

print("Thank you for submitting a responsive registration form!")
