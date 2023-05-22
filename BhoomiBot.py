import pickle
import json
import numpy as np
from sklearn.linear_model import LinearRegression

######################## Get Model artifacts #######################

locations = None
data_columns = None
model = None

with open('model.pickle', 'rb') as f:
    model = pickle.load(f)
    
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]  # first 3 columns are sqft, bath, bhk


######################## start with tKinter #######################

import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title("BhoomiBot")

frame = tkinter.Frame(window)
frame.pack()

def predict_house_price():
    size_info = size_info_entry.get()
    location_info = location_combobox.get()
    if size_info:
        if location_info:
            try:
                loc_index = data_columns.index(location_combobox.get().lower())
                # print("loc_index")
            except:
                loc_index = -1

            x = np.zeros(len(data_columns))
            x[0] = int(size_info_entry.get()) # 
            x[1] = int(bath_spinbox.get())
            x[2] = int(BHK_spinbox.get())
            if loc_index>=0:
                x[loc_index] = 1
            house_price = round(model.predict([x])[0],2)
            #print(house_price)
            display_var.set(house_price)
        else:
            tkinter.messagebox.showwarning(title="Error",
                                       message="Location not selected")
    else:
        tkinter.messagebox.showwarning(title="Error",
                                       message="Missing Plot Size information")

## Frame1 --> "Size info"     
size_info_frame = tkinter.LabelFrame(frame, text ="" )
#size_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='news')
size_info_frame.grid(row=0, column=0, padx=30, pady=10)

    # size infomation --> Label/Entry
size_info_label = tkinter.Label(size_info_frame, text ="Plot Size in sqft" )
size_info_label.grid(row=0, column=0)    
    
size_info_entry = tkinter.Entry(size_info_frame)
size_info_entry.grid(row=1, column=0,padx=5,pady=5)

# -----------------------------------sticky='news'-------------------
## Frame2 --> "BHK info"
BHK_info_frame = tkinter.LabelFrame(frame, text ="" )
BHK_info_frame.grid(row=1, column=0, padx=30, pady=10)

    # BHK information --> Label/spin
BHK_info_label = tkinter.Label(BHK_info_frame, text ="BHK Info")
BHK_info_label.grid(row=0, column=0) 

BHK_spinbox = tkinter.Spinbox(BHK_info_frame, from_= 1, to = 4)
BHK_spinbox.grid(row=1, column=0,padx=5,pady=5)   
    
# ------------------------------------------------------
## Frame3 --> "Bath info"
bath_info_frame = tkinter.LabelFrame(frame, text ="" )
bath_info_frame.grid(row=2, column=0, padx=30, pady=10)

    # bath infomation --> Label/spin
bath_info_label = tkinter.Label(bath_info_frame, text ="Bath Rooms")
bath_info_label.grid(row=0, column=0)

bath_spinbox = tkinter.Spinbox(bath_info_frame, from_=1, to=4)
bath_spinbox.grid(row=1, column=0,padx=5,pady=5)    
    
# ------------------------------------------------------
## Frame4 --> "Location info"
location_info_frame = tkinter.LabelFrame(frame, text ="" )
location_info_frame.grid(row=3, column=0, padx=30, pady=10)

    # Location infomation --> Label/Dropdown
location_name_label = tkinter.Label(location_info_frame, text ="Location")
location_name_label.grid(row=0, column=0)

location_combobox = ttk.Combobox(location_info_frame, values= locations)
location_combobox.grid(row=1, column=0,padx=5,pady=5)    
    
# ------------------------------------------------------
## Frame5 --> "Button"
calculate_frame = tkinter.LabelFrame(frame, text ="" )
calculate_frame.grid(row=4, column=0, padx=30, pady=10)

    # Calculate --> Label/Button
button = tkinter.Button(calculate_frame, text= 'Calculate', 
                        command = predict_house_price,font = ('arial',9,'bold'))
button.grid(row=0, column=0, padx=20, pady=10, sticky='news')   
    
# ------------------------------------------------------
## Frame6 --> "Text Box"
display_frame = tkinter.LabelFrame(frame, text ="Estimated Price in Lakhs" )
display_frame.grid(row=5, column=0, padx=30, pady=10)

    # Text Box --> Label/Entry

display_var =tkinter.StringVar(value="")
display_entry = tkinter.Entry(display_frame,font = ('arial',10,'bold'),
                              textvariable=display_var,bd=10, insertwidth=2,
                             bg='powder blue',justify='center')
display_entry.grid(row=1, column=0,padx=5,pady=10)  


window.mainloop()
