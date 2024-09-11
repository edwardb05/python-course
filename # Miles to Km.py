# Miles to Km
from tkinter import *
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

miles_label = Label(text="miles")
miles_label.grid(row=1, column=3)

equalto_label = Label(text="is equal to")
equalto_label.grid(row=2, column=1)

output_label = Label(text="0")
output_label.grid(row=2, column=2)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.grid(row=1,column = 2)

#Buttons
def convert():
    miles = float(entry.get)
    km = 1.6*miles
    output_label.config(text =km)

#calls action() when pressed
button = Button(text="Calculate", command=convert)
button.grid(row=3, column=2)


