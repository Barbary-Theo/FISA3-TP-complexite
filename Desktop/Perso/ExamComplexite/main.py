import math
import time


def premier(n):

    cpt = 2
    while cpt * cpt <= n:
        if n % cpt == 0:
            return False
        cpt += 1

    return True


def main_premier():

    for n in range(2, 50):
        print(n, "premier : ", premier(n))


def mystere(n):

    if n == 0:
        return 2
    else:
        return mystere(n - 1) * mystere(n - 1)


# ??
def mystere_refactor(n):

    if n == 0:
        return 2
    else:
        res = mystere(n - 1)
        return res * res


def mystere_iter(n):

    res = 2
    cpt = 0

    while cpt < n:
        res = res * res
        cpt += 1

    return res

def main_mystere_test():
    deb = time.time()
    mystere(20)
    fin = time.time()

    print("Mystere de base pour n = 20 :", fin - deb, "secondes")

    deb = time.time()
    mystere_refactor(20)
    fin = time.time()

    print("Mystere amélioré pour n = 20 :", fin - deb, "secondes")


def main_mystere():
    for n in range(0, 15):
        deb = time.time()
        mystere(n)
        fin = time.time()
        print("n :", n, ", temps :", fin - deb)

def main_mystere_refactor():

    for n in range(0, 15):
        mystere_refactor(n)


def main_mystere2():

    for n in range(0, 15):
        mystere_iter(n)


def main_mystere_timing():

    init_mystere = time.time()
    mystere(20)
    end_mystere = time.time()
    print("Mystere de base pour n = 20 :", end_mystere - init_mystere, "secondes")

    init_mystere_refactor = time.time()
    mystere_refactor(20)
    end_mystere_refactor = time.time()
    print("Mystere amélioré pour n = 20 :", end_mystere_refactor - init_mystere_refactor, "secondes")

    init_mystere_iter = time.time()
    mystere_iter(20)
    end_mystere_iter = time.time()
    print("Mystere itératif pour n = 20 :", end_mystere_iter - init_mystere_iter, "secondes")


def fibo_formulation(n):
    return (1 / math.sqrt(5)) * (math.pow((1 + math.sqrt(5)) / 2, n) - math.pow((1 - math.sqrt(5)) / 2, n))


def fibo_expo(n):
    return math.pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5)


def main_fibo_formulation():

    for n in range(0, 100):
        print(n, "fibo formulation :", fibo_formulation(n))


def main_fibo_coherence():
    base = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    for i in range(1, len(base)):
        test = fibo_formulation(i + 1)
        print("Base : ", base[i], ", calcul :", test, ", différence :", math.fabs(base[i] - test))


def main_fibo_expo():

    for n in range(0, 20):
        print(n, "fibo exponentielle :", fibo_expo(n), "| Erreur à",
              (math.fabs(fibo_expo(n) - fibo_formulation(n))))


def fibo_decomposition(nb):
    cpt = 0

    all_fibo = []
    result_fibo = fibo_formulation(2)
    i = 3

    while result_fibo < nb:
        all_fibo.append(result_fibo)
        result_fibo = round(fibo_formulation(i))
        i += 1
        cpt += 1

    index, remaining = len(all_fibo) - 1, nb
    decomposition = str(all_fibo[index])

    remaining = nb - all_fibo[index]
    index -= 2

    while remaining > 0 and index >= 0:
        cpt += 1
        if remaining - all_fibo[index] >= 0:
            decomposition += " + " + str(all_fibo[index])
            remaining -= all_fibo[index]
            index -= 2
        else:
            index -= 1
    return decomposition


def main_fibo_decomposition():
    print(fibo_decomposition(1054))


if __name__ == '__main__':
    main_fibo_decomposition()
