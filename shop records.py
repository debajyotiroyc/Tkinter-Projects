from tkinter import *

def get_vals():
    print(f"The name is {name_val.get()}")
    print(f"The bill amount is {amt_val.get()}")
    print(f"The payment mode is {paym_val.get()}")
    print(f"The amount paid is {debit_val.get()}")
    stat_val.set("Transaction Successful")
    if (float(amt_val.get())!=float(debit_val.get())):
        p=float(amt_val.get())-float(debit_val.get())
        due_val.set(str(p))
    else:
        p="Amount has been fully paid"
        due_val.set(p)
    rec=open("records.txt",'a')
    rec.write(f"The name is {name_val.get()}\n")
    rec.write(f"The bill amount is {amt_val.get()}\n")
    rec.write(f"The payment mode is {paym_val.get()}\n")
    rec.write(f"The amount paid is {debit_val.get()}\n")
    rec.write(f"The status : {stat_val.get()}\n")
    rec.write(f"The due amount is : {due_val.get()}\n")
    rec.write("-----------------------------------------------------------------------------------------------\n")
    rec.close()


root=Tk()
root.geometry("500x500")
f1=Frame(root,bg="red",borderwidth=10,relief=GROOVE)
f1.pack(side=TOP,fill="x")
l1=Label(f1,text="Balaji Enterprises Pvt Ltd",fg="black",font="arial 25 bold")
l1.pack()
f2=Frame(root,borderwidth=10,relief=RAISED,padx=50,pady=15)
f2.pack(side=TOP)
Label(f2,text="Customer Name: ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=1,column=1)
Label(f2,text="Bill Amount : ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=2,column=1)
Label(f2,text="Payment Mode : ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=3,column=1)
Label(f2,text="Amount Paid : ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=4,column=1)
Label(f2,text="Status : ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=5,column=1)
Label(f2,text="Due Amount : ",bg="blue",fg="white",bd=5,padx=5,relief=SUNKEN,font="comicsans 12 bold").grid(row=6,column=1)

name_val=StringVar()
amt_val=StringVar()
paym_val=StringVar()
debit_val=StringVar()
stat_val=StringVar()
due_val=StringVar()
stat_val.set("N/A")
due_val.set("N/A")
Entry(f2,textvariable=name_val).grid(row=1,column=3)
Entry(f2,textvariable=amt_val).grid(row=2,column=3)
Entry(f2,textvariable=paym_val).grid(row=3,column=3)
Entry(f2,textvariable=debit_val).grid(row=4,column=3)
Entry(f2,textvariable=stat_val).grid(row=5,column=3)
Entry(f2,textvariable=due_val).grid(row=6,column=3)

Button(f2,text="Submit",command=get_vals,padx=2,pady=5).grid(row=7,column=2)

root.mainloop()
