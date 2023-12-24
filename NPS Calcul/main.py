import shutil
from tkinter import *
from tkinter import filedialog
import pandas as pd
import os
import openpyxl
from openpyxl import load_workbook
from datetime import datetime

# creating a copy of the NPS file and saving it into the Old NPS file
date_and_hour = datetime.now()
date_now = date_and_hour.strftime("%d-%m-%Y")
current_nps = r'C:\Users\Denis\PycharmProjects\NPS Calcul\NPS.xlsx'
new_NPS_copy = r'C:\Users\Denis\PycharmProjects\NPS Calcul\old NPS\NPS'
shutil.copy2(current_nps, f'{new_NPS_copy}_{date_now}.xlsx')


# checking to see if there are excel files to analyse
directory = r'C:\Users\Denis\PycharmProjects\NPS Calcul\files'

files = []

# if there are, for each file get the absolute path
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        files.append(f)

# reading the content

for file in files:

    df = pd.read_excel(file)
    # print(df)

    with pd.ExcelWriter('NPS.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name="Sheet1", header=None, startrow=writer.sheets['Sheet1'].max_row, index=False)

    shutil.move(file, r"C:\Users\Denis\PycharmProjects\NPS Calcul\old files analyzed")


from tkinter import ttk
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x250")
def select_file():
   path= filedialog.askopenfilename(title="Select a File", filetype=(('text files''*.txt'),('all files','*.*')))
   Label(win, text=path, font=10).pack()
#Create a label and a Button to Open the dialog
Label(win, text="Click the Button to Select a File", font=('Aerial 18 bold')).pack(pady=20)
button= ttk.Button(win, text="Select", command= select_file)
button.pack(ipadx=5, pady=15)
win.mainloop()