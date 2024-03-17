from tkinter import messagebox
from tkinter import *
import random
import os
import json

BG = "#00224D"
TEXT_COLOR = "#A0153E"

english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
english_alphabet.extend([letter.upper() for letter in english_alphabet])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["+", "%", "&", "/", "_", "-", "*"]
previous_mail = ""
try:
    with open("data.json", "r") as file:
        data = file.readlines()
except:
    pass
else:
    last_email=data[len(data)-4]
    mail=last_email.split('"email": "')
    mail=mail[1].split('",')
    previous_mail=mail[0]

def search():
    website = website_input.get().capitalize()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo("Info", message=f"Email : {email}\n"
                                                f"Password : {password}")
        else:
            messagebox.showinfo("Warning!", message=f"Could not find any data for {website}")

    except:
        messagebox.showinfo("Warning!", message="Could not find any data file")



def generate_password():
    nr_letters = random.randint(6, 8)
    nr_numbers = random.randint(3, 5)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(english_alphabet) for _ in range(nr_letters)]
    password_numbers = [str(random.choice(numbers)) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password = password_numbers + password_symbols + password_letters

    random.shuffle(password)

    last_password = "".join(password)

    password_input.delete(0, END)
    password_input.insert(0, last_password)


def add():
    website = website_input.get().capitalize()
    email = email_input.get()
    password = password_input.get()
    if website!="" and email!="" and password!="":
        messagebox.showinfo("Warning",message="Your informations are saved!")
        data_dict = {website:
            {
                "email": email,
                "password": password
            }
        }
        try:
            with open("data.json", "r") as data:
                old_data=json.load(data)
                old_data.update(data_dict)
        except:
            with open("data.json","w") as data:
                json.dump(data_dict,data,indent=4)
        else:
            with open("data.json","w") as data:
                json.dump(old_data,data,indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
    else:
        messagebox.showinfo("Warning!","Please fiil the all blanks")


window = Tk()
window.minsize()
window.title("RandPass")
window.config(padx=50, pady=30, bg=BG)

canvas = Canvas(height=200, width=200, bg=BG, highlightthickness=0)
my_photo = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=my_photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BG)
website_label.grid(row=1, column=0)

website_input = Entry(width=10)
website_input.grid(row=1, column=1, sticky="EW")

search_button = Button(text="search", width=42, command=search)
search_button.grid(row=1, column=2, sticky="EW", padx=2, ipadx=10)

email_username_label = Label(text="Email-Username:", font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BG)
email_username_label.grid(row=2, column=0)

email_input = Entry(width=48)
email_input.insert(0, previous_mail)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:", font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BG)
password_label.grid(row=3, column=0)

password_input = Entry(width=10)
password_input.grid(row=3, column=1, sticky="EW")

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW", padx=2, ipadx=10)

add_button = Button(text="Add", width=41, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
