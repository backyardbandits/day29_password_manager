from tkinter import *

# init variables


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=20, pady=20)

photo_logo = PhotoImage(file="logo.png")
canvas = Canvas (width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo_logo)
canvas.grid(column=0, row=0)

#
window.mainloop()