from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list +=[choice(symbols) for symbol in range(randint(2, 4))]
    password_list +=[choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    entrypassword.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entrywebsite.get()
    email = entryemail.get()
    password =entrypassword.get()
    newdata ={
        website:{
        "email": email,
        "password" :password
         }
    }
    if website == ""or email == "" or password == "":
        messagebox.showerror('Oops', "Please don't leave any fields blank")
    else:
        if messagebox.askokcancel(title ='the title', message=f'this is the email {email}, this is the password {password}. Do you wish to submit?'):
            try:
                with open("password-manager-start/data.json", "r",) as datafile:
                    data = json.load( datafile)
                    data.update(newdata)
            except FileNotFoundError:
                with open("password-manager-start/data.json", "w",) as datafile:
                    json.dump(newdata, datafile, indent=4)
            else:
                with open("password-manager-start/data.json", "w",) as datafile:
                    json.dump(data, datafile, indent=4)
            finally:
                entrywebsite.delete(0,END)
                entrypassword.delete(0,END)


#---- SEARCH FUNCTIONALITY ---------#
def search():
        website = entrywebsite.get()
        email = entryemail.get()
        if website == "" or email == "":
             messagebox.showerror('Oops', "Please don't leave any fields blank")
        else:
            try:
                with open("password-manager-start/data.json", "r",) as datafile:
                    data = json.load( datafile)
                    password = data[website]["password"]
                    messagebox.showinfo('Password', f'Your password is {password}')       
            except FileNotFoundError:
                messagebox.showerror('Oops', "You've not saved any passwords")
            except KeyError:
                messagebox.showerror('Oops', "You've not saved any passwords for this site")
                




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas= Canvas(width=200, height= 200)
padlock_img =PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100, 100, image = padlock_img)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:")
website_label.grid(row=2, column=1)
emailuser_label = Label(text="Email/Username:",)
emailuser_label.grid(row=3, column=1)
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)



entrywebsite = Entry(width=21)
entrywebsite.focus()
entrywebsite.grid(row=2,column = 2, columnspan=1)

entryemail= Entry(width=38)
entryemail.insert(0,'username@email.com')
entryemail.grid(row=3,column = 2, columnspan=2)

entrypassword = Entry(width=21)
entrypassword.grid(row=4,column = 2,)

genpasswordbutton = Button(text="Generate Password", command=generatepassword )
genpasswordbutton.grid(row=4, column=3)

addnewbutton = Button(text = "Add", width= 36, command= save)
addnewbutton.grid(row=5, column=2, columnspan=2)

searchbutton = Button(text="Search", command=search )
searchbutton.grid(row=2, column=3, )
window.mainloop()