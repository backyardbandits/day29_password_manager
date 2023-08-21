import os
from tkinter import *
from tkinter import messagebox

# init variables
file = "passwords"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get values
    website = fld_website.get()
    email_username = fld_username.get()
    password = fld_password.get()

    # validate blanks
    blanks = True
    if len(website)==0 or len(email_username)==0 or len(password)==0:
        blanks = True
    else:
        blanks = False

    if blanks is False:
        # concat into one-liner string. concat filename+extension
        global file
        strline = f"{website}|{email_username}|{password}"
        filename = file + ".txt"

        # confirm
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Ok to save? \n\n"
                                                              f"Website: {website}\n"
                                                              f"Email/Username: {email_username}\n"
                                                              f"Password: {password}")

        if is_ok:
            # write (append) file
            with open(filename, "a") as f:
                f.write(strline + "\n")
                # clear fields
                fld_password.delete(0,END)
                fld_username.delete(0,END)
                fld_website.delete(0,END)
                fld_username.insert(0, "@gmail.com")
    else:
        messagebox.showerror(message="Some fields are blank.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=10, pady=10)

# logo image thru canvas
photo_logo = PhotoImage(file="logo.png")
canvas = Canvas (width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo_logo)
canvas.grid(column=1, row=0)

# widgets
fld_website = Entry(width=40)
fld_username = Entry(width=40)
fld_password = Entry(width=31)

lb_website = Label(text="Website:")
lb_username = Label(text="Email/Username:")
lb_password = Label(text="Password:")

bt_genpass = Button(text="Gen Pass")
bt_add = Button(text="Add", width=34, command=save)

# layout in grid
fld_website.grid(column=1, row=1, columnspan=2)
fld_username.grid(column=1, row=2, columnspan=2)
fld_password.grid(column=1, row=3)

lb_website.grid(column=0, row=1)
lb_username.grid(column=0, row=2)
lb_password.grid(column=0, row=3)

bt_genpass.grid(column=2, row=3)
bt_add.grid(column=1, row=4, columnspan=2)

# widget tings
fld_website.focus()
fld_username.insert(0,"@gmail.com")

#
window.mainloop()