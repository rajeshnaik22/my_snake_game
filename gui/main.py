# Mile to Km converter

import tkinter

def button_clicked():
    print("clicked")
    label3["text"]=int(input.get()) * 1.60934


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


input = tkinter.Entry(width=10)
input.grid(column=1,row=0)

label = tkinter.Label(text="Miles")
label.grid(column=2,row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0,row=1)

label3 = tkinter.Label(text="0")
label3.grid(column=1,row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2,row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)






window.mainloop()