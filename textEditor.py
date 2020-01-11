import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

HEIGHT = 500
WIDTH = 400

fileName = None
saved = False
get = None

def openFile():
    global fileName 
    file = filedialog.askopenfile(mode='r')
    fileName = file.name
    read = file.read()
    text.delete(0.0, END)
    text.insert(0.0,read)
    
def save():
    global fileName, saved, get
    if fileName == None:
        saveAs()
    else :
        get = text.get(0.0, END)
        file = open(fileName, "w")
        file.write(get)
        file.close()
        saved = True

def saveAs():
    global fileName, saved, get
    files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text File', '*.txt')] 
    file = filedialog.asksaveasfile(mode="w", filetypes = files,  defaultextension='.txt')
    fileName = file.name
    get = text.get(0.0, END)
    file.write(get)
    file.close()
    saved = True
    
def newFile():
    global saved
    if get != text.get(0.0, END):
        saved = False
    if saved == False :
        value = messagebox.askyesnocancel("Unsaved file","Do you want to save the current file ?")
        if value == True :
            save()
        elif value == None:
            return
    text.delete(0.0, END)
    

root= Tk("Text Editor")
root.wm_title("Text Editor")

resolution = str(HEIGHT)+'x'+str(WIDTH)
root.geometry(resolution)

text=Text(root, height = HEIGHT, width = WIDTH) 
text.pack() 
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)

filemenu.add_command(label = "New File" , command = newFile)
filemenu.add_command(label = "Open" , command = openFile)
filemenu.add_command(label = "Save" , command = save)
filemenu.add_command(label = "Save as" , command = saveAs)

root.config(menu=menubar)
root.mainloop()