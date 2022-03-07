# -- coding: utf-8 --

import time
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create window
root = tkinter.Tk()
root.wm_title("Embedding in Tk")
root.geometry("700x500")

all_n = []
execution_time = []

fig = Figure(figsize=(2, 3), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def getData(n):

    for i in range(1, n):
        all_n.append(i)

        start = time.time()
        hanoi(i)
        end = time.time()

        execution = end - start
        execution_time.append(execution)
        print(" --> Calculation done successfully : for n = ", i, " in ", execution)


def displayData():
    ax.clear()

    x, y = all_n, execution_time
    ax.plot(x, y, label="Temps d'execution pour n boucle")

    canvas.draw()
    canvas.flush_events()


def ToH(n, A, B, C):
    if n == 1:
        return
    ToH(n - 1, A, C, B)
    ToH(n - 1, C, B, A)


def hanoi(n):
    return ToH(n, 'A', 'B', 'C')


def prog():
    n = int(input("Jusqu'à la valeur : "))
    getData(n)
    displayData()
    root.mainloop()


if __name__ == "__main__":
    prog()
