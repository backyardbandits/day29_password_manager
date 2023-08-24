import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import pyperclip
import json

# init variables
file = "passwords"
file_ext = "json"
filetypes = ["json","txt"]
words = []
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_chars = 6
min_digits = 3

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# read file containing top words
with open('top_words.txt', 'r') as f:
    # Read the content of the file
    content = f.read()

    # Split the content into words using spaces as separators
    words = content.split()

    # Convert all words to lowercase using a list comprehension
    words_lower = [word.lower() for word in words]

def gen_pass():
    password = ""

    # get words until min chars is reached
    while len(password) < min_chars:
        # get random word, capitalize first char
        password += words[random.randint(0, len(words)-1 )].capitalize()

    # get 3 digit num
    for x in range(min_digits):
        # get random digit, concat to str
        password += str(digits[random.randint(0, len(digits)-1 )])

    fld_password.delete(0, END)
    fld_password.insert(0, password)
    pyperclip.copy(password)

    print(f"pass: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_fields():
    # clear fields
    fld_password.delete(0, END)
    fld_username.delete(0, END)
    fld_website.delete(0, END)
    fld_username.insert(0, "@gmail.com")

def save():
    # get values
    website = fld_website.get()
    email_username = fld_username.get()
    password = fld_password.get()

    # validate blanks
    if len(website)==0 or len(email_username)==0 or len(password)==0:
        messagebox.showerror(message="Some fields are blank.")
    else:
        # concat filename+extension
        global file
        filename = file + "." + file_ext

        # confirm save
        is_ok = True
        # is_ok = messagebox.askokcancel(title="Confirmation", message=f"Ok to save? \n\n"
        #                                                       f"Website: {website}\n"
        #                                                       f"Email/Username: {email_username}\n"
        #                                                       f"Password: {password}")

        if is_ok:
            if file_ext == "json":
                # put values into a dict
                new_data = {
                    website :{
                        "email_username": email_username,
                        "password": password
                    }
                }

                # WRITE JSON FILE
                try:
                    # read current data
                    with open(filename, "r") as json_file:
                        data = json.load(json_file)

                except FileNotFoundError:
                    print(f"File not found. Creating file: {filename}")
                    # save new
                    with open(filename, "w") as json_file:
                        json.dump(new_data, json_file, indent=4)

                else:
                    # update old data with new data entry (append)
                    data.update(new_data)

                    # save updated
                    with open(filename, "w") as json_file:
                        json.dump(data, json_file, indent=4)

                clear_fields()

            else:
                # write (append) file
                strline = f"{website}|{email_username}|{password}"
                with open(filename, "a") as f:
                    f.write(strline + "\n")

                clear_fields()

# ---------------------------- SEARCH ------------------------------- #
def search_pass():
    filename = file + "." + file_ext
    website = fld_website.get()
    msg_prefix = "[SEARCH]"

    try:
        # read current data
        with open(filename, "r") as json_file:
            data = json.load(json_file)
        data_entry = data[website]
        password = data_entry["password"]

        password_msg = f"{msg_prefix} Password searched: {password}"
        print(password_msg)
        # messagebox.showinfo(message=password_msg)

    except KeyError:
        msg = f"{msg_prefix} No entry found for website: {website}"
        print(msg)
        # messagebox.showinfo(message=msg)
    except FileNotFoundError:
        error_msg = f"{msg_prefix} Error reading file: {filename}"
        print(error_msg)
        # messagebox.showerror(error_msg)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=10, pady=10)

# logo image thru canvas
photo_logo = PhotoImage(file="logo.png")
canvas = Canvas (width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo_logo)
canvas.grid(column=1, row=0)

# set widgets
# drop down filetype
def on_filetypes_select(event):
    global file_ext
    selected_item = filetypes_var.get()
    print(f"selected item: {selected_item}")
    file_ext = selected_item

filetypes_var = StringVar()
drp_filetype = ttk.Combobox(window, textvariable=filetypes_var, values=filetypes, width=10)
drp_filetype.set("json")
drp_filetype.bind("<<ComboboxSelected>>", on_filetypes_select)  # Event handler

fld_website = Entry(width=31)
fld_username = Entry(width=40)
fld_password = Entry(width=31)

lb_filetype = Label(text="File Type:")
lb_website = Label(text="Website:")
lb_username = Label(text="Email/Username:")
lb_password = Label(text="Password:")

bt_search = Button(text="Search", command=search_pass)
bt_genpass = Button(text="Gen Pass", command=gen_pass)
bt_add = Button(text="Add", width=34, command=save)

# layout in grid
drp_filetype.grid(column=1, row=5, sticky="W")
fld_website.grid(column=1, row=1, sticky="W")
fld_username.grid(column=1, row=2, columnspan=2, sticky="W")
fld_password.grid(column=1, row=3, sticky="W")

lb_filetype.grid(column=0, row=5, sticky="W")
lb_website.grid(column=0, row=1, sticky="W")
lb_username.grid(column=0, row=2, sticky="W")
lb_password.grid(column=0, row=3, sticky="W")

bt_search.grid(column=2, row=1, sticky="W")
bt_genpass.grid(column=2, row=3, sticky="W")
bt_add.grid(column=1, row=4, columnspan=2, sticky="W")

# widget default config
fld_website.focus()
fld_username.insert(0,"@gmail.com")

#
window.mainloop()