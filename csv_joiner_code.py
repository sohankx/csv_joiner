## Merge Multiple 1M Rows CSV files
import os
# import glob
import pandas as pd
import sys
# os.chdir("mydir")
# cwd = os.getcwd()
# print(cwd)
# file_name1=glob.glob(cwd+"/*")
# # print(file_name1)


# # # 3. creates empty list to include the content of each file converted to pandas DF
# csv_list = []
 
# # # 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
# for file in sorted(file_name1):
#     csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))

# # # 5. merges single pandas DFs into a single DF, index is refreshed 
# csv_merged = pd.concat(csv_list, ignore_index=True)

# # # 6. Single DF is saved to the path in CSV format, without index column
# csv_merged.to_csv(cwd+ '/Joined.csv', index=False)
import os
# def rest():
#     os.system('cls')
#     script_name = os.path.basename(__file__)
#     os.system('csv_joiner_code.py')




import os
import sys
import psutil
import logging

def close_restart():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# from joiner import join_another_files
# create the root window
root = tk.Tk()
root.title('CSV Joiner')
root.resizable(False, False)
root.geometry('300x450')
root.configure(background='blue4')

file_list=[]
def select_files():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Browse files',
        initialdir='/',
        filetypes=filetypes)

    file_list.append(filenames)

    showinfo(
        title='Selected Files',
        message=filenames
    )
# cornflower blue

# open button
style = ttk.Style()
style.configure("BW.TLabel", font=('Italian Bold','20','bold'),background="white")

# l1 = ttk.Label(text="Test", style="BW.TLabel")
open_button = ttk.Button(
    root,
    text='Browse Files',style="BW.TLabel",
    command=select_files
)

open_button.pack(expand=True)

def on_enter(e):
    style.configure("BW.TLabel", font=('Italian Bold','20','bold'),background="white")

def on_leave(e):
    style.configure("BW.TLabel", font=('Italian Bold','20','bold'),background="cyan")


open_button.bind("<Enter>", on_enter)
open_button.bind("<Leave>", on_leave)



def joiner_files():
	# print(file_list)
	dr=(file_list[0][0].split('/'))[:-1]
	joined = "/". join(dr)


		# # 3. creates empty list to include the content of each file converted to pandas DF
	csv_list = []
	 
	# # 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
	for file_name1 in file_list:
		for file in sorted(file_name1):
		    csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))

	# # 5. merges single pandas DFs into a single DF, index is refreshed 
	csv_merged = pd.concat(csv_list, ignore_index=True)

	# # 6. Single DF is saved to the path in CSV format, without index column
	csv_merged.to_csv(joined+'/Joined.csv', index=False)
	# import os
	os.system(f'start {os.path.basename(joined)}')
	# print(file_list)
	# join_another_files()
	# rest()
	close_restart()

	# root.destroy()



def close():
	root.destroy()



  
  
# Button for closing
exit_button = Button(root, text="Join Selected Files",bg="spring green",height= 1, width=15, command=joiner_files)
exit_button.pack(expand=True)
# Button for closing
exit_button = Button(root, text="Exit",bg="red3",height= 1, width=7, command=close)
exit_button.pack(expand=True)


footer_frame = tk.Frame(root)
label = tk.Label(footer_frame, text="Created by :- Sohan Chaudhary",height=1, font='Helvetica 15 bold', background="green yellow")

footer_frame.pack(side="bottom", fill="x")
label.pack(side="right")

root.mainloop()

# print(filenames)
