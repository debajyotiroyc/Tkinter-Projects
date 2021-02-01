from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def resize():
    root.geometry(f"{s1.get()}x{s2.get()}")
    tmsg.showinfo("Window resize",f"Your {s1.get()}x{s2.get()} window has been formed.")

Label(root,text="Window Resizer",bg="blue",fg="white",font="verdana 20 bold").pack(side=TOP,padx=2,pady=1)
f1=Frame(root,bg="orange",padx=50)
f1.pack(side=TOP,padx=2,pady=2)
Label(f1,text="Width of window: ",fg="white",bg="blue",font="arial 10 bold",relief=GROOVE).grid(row=0,column=0,padx=2,pady=2,ipadx=1,ipady=1)
s1=Scale(f1,from_=100,to="1000",orient=HORIZONTAL)
s1.grid(row=0,column=2,padx=2,pady=2)
Label(f1,text="Height of window: ",fg="white",bg="blue",font="arial 10 bold",relief=GROOVE).grid(row=1,column=0,padx=2,pady=2,ipadx=1,ipady=1)
s2=Scale(f1,from_=100,to="1000",orient=HORIZONTAL)
s2.grid(row=1,column=2,padx=2,pady=2)
Button(f1,text="Submit",command=resize).grid(row=3,column=1,padx=2,pady=2)

root.mainloop()