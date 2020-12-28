from tkinter import *

def getv():
    print(f"The Full Name is : {full_name.get()}")
    print(f"The Phone Number is : {phone.get()}")
    print(f"The Address is : {address.get()}")
    print(f"The Duration is : {length.get()}")


root=Tk()
root.geometry("500x500")
disp_frame=Frame(root,borderwidth=5,padx=5,pady=5)
disp_frame.pack(side=TOP,fill="x")
disp_msg=Label(disp_frame,text="Welcome to West Bengal Tour and Travels Pvt. Limited",bg="blue",fg="white",padx=2,pady=2,font="arial 20 bold",relief=GROOVE)
disp_msg.pack(fill=X)


details_frame=Frame(root,padx=50,pady=20,borderwidth=15,bg="red")
details_frame.pack()
full_name=StringVar()
phone=StringVar()
address=StringVar()
length=StringVar()
food=IntVar()

Label(details_frame,text="Enter your details",anchor="center",font="Arial 20 bold",padx=15,pady=5,relief=RAISED,bd=5).grid(row=0,column=12)
l1=Label(details_frame,text="Full name: ",padx=4,bd=5,bg="blue",relief=SUNKEN)
l2=Label(details_frame,text="Phone no. : ",padx=4,bd=5,bg="yellow",relief=SUNKEN)
l3=Label(details_frame,text="Address: ",padx=4,bd=5,bg="orange",relief=SUNKEN)
l4=Label(details_frame,text="Duration: ",padx=4,bd=5,bg="green",relief=SUNKEN)

l1.grid(row=1,column=11)
l2.grid(row=2,column=11)
l3.grid(row=3,column=11)
l4.grid(row=4,column=11)

full_ent=Entry(details_frame,textvariable=full_name)
phone_ent=Entry(details_frame,textvariable=phone)
address_ent=Entry(details_frame,textvariable=address)
length_ent=Entry(details_frame,textvariable=length)


full_ent.grid(row=1,column=13)
phone_ent.grid(row=2,column=13)
address_ent.grid(row=3,column=13)
length_ent.grid(row=4,column=13)

Checkbutton(details_frame,text="Do you want to include meals?",variable=food,relief=GROOVE,pady=3).grid(row=5,column=11)
Button(details_frame,text="Submit",command=getv).grid(row=6,column=12)

root.mainloop()