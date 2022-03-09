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


def crible(n):
    all_value = list(range(1, n + 1))
    all_coched = []
    target_index = 0

    for i in range(1, n + 1):
        all_coched.append(False)

    # Se placer sur le 1
    all_coched[0] = True

    # Se placer sur le prochain non coché
    while all_coched[target_index]:
        target_index += 1

    # Cocher tous ses multiples
    for i in range(1, n):
        if isMultiple(all_value[target_index], all_value[i]):
            all_coched[i] = False

    for i in range(1, n):
        # target est le 2
        target_index = 1

        # Se placer sur le prochain non coché
        while target_index < n and all_coched[target_index]:
            target_index += 1
        print(all_coched)

        # Cocher tous ses multiples
        for j in range(1, target_index):
            if isMultiple(all_value[target_index], all_value[j]):
                all_coched[j] = False



def main_exo_3():
    crible(100)


if __name__ == "__main__":
    main_exo_3()
