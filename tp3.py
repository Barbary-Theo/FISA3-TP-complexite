def oui():
    print("oui")


def build_couple(elements):
    couples = []

    for valeur in elements:
        for valeur_bis in elements:
            if valeur != valeur_bis and \
                    not (couples.__contains__([valeur, valeur_bis]) or couples.__contains__([valeur_bis, valeur])):
                couples.append([valeur, valeur_bis])

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
    return -1


def multiplication(valeur, valeur_bis):
    result = valeur * valeur_bis
    if result >= 0:
        return result
    return -1


def division(valeur, valeur_bis):
    result = valeur / valeur_bis
    if result >= 0 and valeur % valeur_bis == 0:
        return result
    return -1


def create_ensemble_part(elements, couple, operation):
    result = operation(couple[0], couple[1])
    if result == -1:
        return None

    ensemble_part = [result]

    for element in elements:
        ensemble_part.append(element)

    return ensemble_part


def build_ensemble(elements, couple):
    add = create_ensemble_part(elements, couple, append)
    soustract = create_ensemble_part(elements, couple, soustraction)
    multi = create_ensemble_part(elements, couple, multiplication)
    divide = create_ensemble_part(elements, couple, division)

    ensemble = []

    if add is not None:
        ensemble.append(add)
    if soustract is not None:
        ensemble.append(soustract)
    if multi is not None:
        ensemble.append(multi)
    if divide is not None:
        ensemble.append(divide)

    return ensemble


def is_possible(result, elements):

    couples = build_couple(elements)

    if elements[0] is not None and isinstance(elements[0], list):
        for ensemble in elements:
            couples = build_couple(ensemble)
            for couple in couples:
                ensemble_copy = ensemble.copy()
                if len(ensemble_copy) >= 2:
                    ensemble_copy.remove(couple[0])
                    ensemble_copy.remove(couple[1])
                    ensemble = build_ensemble(ensemble_copy, couple)
                    print(ensemble)
                    is_possible(result, ensemble)
    else:
        for couple in couples:
            elements_copy = elements.copy()
            elements_copy.remove(couple[0])
            elements_copy.remove(couple[1])
            ensemble = build_ensemble(elements_copy, couple)
            print(ensemble)
            is_possible(result, ensemble)


def main():
    # print(build_ensemble([2, 3, 4, 5], [0, 1]))
    print(is_possible(10, [0, 1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
