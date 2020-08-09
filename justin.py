from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from glob import *
import os
import subprocess



window = Tk()

window.geometry("1080x720")

window.title("Schön")


tab_control = ttk.Notebook(window)
tab1 = ttk.Notebook(window)
tab_control.add(tab1, text="Home")
tab_control.pack(expand=1, fill="both")


frame1 = Frame(tab1, height=1920, width=1080, bg="#111111")
frame1.pack(fill="both", expand=1)

def getsavefile():
    save = save_file.get()
    return save


def open_it():
    save_file = filedialog.askopenfilename(title="Datei auswählen", filetypes=[("sii files", "*.sii")])
    
    fo = open(save_file,"r+") 
    print("Name of the File : ",fo.name)
    
    isinthebücher = Label(frame1, text="Ausgwählte Datei \n" + os.path.basename(save_file))
    isinthebücher.pack()

    command=lambda:[speichern()]
    subprocess.Popen(["C:/Users/wrana/Documents/Euro Truck Simulator 2/SII_Decrypt.exe", save_file])

    coordinatesentry = Entry(frame1, width=80)
    coordinatesentry.place(x=300, y= 300)

    cords = coordinatesentry.get()

    print(cords)




buttonsearch = Button(frame1, text="Save auswählen", command=open_it, font=("Helvetica", "20"))
buttonsearch.place(x=20, y=618)






window.mainloop()
