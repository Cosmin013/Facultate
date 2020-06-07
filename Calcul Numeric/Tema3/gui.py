from tkinter import *
from tkinter import messagebox
from main import *

root = Tk()
root.title("Tema 3 CN")
root.resizable(0, 0)
root.attributes("-toolwindow", 1)


def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()


def click_submit():
    try:
        rez = calc(path1.get(), path2.get(), rezori.get(), rezplus.get(), saveadunare.get(), saveinmultire.get())
        messagebox.showinfo("Success! ", rez)
    except:
        messagebox.showerror("Error", "Something went wrong!")



def init():
    clear()
    lbl1 = Label(root, text="A :")
    lbl2 = Label(root, text="B :")
    lbl3 = Label(root, text="Rezultat adunare :")
    lbl4 = Label(root, text="Rezultat inmultire :")
    lbl5 = Label(root, text="Salveaza adunarea :")
    lbl6 = Label(root, text="Salveaza inmultirea :")

    global path1
    path1 = Entry(root, text="")
    path1.insert(0, "a.txt")
    global path2
    path2 = Entry(root, text="")
    path2.insert(0, "b.txt")

    global rezplus
    rezplus = Entry(root, text="")
    rezplus.insert(0, "aplusb.txt")
    global rezori
    rezori = Entry(root, text="")
    rezori.insert(0, "aorib.txt")

    global saveadunare
    saveadunare = Entry(root, text="")
    saveadunare.insert(0, "rezplus.txt")
    global saveinmultire
    saveinmultire = Entry(root, text="")
    saveinmultire.insert(0, "rezori.txt")


    submitButton = Button(root, text="Submit", command=click_submit)

    lbl1.grid(row=0, column=0, pady=10, padx=(10, 0))
    lbl2.grid(row=1, column=0, pady=10, padx=(10, 0))
    lbl3.grid(row=2, column=0, pady=10, padx=(10, 0))
    lbl4.grid(row=3, column=0, pady=10, padx=(10, 0))
    lbl5.grid(row=4, column=0, pady=10, padx=(10, 0))
    lbl6.grid(row=5, column=0, pady=10, padx=(10, 0))

    path1.grid(row=0, column=1, pady=10, padx=(10, 0))
    path2.grid(row=1, column=1, pady=10, padx=(10, 0))
    rezplus.grid(row=2, column=1, pady=10, padx=(10, 0))
    rezori.grid(row=3, column=1, pady=10, padx=(10, 0))
    saveadunare.grid(row=4, column=1, pady=10, padx=(10, 0))
    saveinmultire.grid(row=5, column=1, pady=10, padx=(10, 0))


    submitButton.grid(row=5, column=2, padx=(10, 10))


init()

root.mainloop()
