def elemordonatecresc(list):
    sortedlist = list[:]
    sortedlist.sort()
    if sortedlist == list:
        return True
    return False


def readfloatlist() -> list[float]:
    list = []
    givenstring = input("Dati lista cu elemente separate prin virgula")
    numbers_as_string = givenstring.split(",")
    for x in numbers_as_string:
        list.append(float(x))
    return list

def readintlist() -> list[int]:
    list = []
    givenstring = input("Dati lista cu elemente separate prin virgula")
    numbers_as_string = givenstring.split(",")
    for x in numbers_as_string:
        list.append(int(x))

    return list


def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de nr ordonate crescator
    :param lst: lista nr intregi
    :return: cea mai lunga subsecventa de nr ordonate crescator
    '''
    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if elemordonatecresc(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventamax):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def listwithzero(l):
    for x in l:
        if x != 0:
            return False
    return True


def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    '''
    Determina cea mai lunga subsecventa de numere cu popr. ca toate au partea fractionara = partea intreaga
    :param lst: lista cu numere reale
    :return: cea mai lunga subsecventa cu proprietatea ca toate numerele au pi = pf
    '''
    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if listwithzero(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventamax):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def is_palindrome(n):
    '''
    Verifica daca un numar este palindrom
    :param n:  numar intreg
    :return: Retruneaza adevarat daca nr este palindrom si False in caz contrar
    '''
    if n < 10:
        return False
    ogl = 0
    aux = n
    while aux > 0:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10
    if ogl == n:
        return True
    else:
        return False

def  get_longest_all_palindromes(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere cu popr. ca toate nr sunt palindrom
    :param lst: lista cu numere reale
    :return: cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindrom
    '''
    subsecventamax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if is_palindrome(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventamax):
                subsecventamax = lst[i:j + 1]
    return subsecventamax


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([12, 11, 22, 44, 54, 22]) == [11, 22, 44]
    assert get_longest_all_palindromes([12, 11, 22, 44, 54, 22, 66, 101, 202]) == [22, 66, 101, 202]


def test_elemordonatecresc():
    assert elemordonatecresc([]) is True
    assert elemordonatecresc([10, 4, 5]) is False
    assert elemordonatecresc([10, 20, 30]) is True


def test_get_longest_sorted_asc():
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([1, 2, 0, 0]) == [0, 0]
    assert get_longest_equal_int_real([1, 2, 0, 0, 32, 0, 0, 0]) == [0, 0, 0]


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([1, 2, 0, 0]) == [0.0, 0.0]
    assert get_longest_equal_int_real([1, 2, 0, 0 , 32, 0, 0, 0]) == [0.0, 0.0, 0.0]


def main():
    test_get_longest_sorted_asc()
    test_get_longest_equal_int_real()
    test_elemordonatecresc()
    print("""
    1, Determinati cea mai lunga subsecventa de numere ordonate crescator dintr un sir dat
    2, Determinati cea mai lunga subsecventa cu proprietatea ca elementele au partea fractionara egala cu partea intreaga
    3, Determinati cea mai lunga subsecventa cu proprietatea ca toate elem sunt palindrom
    x, Iesire""")
    while True:
        option = input("Selectati o funtie")
        if option == "1":
            l = readintlist()
            print(get_longest_sorted_asc(l))
        elif option == "2":
            l = readfloatlist()
            print(get_longest_equal_int_real(l))
        elif option == '3':
            l = readintlist()
            print(get_longest_all_palindromes(l))
        elif option == "x":
            break
        else:
            print("Nu ati selectat o optiune valida!")


main()
