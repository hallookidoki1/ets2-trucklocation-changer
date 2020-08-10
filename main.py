from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from glob import *
import os
import subprocess
import re




window = Tk()

window.geometry("1080x720")

window.title("Schön")


tab_control = ttk.Notebook(window)
tab1 = ttk.Notebook(window)
tab_control.add(tab1, text="Home")
tab_control.pack(expand=1, fill="both")

tab2 = ttk.Notebook(window)
tab_control.add(tab2, text="Settings")
tab_control.pack(expand=1, fill="both")


frame1 = Frame(tab1, height=1080, width=720, bg="#111111")
frame1.pack(fill="both", expand=1)

frame2 = Frame(tab2, height=1080, width=720, bg="#111111")
frame2.pack(fill="both", expand=1)




def getsavefile():
    save = save_file.get()
    return save


def open_it():
    save_file = filedialog.askopenfilename(title="Datei auswählen", filetypes=[("sii files", "*.sii")])
    

    

    

    
    isinthebücher = Label(frame1, text="Ausgwählte Datei \n" + os.path.basename(save_file))
    isinthebücher.pack()

    command=lambda:[speichern()]
    subprocess.Popen(["C:/Users/wrana/Documents/Euro Truck Simulator 2/SII_Decrypt.exe", save_file])

    coordinatesentry = Entry(frame1, width=80)
    coordinatesentry.place(x=300, y= 300)


    def cordeintragen():

        cordget = coordinatesentry.get()



        with open(save_file, "r") as f:
            data = f.read()
        
        data = re.sub(r"(?<!_)truck_placement: .*\n", r"truck_placement: %s\n" % cordget, data)

        with open(save_file, "w") as f:
            f.writelines(data)



        
    submitbutton = Button(frame1, text="Bestätigen", font=("Helvetica", "20"), command= cordeintragen)
    submitbutton.place(x= 910 ,y= 618)
#hallo das ist scheiße


    

   




buttonsearch = Button(frame1, text="Save auswählen", command=open_it, font=("Helvetica", "20"))
buttonsearch.place(x=20, y=618)







window.mainloop()
