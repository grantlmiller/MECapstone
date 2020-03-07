import tkinter
import tkinter.messagebox
import Element

#global variables
elementList = []
#button functions 
def add_clicked():
    print("add clicked")
    add_popup()
def delete_clicked():
    print("Delete clicked")

#define pop up window 
def add_popup():
    popup = tkinter.Tk()
    popup.wm_title("Add Element")
    label = tkinter.Label(popup, text="Add Element")
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Add", command = popup.destroy)
    B2 = tkinter.Button(popup, text="Cancel", command = popup.destroy)
    B1.pack()
    B2.pack()
    popup.mainloop()


#establish main window
mainWindow = tkinter.Tk()
mainWindow.title("main tool")
elementList = []

#main listbox for elements 
elementListBox = tkinter.Listbox(mainWindow)
elementListBox.pack()
#elementListBox.insert(END,"Hell")

#buttons on main window
addButton = tkinter.Button(mainWindow, text="Add", command=add_clicked)
deleteButton = tkinter.Button(mainWindow, text="Delete", command=delete_clicked)
addButton.pack()
deleteButton.pack()
#run window mainloop
mainWindow.mainloop()
