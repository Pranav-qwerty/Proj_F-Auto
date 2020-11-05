from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()


def get_val():
    from Write_excel import Write_Patients_DataBase as wb
    a = [name_value.get(), Mother_value.get(), Father_value.get(), gender_value.get(),
         guardian_value.get(), dob_value.get(), address_value.get(), t_address_value.get(),
         Phone_value.get(), Card_no_value.get(), blood_value.get()]
    wb(a)
    showinfo("Info Submitted", f"""The info you have given is submitted.
    Thank you for using!""")

    name_entry.delete(0, 'end')
    Mother_entry.delete(0, 'end')
    Father_entry.delete(0, 'end')
    guardian_entry.delete(0, 'end')
    gender_entry.delete(0, 'end')
    dob_entry.delete(0, 'end')
    Phone_entry.delete(0, 'end')
    Card_no_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    t_address_entry.delete(0, 'end')
    blood_entry.delete(0, 'end')


root.title("Govind Saraswati High School")
root.geometry('750x380')
root.maxsize(750, 380)
root.maxsize(750, 380)
Label(root, text="Govind Saraswati High School", font="comicsans-bold 15 bold", pady=15).grid(row=0, column=4)
name = Label(root, text="Student Name")
Mother = Label(root, text="Mother Name")
Father = Label(root, text="Father Name")
gender = Label(root, text="Sex")
Guardian = Label(root, text="Guardian Name")
dob = Label(root, text="D.O.B")
address = Label(root, text="Permanent Address")
t_address = Label(root, text="Temporary Address")
Phone = Label(root, text="Phone Number")
Card_no = Label(root, text="Aadhaar Card Number")
blood = Label(root, text="Blood Group")

name.grid(row=1, column=2)
Mother.grid(row=1, column=4)
Father.grid(row=2, column=2)
gender.grid(row=2, column=4)
Guardian.grid(row=3, column=2)
dob.grid(row=3, column=4)
address.grid(row=4, column=2)
t_address.grid(row=4, column=4)
Phone.grid(row=5, column=2)
Card_no.grid(row=5, column=4)
blood.grid(row=6, column=2)

name_value = StringVar()
Mother_value = StringVar()
Father_value = StringVar()
gender_value = StringVar()
dob_value = StringVar()
address_value = StringVar()
t_address_value = StringVar()
Phone_value = StringVar()
Card_no_value = StringVar()
blood_value = StringVar()
guardian_value = StringVar()

name_entry = Entry(root, textvariable=name_value)
Mother_entry = Entry(root, textvariable=Mother_value)
Father_entry = Entry(root, textvariable=Father_value)
gender_entry = Entry(root, textvariable=gender_value)
dob_entry = Entry(root, textvariable=dob_value)
address_entry = Entry(root, textvariable=address_value)
t_address_entry = Entry(root, textvariable=t_address_value)
Phone_entry = Entry(root, textvariable=Phone_value)
Card_no_entry = Entry(root, textvariable=Card_no_value)
blood_entry = Entry(root, textvariable=blood_value)
guardian_entry = Entry(root, textvariable=guardian_value)

name_entry.grid(row=1, column=3)
Mother_entry.grid(row=1, column=5)
Father_entry.grid(row=2, column=3)
gender_entry.grid(row=2, column=5)
guardian_entry.grid(row=3, column=3)
dob_entry.grid(row=3, column=5)
address_entry.grid(row=4, column=3)
t_address_entry.grid(row=4, column=5)
Phone_entry.grid(row=5, column=3)
Card_no_entry.grid(row=5, column=5)
blood_entry.grid(row=6, column=3)

# Button
Button(text="Submit", command=get_val, pady=15, padx=19).grid(row=17, column=4)
Label(text="Don't Use commas", ).grid(row=29, column=4)

root.mainloop()
