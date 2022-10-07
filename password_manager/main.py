from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

def search():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(message="No passwords saved yet")
    else:
        search_text = website.get()
        
        if search_text in data:
            messagebox.showinfo(message= f"email: {data[search_text]['email']}\n password: {data[search_text]['password']}")
            pyperclip.copy(data[search_text]['password'])
        else:
            messagebox.showinfo(message= f"Password not saved for {search_text}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_function():
    password.delete(0,END)
    new_password = generate_password()
    password.insert(0,new_password)
    pyperclip.copy(new_password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def save():

    website_value = website.get()
    email_value = email.get()
    password_value = password.get()

    if website_value == '' or email_value == '' or password_value == '':
        messagebox.showerror(title="Error", message="Fields should not be empty")
        return

    
    response = messagebox.askokcancel(message="Do you want to save?")

    if response:
        new_data = {
            website_value: {
                "email": email_value,
                "password": password_value
            }
        }

        print(new_data)
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json","w") as data_file:
                data = {}
        data.update(new_data)
        
        with open("data.json","w") as data_file:
            json.dump(data,data_file,indent=4)

        website.delete(0,END)
        password.delete(0,END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="password_manager/logo.png")


canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

lb_website = Label(text="Website:")
lb_website.grid(column=0,row=1)

website = Entry()
website.grid(row=1,column=1)
website.focus()

search_button = Button(text="Search",width=13,command=search)
search_button.grid(row=1,column=2)

lb_email = Label(text="Email/Username:")
lb_email.grid(column=0,row=2)

email = Entry(width=37)
email.grid(row=2,column=1,columnspan=2)
email.insert(0,"abc@example.com")

lb_password = Label(text="Password:")
lb_password.grid(row=3, column=0)

password = Entry(width=21)
password.grid(row=3,column=1)

generate_password_entry = Button(text="Generate Password",command=generate_password_function)
generate_password_entry.grid(row=3, column=2)


add = Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)


window.mainloop()
