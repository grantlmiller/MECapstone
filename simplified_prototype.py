from tkinter import *
#Independent Variables
list_of_elements = [] #size of cooling element
#
#USER INTERFACE
#
#Initialize window 
window = Tk()
window.title("Simple Tool")
    #cooling element label
def add_labels():
    cooling_element_name_label = Label(window, text="Cooling Element \nName")
    cooling_element_name_label.grid(column=0, row=1)
    #flow rate output label
    flow_rate_output_label = Label(window, text="Flow Rate")
    flow_rate_output_label.grid(column=2,row=0)
    #input pressure label
    input_pressure_label = Label(window, text="Input Pressure")
    input_pressure_label.grid(column=0,row=0)
    #cooling element size
    cooling_element_size_label = Label(window, text="Size of Element")
    cooling_element_size_label.grid(column=0,row=3)
    
def add_textboxes():
     #cooling element textbox
    cooling_element_name_textbox = Entry(window,width=10)
    cooling_element_name_textbox.grid(column=1, row=1)
    #cooling size textbox
    cooling_element_size_textbox = Entry(window,width=10)
    cooling_element_size_textbox.grid(column=1,row=3)
    #flow rate output textbox
    flow_rate_output_textbox = Entry(window,width=10)
    flow_rate_output_textbox.grid(column=3,row=0)
    #input pressure textbox
    input_pressure_textbox = Entry(window,width=10)
    input_pressure_textbox.grid(column=1,row=0)

add_labels()
add_textboxes()

#List Box
listboxName = Listbox(window,width=10)
listboxName.grid(row=9, column=0)

#getting info from textbox
class Element:
    def __init__(self):
        self.name = cooling_element_name_textbox.get()
        self.size = cooling_element_size_textbox.get()
        #self.resistance 
        listboxName.insert(END,self.name)
        cooling_element_name_textbox.delete("0",END)
        cooling_element_size_textbox.delete("0",END)
        
        
#buttons
#add button this will save data and clear for next element
def add_clicked():
    element = Element()
    list_of_elements.append(element)
add_btn = Button(window, text="New Item", command=add_clicked)
add_btn.grid(column=0, row=8)
#calculate button
def calculate_clicked():
    for e in list_of_elements:
        e.resistance = lookup(e.size)
        
    
#calculate_btn = Button(window, text="Calculate", command=calculate_clicked)
#calculate_btn.grid(column=3, row=8)
#Start Mainloop
window.mainloop()


