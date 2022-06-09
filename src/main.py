import bot
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap("signy.ico")
root.title("Signy Bot")

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

num = StringVar()
num.set(5)
num_entry = ttk.Spinbox(mainframe, from_=1, to_=100, textvariable=num)
num_entry.grid(column=3, row=1, sticky=(W, E))

def begin():
    z = messagebox.askquestion("Bot Starting", "Please navigate to discord within 5 seconds.")
    if(z == 'yes'):
        time.sleep(5)
        inum = int(num.get())
        bot.start_bot(inum)
    elif (z == 'no'):
        print("Cancelled")
    else:
        print("exception")
    
ttk.Button(mainframe, text="Activate", style='Accent.TButton', command=begin).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Amount Of Signies").grid(column=1, row=1, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

num_entry.focus()
root.bind("<Return>", begin)

root.mainloop()



