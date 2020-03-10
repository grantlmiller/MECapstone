import tkinter
import tkinter.messagebox
import Element
import csv


#establish main window
mainWindow = tkinter.Tk()
mainWindow.title("main tool")
#List of Elements that have been inputted
elementList = []
CurrentElement=[]

#button functions for main window
def main_add_clicked():
    add_popup()
def delete_clicked():
    current_listbox_selection = elementListBox.get(tkinter.ACTIVE)
    for i in elementList:
        if i.name == current_listbox_selection:
            elementList.remove(i)
            elementListBox.delete(tkinter.ANCHOR)
def refresh_clicked():
    current_listbox_selection = elementListBox.get(tkinter.ACTIVE)
    size = 0
    for i in elementList:
        if i.name == current_listbox_selection:
            size =i.size
    current_size.config(text=size)

#Define what happens if you close the main window (line is so you can press the X in upper right hand corner)
mainWindow.protocol("WM_DELETE_WINDOW",mainWindow.destroy)

#main listbox for elements 
elementListBox = tkinter.Listbox(mainWindow)
elementListBox.pack()

#define pop up window 
def add_popup():
    popup = tkinter.Tk()
    popup.wm_title("Add Element")
    #labels and Textboxes for popup
    nameLabel = tkinter.Label(popup, text="Element Name:")
    sizeLabel = tkinter.Label(popup, text="Element Size:")
    nameTextBox = tkinter.Entry(popup)
    sizeTextBox = tkinter.Entry(popup)
    nameLabel.grid(column=0, row=0)
    sizeLabel.grid(column=0, row=1)
    nameTextBox.grid(row=0, column=1)
    sizeTextBox.grid(row=1, column=1)
    #define function for add button clicked in pop up (after entering values)
    def popup_add_clicked():
        CurrentElement = Element.Element(nameTextBox.get(),sizeTextBox.get())
        elementList.append(CurrentElement)
        elementListBox.insert(tkinter.END,CurrentElement.name)
        popup.destroy()
    

    popup_add_button = tkinter.Button(popup, text="Add", command = popup_add_clicked)
    popup_cancel_button = tkinter.Button(popup, text="Cancel", command = popup.destroy)
    popup_add_button.grid(row=2, column=0)
    popup_cancel_button.grid(row=3, column=0)
    #mainloop to keep popup interactive
    popup.mainloop()
#Items main window
#Info about Current Element Selected
current_size_label = tkinter.Label(mainWindow, text='Element Size')
current_size = tkinter.Label(mainWindow, text=elementListBox.get(tkinter.ACTIVE))
current_size_label.pack()
current_size.pack()

#mainWIndow button definitions 
addButton = tkinter.Button(mainWindow, text="Add", command=main_add_clicked)
deleteButton = tkinter.Button(mainWindow, text="Delete", command=delete_clicked)
refreshButton = tkinter.Button(mainWindow, text="Refresh", command = refresh_clicked)
addButton.pack(side=tkinter.LEFT)
deleteButton.pack(side=tkinter.LEFT)
refreshButton.pack(side =tkinter.LEFT)
#run window mainloop
mainWindow.mainloop()
