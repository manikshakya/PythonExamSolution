def teenagers(ages):
    lists = []
    for i in ages:
        if i == 13 or i == 14 or i == 15 or i == 16 or i == 17 or i == 18 or i == 19:
            lists.append(i)
    return lists

class Test:

    print(teenagers([15, 27, 5, 22, 51, 52, 49, 41, 19, 65]))



