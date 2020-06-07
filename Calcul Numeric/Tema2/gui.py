from tkinter import *
from main import get_output

root = Tk()
root.title("Tema 2 CN")
root.resizable(0, 0)
root.attributes("-toolwindow", 1)
A = list()
B = list()
n = 0


def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()


def get_res():
    input_A = [[float(A[i + j * n].get()) for i in range(n)] for j in range(n)]
    input_b = [float(B[i].get()) for i in range(n)]
    C = get_output(n, input_A, input_b)
    clear()
    lblA = Label(root, text=C)
    lblA.grid(sticky=N, padx=10, pady=10)
    reset_button = Button(root, text="Reset", command=init)
    reset_button.grid(pady=10)


def click_submit():
    global n, textbox
    n = int(textbox.get())
    clear()
    lblA = Label(root, text="A:")
    lblA.grid(row=0, column=0, padx=(10, 0), rowspan=n, sticky='N')
    global A
    A = list()

    for i in range(n):  # Rows
        for j in range(n):  # Columns
            b = Entry(root, text="", width=3)
            b.insert(0, '0')
            A.append(b)
            b.grid(row=i, column=j + 1, padx=1, pady=1)

    lblB = Label(root, text="B:")
    lblB.grid(row=n, column=0, pady=10, padx=(10, 0))
    for i in range(n):
        b = Entry(root, text="", width=3)
        b.insert(0, '0')
        B.append(b)
        b.grid(row=n, column=i + 1)

    submitButton = Button(root, text="Submit", command=get_res)
    submitButton.grid(columnspan=n + 2, pady=10)
    lbl = Label(text=" ")
    lbl.grid(row=n, column=n + 2)


def init():
    clear()
    global textbox
    lbl = Label(root, text="n:")
    textbox = Entry(root, text="")
    textbox.insert(0, "5")
    submitButton = Button(root, text="Submit", command=click_submit)
    lbl.grid(row=0, column=0, pady=10, padx=(10, 0))
    textbox.grid(row=0, column=1)
    submitButton.grid(row=0, column=2, padx=(0, 10))


init()

root.mainloop()
