from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox


# --------------------------------- PASSWORD GENERATOR ----------------------------#
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_text.insert(0, password)


# --------------------------------- SAVE PASSWORD ----------------------------#
def save():
    web = website_text.get()
    email = email_text.get()
    password = password_text.get()
    if len(web) == 0 or len(password) <= 0:
        messagebox.showerror(title="Error", message="You cant leave the fields blank.\nPlease enter valid details.")
    else:
        if messagebox.askokcancel(title=web,
                                  message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?"):
            with open("./password.txt", mode='a') as password_file:
                password_file.write(f"{web} | {email} | {password}\n")
            website_text.delete(0, END)
            password_text.delete(0, END)


# --------------------------------- UI SETUP ----------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_text = Entry(width=45)
website_text.grid(row=1, column=1, columnspan=2)
email_text = Entry(width=45)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "Tarunpatnala@gmail.com")
password_text = Entry(width=26)
password_text.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", width=15, command=password_generator)
gen_pass.grid(row=3, column=2)
add = Button(text="Add", width=38, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
