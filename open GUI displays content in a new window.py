import tkinter as tk                 		# import tkinter
from tkinter import filedialog       	# import file dialog

def open_file():                     		# function to open file
    file = filedialog.askopenfilename()   # open file dialog
    if file:                        		 # check file selected
        f = open(file, "r")          		# open file
        text.insert(tk.END, f.read()) 	# display content
        f.close()                    		# close file

root = tk.Tk()                       		# create window
tk.Button(root, text="Open File", command=open_file).pack()  # button
text = tk.Text(root)                 		# text box
text.pack()                          		# place text box
root.mainloop()                      		# run program
