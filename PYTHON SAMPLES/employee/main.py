
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from db import Database
import re



db = Database("Employee.db")     #connection to database

class Employee:
    def __init__(self, main):
        self.main = main


        self.T_Frame = Frame(self.main, height=30, width=1366, bg="black", bd=2, relief="groove")
        self.T_Frame.pack()

        self.Title = Label(self.T_Frame, text="EMPLOYEE MANAGEMENT SYSTEM", font="ariel 20 bold", width=1366, bg="white", fg="black")
        self.Title.pack()

        self.Frame1 = Frame(self.T_Frame, height=350, width=1366, bd=2, relief="groove", bg="navy")
        self.Frame1.pack()


        self.Name = Label(self.Frame1, text="Name", font=("Calibri", 18), bg="navy", fg="white")
        self.Name.place(x=50, y=10)
        self.Name_Entry = Entry(self.Frame1, width=50, bg="white", fg="black")
        self.Name_Entry.place(x=180, y=20, height=24)
        self.Name_Entry.bind("<KeyRelease>", self.validate_name)
        self.name_error = Label(self.Frame1, text="", font=("Calibri", 10), fg="red", bg="navy")
        self.name_error.place(x=180, y=45)



        self.age = Label(self.Frame1, text="Age", font=("Calibri", 18), bg="navy", fg="white")
        self.age.place(x=700, y=10)
        self.age_Entry = Entry(self.Frame1, width=50, bg="white", fg="black")
        self.age_Entry.place(x=850, y=20, height=24)
        self.age_Entry.bind("<KeyRelease>", self.validate_age)
        self.age_error = Label(self.Frame1, text="", font=("Calibri", 10), fg="red", bg="navy")
        self.age_error.place(x=850, y=45)


        self.DOJ = Label(self.Frame1, text="D.O.J", font=("Calibri", 18), bg="navy", fg="white")
        self.DOJ.place(x=50, y=70)
        self.DOJ_Entry = DateEntry(self.Frame1, width=47, bg="white", date_pattern="dd/MM/yyyy", fg="black")
        self.DOJ_Entry.place(x=180, y=78, height=25)
        self.DOJ_Entry.bind("<<DateEntrySelected>>", self.validate_doj)  # Only for tkcalendar.DateEntry

        self.gender = Label(self.Frame1, text="Gender", font=("Calibri", 18), bg="navy", fg="white")
        self.gender.place(x=50, y=125)
        self.gender_combo = ttk.Combobox(self.Frame1, font=("Calibri", 11), width=40, state="readonly",style="Gender.TCombobox")
        self.gender_combo['values'] = ("Male","Female")  # Include 'Select Gender'
        self.gender_combo.set("Select Gender")
        self.gender_combo.configure(background="white")
        self.gender_combo.place(x=180, y=134, height=24)
        self.gender_combo.bind("<<ComboboxSelected>>", self.validate_gender)
        self.gender_error = Label(self.Frame1, text="", fg="red", font=("Calibri", 10), bg="navy")
        self.gender_error.place(x=180, y=160)

        self.email = Label(self.Frame1, text="Gmail", font=("Calibri", 18), bg="navy", fg="white")
        self.email.place(x=700, y=70)
        self.email_Entry = Entry(self.Frame1, width=50, bg="white")
        self.email_Entry.place(x=850, y=76, height=24)
        self.email_Entry.bind("<KeyRelease>", self.validate_email)
        self.email_error = Label(self.Frame1, text="", font=("Calibri", 10), fg="red", bg="navy")
        self.email_error.place(x=850, y=105)


        self.contact = Label(self.Frame1, text="Contact.No", font=("Calibri", 18), bg="navy", fg="white")
        self.contact.place(x=700, y=125)
        self.contact_Entry = Entry(self.Frame1, width=50, bg="white")
        self.contact_Entry.place(x=850, y=130, height=24)
        self.contact_Entry.bind("<KeyRelease>", self.validate_contact)
        self.contact_error = Label(self.Frame1, text="", font=("Calibri", 10), fg="red", bg="navy")
        self.contact_error.place(x=850, y=155)


        self.address = Label(self.Frame1, text="Address", font=("Calibri", 18), bg="navy", fg="white")
        self.address.place(x=50, y=180)
        self.address_Entry = Text(self.Frame1, width=70, height=4, font=("Calibri", 14), bg="white")
        self.address_Entry.place(x=160, y=190)
        self.address_Entry.bind("<KeyRelease>", self.validate_address)
        self.address_error = Label(self.Frame1, text="", font=("Calibri", 10), fg="red", bg="navy")
        self.address_error.place(x=168, y=287)


        self.button_Frame = Frame(self.T_Frame, height=50, width=1366, bg="navy")
        self.button_Frame.place(x=50, y=337)
        self.add_btn = Button(self.button_Frame, text="Add Details", font=("Calibri", 14), bg="green", fg="white", command=self.add_employee)
        self.add_btn.grid(row=0, column=0, padx=10, pady=5)

        self.button_Frame = Frame(self.T_Frame, height=50, width=400, relief="sunken", bg="navy")
        self.button_Frame.place(x=300, y=337)
        self.update_btn = Button(self.button_Frame, text="Update Details", font=("Calibri", 14), bg="gold", fg="white",command=self.update_employee)
        self.update_btn.pack(padx=10, pady=5)

        self.button_Frame = Frame(self.T_Frame, height=50, width=400, relief="sunken", bg="navy")
        self.button_Frame.place(x=560, y=337)
        self.delete_btn = Button(self.button_Frame, text="Delete Details", font=("Calibri", 14), bg="red", fg="white",command=self.delete_employee)
        self.delete_btn.pack(padx=10, pady=5)

        self.button_Frame = Frame(self.T_Frame, height=50, width=400, relief="sunken", bg="navy")
        self.button_Frame.place(x=800, y=337)
        self.clear_btn =Button(self.button_Frame, text="clear Details", font=("Calibri", 14), bg="purple",command=self.clear_all,fg="white")
        self.clear_btn.pack(padx=10, pady=5)



        self.search_label = Label(self.Frame1, text="Search:", font=("Calibri", 14), fg="white", bg="navy")
        self.search_label.place(x=950, y=215)
        self.search_entry = Entry(self.Frame1, width=50, bg="light yellow", fg="black")
        self.search_entry.place(x=1020, y=218, height=24)
        self.search_entry.bind("<KeyRelease>", self.perform_search)



        tree_frame = Frame(self.main)
        tree_frame.pack(fill="both", expand=True)


        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)



        self.tree = ttk.Treeview(tree_frame, columns=("c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7"), show="headings",
                                 height=6, yscrollcommand=tree_scroll.set) #link tree view to scrollbar
        tree_scroll.config(command=self.tree.yview)#scroll bar control


        col_names = {
            "c0": "ID",
            "c1": "NAME",
            "c2": "AGE",
            "c3": "DOJ",              #dictionary
            "c4": "GMAIL",
            "c5": "GENDER",
            "c6": "CONTACT",
            "c7": "ADDRESS"
        }

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col_names[col], command=lambda _col=col: self.sort_treeview(_col, False))
            self.tree.column("c0", anchor=CENTER, width=50)
            self.tree.column("c1", anchor=CENTER, width=100)
            self.tree.column("c2", anchor=CENTER, width=70)
            self.tree.column("c3", anchor=CENTER, width=100)
            self.tree.column("c4", anchor=CENTER, width=150)
            self.tree.column("c5", anchor=CENTER, width=80)
            self.tree.column("c6", anchor=CENTER, width=120)
            self.tree.column("c7", anchor=W, width=300)

            self.tree.bind("<ButtonRelease-1>", self.on_tree_select) #left click on mouse
            self.tree.pack(fill="both", expand=True)
            self.display_all()

        style = ttk.Style()
        style.theme_use("default")


    def add_employee(self):

        self.name_error.config(text="")     #clears all before errors
        self.age_error.config(text="")
        self.email_error.config(text="")
        self.contact_error.config(text="")
        self.address_error.config(text="")
        self.gender_error.config(text="")



        name = self.Name_Entry.get().strip()    #gets input from user
        age = self.age_Entry.get().strip()
        email = self.email_Entry.get().strip()
        contact = self.contact_Entry.get().strip()
        address = self.address_Entry.get("1.0", END).strip()
        doj = self.DOJ_Entry.get().strip()
        gender = self.gender_combo.get().strip()

        if not all([name, age, email, contact, address, doj]) or gender == "Select Gender":  #checks if there is any empty entry
            messagebox.showerror("Input Error", "Please enter all details before submitting.")
            if gender == "Select Gender":
                self.gender_error.config(text="Please select gender.")
                self.gender_combo.configure(style="Red.TCombobox")
            return

        valid = True

        valid = True


        if not re.fullmatch(r"[A-Za-z\s]+", name):
            self.name_error.config(text="Only letters allowed.")
            valid = False

        try:
            age_val = int(age)
            if not (18 <= age_val <= 50):
                self.age_error.config(text="Age must be 18‑50.")
                valid = False
        except:
            self.age_error.config(text="Invalid number.")
            valid = False

        if not re.fullmatch(r"[\w.%+-]+@gmail\.com", email):
            self.email_error.config(text="Must be a Gmail.")
            valid = False

        if not re.fullmatch(r"\d{10}", contact):
            self.contact_error.config(text="10-digit required.")
            valid = False

        if not len(address)>5 :
            self.address_error.config(text="Address must be at least 10 characters.")
            valid = False

        if not valid:
            messagebox.showinfo("Wrong details", "please  enter correct details.")
            return

        success = db.insert(name, age, doj, email, gender, contact, address)

        if success:
            messagebox.showinfo("Success", f"Employee '{name}' added successfully!")
            self.display_all()
            return


        if not success:
            messagebox.showerror("Duplicate Entry", "This employee already exists in the database.")
            return

        if not self.validate_gender():
            return



        #self.clear_all()
        self.display_all()



    def clear_errors(self): #clears all the error label
        self.name_error.config(text="")
        self.age_error.config(text="")
        self.email_error.config(text="")
        self.contact_error.config(text="")
        self.address_error.config(text="")
        self.gender_error.config(text="")


    def display_all(self):
        self.tree.delete(*self.tree.get_children())  # clears all current rows in treeview
        for row in db.fetch():  #return employee data
            self.tree.insert("", END, values=row) #"" start from ID colum,END= places row at bottom

    def delete_employee(self):
        selected_item = self.tree.focus() #checks and gets the selected item
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return
        values = self.tree.item(selected_item, "values")
        emp_id = values[0]  #extracting the id column of selected row

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete employee ID {emp_id}?")
        if confirm:
            db.remove(int(emp_id))
            self.tree.delete(selected_item)
            self.clear_all()

    def update_employee(self):

        name = self.Name_Entry.get().strip()  #taking the input from the user
        age = self.age_Entry.get().strip()
        email = self.email_Entry.get().strip()
        contact = self.contact_Entry.get().strip()
        address = self.address_Entry.get("1.0", END).strip()
        doj = self.DOJ_Entry.get().strip()
        gender = self.gender_combo.get().strip()

        selected_item = self.tree.focus()  #check if the row is selected
        if not selected_item: #checks for a record to select
            messagebox.showerror("Error", "Please select a record to update.")
            return

        values = self.tree.item(selected_item, "values")
        emp_id = values[0]   #extractinng the id column of selected row

        if not all([name, age, email, contact, address, doj, gender]): #checks for the empty entry
            messagebox.showerror("Missing Data", "Please fill all the fields before updating.")
            return

        if (    #existing values==new input values
                values[1].strip() == name and
                values[2].strip() == age and
                values[3].strip() == doj and
                values[4].strip() == email and
                values[5].strip() == gender and
                values[6].strip() == contact and
                values[7].strip() == address
        ):
            messagebox.showerror("Error", "Cannot update with same employee details.")
            return

        confirm = messagebox.askyesno("Confirm Update", f"Are you sure you want to update employee ID {emp_id}?")
        if not confirm:
            return

        if not self.validate_gender():
            return

        valid = db.update(emp_id, name, age, doj, email, gender, contact, address)
        if valid:    #update database
            self.display_all()
            messagebox.showinfo("Success", f"Employee ID {emp_id} updated successfully!")
            return

    def on_tree_select(self, event):
        selected_item = self.tree.focus()  #checks if any record is selected
        if not selected_item:
            return

        values = self.tree.item(selected_item, "values")

        self.Name_Entry.delete(0, END)  #remove recordd
        self.Name_Entry.insert(0, values[1]) # fills the value

        self.age_Entry.delete(0, END)
        self.age_Entry.insert(0, values[2])

        # If using DateEntry from tkcalendar
        try:
            self.DOJ_Entry.set_date(values[3])
        except:
            self.DOJ_Entry.delete(0, END)
            self.DOJ_Entry.insert(0, values[3])

        self.email_Entry.delete(0, END)
        self.email_Entry.insert(0, values[4])

        self.gender_combo.set(values[5])
        self.validate_gender()

        self.contact_Entry.delete(0, END)
        self.contact_Entry.insert(0, values[6])

        self.address_Entry.delete("1.0", END)
        self.address_Entry.insert("1.0", values[7])


    def clear_all(self):
        self.Name_Entry.delete(0, END)    #clears entry from starting to end
        self.age_Entry.delete(0, END)
        self.email_Entry.delete(0, END)
        self.contact_Entry.delete(0, END)
        self.address_Entry.delete("1.0", END)  # clears multi line error

        self.name_error.config(text="")  #clears the previous validatiion errors
        self.age_error.config(text="")
        self.email_error.config(text="")
        self.contact_error.config(text="")
        self.address_error.config(text="")

        try:
            self.DOJ_Entry.set_date("")  # reset date
        except:
            self.DOJ_Entry.delete(0, END)

        self.gender_combo.set("Select Gender")
        self.gender_combo.configure(background="white")  # reset gender

        # Reset field backgrounds
        self.Name_Entry.config(bg="white")
        self.age_Entry.config(bg="white")
        self.email_Entry.config(bg="white")
        self.contact_Entry.config(bg="white")
        self.address_Entry.config(bg="white")

        # Clear error labels
        self.name_error.config(text="")
        self.age_error.config(text="")
        self.email_error.config(text="")
        self.contact_error.config(text="")
        self.address_error.config(text="")
        self.gender_error.config(text="")


    def validate_name(self, event):
        self.clear_errors()
        name = self.Name_Entry.get().strip()

        if not name:
            self.name_error.config(text="Name is required.")
            self.Name_Entry.config(bg="red")
            return

        if not re.fullmatch(r"[A-Za-z\s]+", name):
            self.name_error.config(text="Only letters allowed.")
            self.Name_Entry.config(bg="red")
            return


        self.Name_Entry.config(bg="light green")
        return



    def validate_age(self, event):
        self.clear_errors()
        age = self.age_Entry.get()
        if not age.isdigit() or not (18 <= int(age) <= 50):
            self.age_error.config(text="Age must be 18-50.")

        is_valid= not age.isdigit()  or not (18 <= int(age) <= 50)
        if   is_valid:
           self.age_Entry.config(bg="red")
           return
        else:
           self.age_Entry.config(bg="light green")


    def validate_email(self, event):
        self.clear_errors()
        email = self.email_Entry.get()
        if not re.fullmatch(r"[\w.%+-]*@gmail\.com", email):
            self.email_error.config(text="Enter valid Gmail.")

        is_valid= not re.fullmatch(r"[\w.%+-]*@gmail\.com", email)

        if  is_valid:
            self.email_Entry.config(bg="red")
            return
        else:
            self.email_Entry.config(bg="light green")
            return


    def validate_contact(self, event):
        self.clear_errors()
        contact = self.contact_Entry.get()

        if not contact.isdigit() or len(contact) != 10:
            self.contact_error.config(text="10 digit contact only.")
            self.contact_Entry.config(bg="red")
            return

        # If valid
        self.contact_Entry.config(bg="light green")
        self.contact_error.config(text="")


    def validate_address(self, event):
        self.clear_errors()
        address = self.address_Entry.get("1.0", END).strip()
        if not len(address) > 5:
            self.address_error.config(text="Address too short.")
        is_valid =not len(address) >5

        if is_valid:
            self.address_Entry.config(bg="red")
            return

        else:
            self.address_Entry.config(bg="light green")


    def validate_gender(self, event=None):
        selected_gender = self.gender_combo.get()

        if selected_gender == "Select Gender":
            self.gender_combo.configure(background="red")
            self.gender_error.config(text="Please select gender.")
            return False
        else:
            self.gender_combo.configure(background="light green")
            self.gender_error.config(text="")
            return True

    def validate_doj(self, event=None):
        from datetime import datetime

        doj = self.DOJ_Entry.get().strip()

        if doj:
            try:
                # Adjust the format if your DateEntry uses a different one
                datetime.strptime(doj, "%m/%d/%Y")  # Default format in tkcalendar
                self.DOJ_Entry.configure(background="light green")
                self.doj_error.config(text="")  # Optional: clear error label
            except ValueError:
                self.DOJ_Entry.configure(background="red")
                self.doj_error.config(text="Invalid Date")
        else:
            self.DOJ_Entry.configure(background="red")
            self.doj_error.config(text="DOJ is required")


    def update_treeview(self, records):
        # First clear the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new sorted records
        for record in records:
            self.tree.insert('', END, values=record)

    def sort_treeview(self, col, reverse):
        from datetime import datetime

        data = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]

        try:
            if col in ["c0", "c2"]:  # ID or Age
                # Safely try converting to int, fallback to 0 if invalid
                data.sort(key=lambda t: int(t[0]) if t[0].isdigit() else 0, reverse=reverse)

            elif col == "c3":  # DOJ (Date of Joining)
                def safe_date(d):
                    try:
                        return datetime.strptime(d.replace("-", "/"), "%d/%m/%Y")
                    except:
                        return datetime.min  # push invalid/empty dates to top/bottom

                data.sort(key=lambda t: safe_date(t[0]), reverse=reverse)

            else:
                data.sort(key=lambda t: t[0].lower(), reverse=reverse)

        except Exception as e:
            print("Sort Error:", e)
            return

        for index, (val, k) in enumerate(data):
            self.tree.move(k, '', index)

        self.tree.heading(col, command=lambda: self.sort_treeview(col, not reverse))

    def perform_search(self, event=None):
        query = self.search_entry.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)


        records = db.fetch()
        for row in records:
            if any(query in str(field).lower() for field in row):
                self.tree.insert("", "end", values=row)


main = Tk()
main.title("Employee Management System")
main.geometry("1366x768+0+0")
main.state("zoomed")
Employee(main)
main.mainloop()
