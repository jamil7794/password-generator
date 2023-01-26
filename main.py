from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
window.config(padx=20, pady=20)
canvas.grid(row=0, column=1)


website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email")
email_label.grid(row=2, column=0)
password_label = Label(text="Pasword")
password_label.grid(row=3, column=0)


website_Entry = Entry(width=35)
website_Entry.grid(row=1, column=1, columnspan=2)
website_Entry.focus()
email_Entry = Entry(width=35)
email_Entry.grid(row=2, column=1, columnspan=2)
email_Entry.insert(0,"jamiljalal7794@gmail.com")
password_Entry = Entry(width=21)
password_Entry.grid(row=3, column=1)




generatePassButton = Button(text="Generate Password")
generatePassButton.grid(row=3, column=2, columnspan=2)
addButton = Button(text="Add",width=35)
addButton.grid(row=4, column=1, columnspan=2)

def save():
    pass
  

window.mainloop()