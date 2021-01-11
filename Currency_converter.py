from tkinter import *
def conv():

    curr={"USD":1.00, "INR":73.57, "JPY":104.28,"NZD":1.40,"SFR":0.89,"ARS":85.38 }
    a1=float(var1.get())
    a2=0.0
    d=0.0
    if from_curr.get()!="USD":
        d=a1/curr.get(from_curr.get())
        a2=d*curr.get(to_curr.get())
    else:
        a2=a1*curr.get(to_curr.get())
    var2.set(str(round(a2,3)))



root=Tk()
root.title("Currency Converter")

Label(root,text="WELCOME TO MY CURRENCY CONVERTER",font="comicsans 25 bold",fg="white",bg="blue").pack(side=TOP,fill=X)
f1=Frame(root,bg="orange",padx=50,pady=20,relief=GROOVE,borderwidth=10)
f1.pack(side=TOP,pady=10)
Label(f1,text="Converter App",fg="white",bg="red",font="arial 18 bold",relief=GROOVE,borderwidth=2).grid(row=0,column=1,padx=5,pady=5,ipadx=7,ipady=7)
Label(f1,text="Select A Currency",fg="white",bg="red",font="arial 14 bold",pady=5).grid(row=1,column=0,pady=5,ipadx=3,ipady=3)
Label(f1,text="Select A Currency",fg="white",font="arial 14 bold",bg="red",pady=5).grid(row=1,column=2,pady=5,ipadx=3,ipady=3)
from_curr=StringVar()
to_curr=StringVar()
from_curr.set("Choose")
to_curr.set("Choose")
choices=["USD","INR","JPY","NZD","SFR","ARS"]
menu1=OptionMenu(f1,from_curr,*choices)
menu1.grid(row=2,column=0,padx=8,pady=8,ipadx=6,ipady=6)
menu2=OptionMenu(f1,to_curr,*choices)
menu2.grid(row=2,column=2,padx=8,pady=8,ipadx=6,ipady=6)

Label(f1,text="Enter Amount",font="arial 14 bold",fg="red",bg="aqua").grid(row=3,column=0,padx=8,pady=8,ipadx=10,ipady=10)
Label(f1,text="Output Amount",font="arial 14 bold",fg="red",bg="aqua").grid(row=3,column=2,padx=8,pady=8,ipadx=10,ipady=10)

var1=StringVar()
var2=StringVar()
Entry(f1,textvariable=var1).grid(row=4,column=0,ipadx=15,ipady=15,padx=6,pady=6)
Entry(f1,textvariable=var2).grid(row=4,column=2,ipadx=15,ipady=15,padx=6,pady=6)
Button(f1,text="Submit",activebackground="blue",activeforeground="yellow",fg="red",bg="white",command=conv).grid(row=5,column=1,padx=5,pady=5,ipadx=10,ipady=10)


root.mainloop()
        



