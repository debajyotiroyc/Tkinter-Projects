from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from tkinter.colorchooser import askcolor
import time

def new_file():
    global file
    global n
    n=n+1
    root.title(f"New Text Document-MyNotePad({n})")
    file=None
    text.delete(0.0,END)

def save_file():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(0.0,END))
            f.close()
            root.title(os.path.basename(file)+"- MyNotePad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(text.get(0.0, END))
        f.close()


def fun():
    print("OK")

def open_file():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- MyNotePad")
        text.delete(0.0,END)
        f=open(file,"r")
        text.insert(0.0,f.read())
        f.close()


def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def dele():
    text.delete(0.0,END)
def undo():
    text.edit_undo()
def redo():
    text.edit_redo()
def reset():
    text.edit_reset()
def select_all():
    text.tag_add(SEL,"1.0",END)
    text.see(INSERT)
def changeFg():
    (triple,hexstr)=askcolor()
    if hexstr:
        text.config(fg=hexstr)
def changeBg():
    (triple,hexstr)=askcolor()
    if hexstr:
        text.config(bg=hexstr)
def addDate():
    full_date= time.localtime()
    day=str(full_date.tm_mday)
    month=str(full_date.tm_mon)
    year=str(full_date.tm_year)
    date= day+"/"+month+"/"+year
    text.insert(INSERT,date,"a")

def about():
    tmsg.showinfo("About MyNotePad","This notepad type text editor has been made by Debajyoti, a coder from WB. Kindly follow him on GitHub for more interesting projects. Stay Tuned.")

root=Tk()
root.title("New Text Document-MyNotePad(1)")
n=1
file=None
st=StringVar()
st.set("Ready...")
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="New",command=new_file)
m1.add_command(label="Open..",command=open_file)
m1.add_command(label="Save As",command=save_file)
m1.add_separator()
m1.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label="Undo",command=undo)
m2.add_separator()
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
m2.add_command(label="Delete",command=dele)
m2.add_separator()
m2.add_command(label="Re-do",command=redo)
m2.add_command(label="Re-Set",command=reset)
m2.add_separator()
m2.add_command(label="Select all..",command=select_all)
menubar.add_cascade(label="Edit",menu=m2)

m3=Menu(menubar,tearoff=0)
m3.add_command(label="Font color",command=changeFg)
m3.add_command(label="Background color",command=changeBg)
menubar.add_cascade(label="Format",menu=m3)

m4=Menu(menubar,tearoff=0)
m4.add_command(label="Date..",command=addDate)
menubar.add_cascade(label="View",menu=m4)

m5=Menu(menubar,tearoff=0)
m5.add_command(label="About Notepad",command=about)
menubar.add_cascade(label="Help",menu=m5)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(root,yscrollcommand=scrollbar.set,height=50,undo=True)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.config(menu=menubar)


root.mainloop()