from tkinter import *

# init variables


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=20, pady=20)

# logo image thru canvas
photo_logo = PhotoImage(file="logo.png")
canvas = Canvas (width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo_logo)
canvas.grid(column=0, row=0)

fld_website = Entry(width=35)
fld_username = Entry(width=35)
fld_password = Entry(width=21)
lb_website = Label(text="Website")
lb_username = Label(text="Email/Username")
lb_password = Label(text="Password")
bt_genpass = Button(text="Generate Password")
bt_add = Button(text="Add", width=36)

fld_website.grid(column=1, row=1, columnspan=2)
fld_username.grid(column=, row=)
fld_password.grid(column=, row=)
lb_website.grid(column=, row=)
lb_username.grid(column=, row=)
lb_password.grid(column=, row=)
bt_genpass.grid(column=, row=)
bt_add.grid(column=, row=)



#
window.mainloop()