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
all_nb_occurence = []
execution_time = []

fig = Figure(figsize=(2, 3), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def getDataHanoi(n):

    for i in range(1, n):
        all_n.append(i)

        start = time.time()
        all_nb_occurence.append(hanoi(i))
        end = time.time()

        execution = end - start
        execution_time.append(execution)
        print(" --> Calculation done successfully : for n = ", i, " in ", execution)


def displayData():
    ax.clear()

    x, y = all_n, all_nb_occurence
    ax.plot(x, y)

    canvas.draw()
    canvas.flush_events()


def HanoiTour(n, A, B, C, occurence):

    if n == 1:
        return occurence
    return HanoiTour(n - 1, A, C, B, occurence + 1) + HanoiTour(n - 1, C, B, A, occurence + 1)


def hanoi(n):
    return HanoiTour(n, 'A', 'B', 'C', 0)


def prog():
    n = int(input("Jusqu'à la valeur : "))
    getDataHanoi(n)
    displayData()
    root.mainloop()


if __name__ == "__main__":
    prog()
