import random as random
import time


def build_couple(elements):
    couples = []

    for i in range(len(elements)):
        for j in range(i, len(elements)):
            if i != j:
                couples.append([elements[i], elements[j]])

    return couples


def append(valeur, valeur_bis):
    result = valeur + valeur_bis
    if result >= 0:
        return result
    return -1


def soustraction(valeur, valeur_bis):
    result = valeur - valeur_bis
    if result >= 0:
        return result
    elif valeur_bis - valeur >= 0:
        return valeur_bis - valeur
    return -1


def multiplication(valeur, valeur_bis):
    result = valeur * valeur_bis
    if result >= 0:
        return result
    return -1


def division(valeur, valeur_bis):
    if valeur_bis > 0 and valeur % valeur_bis == 0:
        return valeur / valeur_bis
    elif valeur > 0 and valeur_bis % valeur == 0:
        return valeur_bis / valeur
    return -1


def build_ensemble(elements, couple):
    add = append(couple[0], couple[1])
    sous = soustraction(couple[0], couple[1])
    multi = multiplication(couple[0], couple[1])
    divide = division(couple[0], couple[1])

    ensemble_add = [add]
    ensemble_sous = [sous]
    ensemble_multi = [multi]
    ensemble_divide = [divide]

    for element in elements:
        ensemble_add.append(element)
        ensemble_sous.append(element)
        ensemble_multi.append(element)
        ensemble_divide.append(element)

    ensemble = []
    if add != -1:
        ensemble.append(ensemble_add)
    if sous != -1:
        ensemble.append(ensemble_sous)
    if multi != -1:
        ensemble.append(ensemble_multi)
    if divide != -1:
        ensemble.append(ensemble_divide)

    return ensemble


def check_result_find(result, ensemble):

    for liste in ensemble:
        if liste.__contains__(result):
            return True

    return False


def is_possible(result, elements, find, iter):
    if find:
        return True, iter
    couples = build_couple(elements)
    if elements[0] is not None and isinstance(elements[0], list):
        iter += 4
        for i in range(len(elements)):
            couples = build_couple(elements[i])
            for couple in couples:
                rest = elements[i].copy()
                rest.remove(couple[0])
                rest.remove(couple[1])
                ensemble = build_ensemble(rest, couple)
                if check_result_find(result, ensemble):
                    return True, iter
                res = is_possible(result, ensemble, find, iter)
                find = res[0]
                iter = res[1]
                if find:
                    return find, iter
    else:
        for couple in couples:
            elements_copy = elements.copy()
            elements_copy.remove(couple[0])
            elements_copy.remove(couple[1])
            ensemble = build_ensemble(elements_copy, couple)
            if check_result_find(result, ensemble):
                return True, iter
            res = is_possible(result, ensemble, find, iter)
            find = res[0]
            iter = res[1]
            if find:
                return find, iter
    return find, iter


def get_a_random_in_this_list(list):
    return list[random.randint(0, len(list) - 1)]


def random_plate():
    plates = [25, 25, 50, 50, 75, 75, 100, 100]
    for i in range(2):
        for j in range(1, 11):
            plates.append(j)

    six_plates = []
    for i in range(6):
        valeur_selected = get_a_random_in_this_list(plates)
        six_plates.append(valeur_selected)
        plates.remove(valeur_selected)

    return six_plates


def get_result_to_find():
    return random.randint(100, 999)


def temps_moyen(nb_test):
    temps_total = 0

    for i in range(nb_test):
        begin = time.time()
        result = get_result_to_find()
        plates = random_plate()
        res = is_possible(result, plates, False, 0)
        end = time.time()

        temps_total += end - begin

        print("After", (end - begin), "seconds, found ? :", res[0], "in", res[1], "iterations")

    return temps_total / nb_test


def main():
    nb_test = 1000
    print("\nTime :", temps_moyen(nb_test), "seconds for", nb_test, "tests")


if __name__ == "__main__":
    main()
