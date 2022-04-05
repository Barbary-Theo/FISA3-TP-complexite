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


def displayData(list):
    ax.clear()

    x, y = all_n, list
    ax.plot(x, y)

    canvas.draw()
    canvas.flush_events()


def HanoiTour(n, A, B, C, occurence):

    if n == 1:
        return occurence
    return HanoiTour(n - 1, A, C, B, occurence + 1) + HanoiTour(n - 1, C, B, A, occurence + 1)


def hanoi(n):
    return HanoiTour(n, 'A', 'B', 'C', 0)


def main_exo_1():
    n = int(input("Jusqu'à la valeur : "))
    getDataHanoi(n)
    displayData(all_nb_occurence)
    root.mainloop()


def suite_recurrente_iter(n):
    res = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            res.append(1)
        else:
            res.append(res[i - 1] + res[i - 2])

    return res[-1]


def suite_recurrente_recu(n):

    if n == 0 or n == 1:
        return 1
    else:
        return suite_recurrente_recu(n - 1) + suite_recurrente_recu(n - 2)


def getData_suite_recu(n, f):

    for i in range(1, n):
        all_n.append(i)

        start = time.time()
        f(i)
        end = time.time()

        execution = end - start
        execution_time.append(execution)

        if n < 1000:
            print(" --> Calculation done successfully : for n = ", i, " in ", execution)


def main_exo_2():
    n = int(input("Jusqu'à la valeur : "))

    #getData_suite_recu(n, suite_recurrente_recu)
    getData_suite_recu(n, suite_recurrente_iter)
    displayData(execution_time)
    root.mainloop()


def isMultiple(nb, value):

    if nb % value == 0:
        return True
    return False


def reset_coched(n):
    all_coched = []
    for i in range(1, n + 1):
        all_coched.append(False)
    return all_coched


def eratosthene_crible(n):

    premier = []
    all_number = []

    for i in range(1, n):
        all_number.append(i)

    del(all_number[0])

    while len(all_number) != 0:
        premier.append(all_number[0])
        i = all_number[0]

        for number in all_number:
            if number % i == 0:
                del(all_number[all_number.index(number)])

    return premier


def main_exo_3():
    print(eratosthene_crible(100))


if __name__ == "__main__":
    main_exo_3()
