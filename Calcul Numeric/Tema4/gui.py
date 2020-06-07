from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import main as m
import bonus as b

root = Tk()
root.title("Tema 4 CN")
root.minsize(400, 250)
root.geometry("500x400")
root.attributes("-toolwindow", 1)

def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()

def click_submit1():
    if structura.current() == 0:
        rez = m.get_res('1')
    else:
        rez = b.get_res('1')
    printeaza(rez, '1')

def click_submit2():
    if structura.current() == 0:
        rez = m.get_res('2')
    else:
        rez = b.get_res('2')
    printeaza(rez, '2')

def click_submit3():
    if structura.current() == 0:
        rez = m.get_res('3')
    else:
        rez = b.get_res('3')
    printeaza(rez, '3')

def click_submit4():
    if structura.current() == 0:
        rez = m.get_res('4')
    else:
        rez = b.get_res('4')
    printeaza(rez, '4')

def click_submit5():
    if structura.current() == 0:
        rez = m.get_res('5')
    else:
        rez = b.get_res('5')
    printeaza(rez, '5')

def printeaza(rez, caz):
    if isinstance(rez, str):
        messagebox.showinfo("Something went wrong", rez)
    else:
        listbox.delete(0, END)
        listbox.insert(END,  '  Case ' + caz +'       Norm : ' + str(rez[0]) + '\n')
        for i in range(len(rez[1])):
            listbox.insert(END, '  x' + str(i) + ' = ' + str(rez[1][i]))

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

listbox = Listbox(root,  borderwidth=5, yscrollcommand = sb.set)
listbox.pack(fill=BOTH, expand=1)

submitButton1 = Button(root, text="Case 1", command=click_submit1)
submitButton2 = Button(root, text="Case 2", command=click_submit2)
submitButton3 = Button(root, text="Case 3", command=click_submit3)
submitButton4 = Button(root, text="Case 4", command=click_submit4)
submitButton5 = Button(root, text="Case 5", command=click_submit5)

structura = ttk.Combobox(root, values=["Default", "Bonus"], state='readonly')
submitButton1.pack(side=LEFT, padx=5, pady=5)
submitButton2.pack(side=LEFT, padx=5, pady=5)
submitButton3.pack(side=LEFT, padx=5, pady=5)
submitButton4.pack(side=LEFT, padx=5, pady=5)
submitButton5.pack(side=LEFT, padx=5, pady=5)

structura.pack(side=RIGHT)
structura.current(0)

sb.config( command = listbox.yview )

root.mainloop()