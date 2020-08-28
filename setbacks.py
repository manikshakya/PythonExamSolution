def setbacks(lifts):
    counter = 0
    backs = []
    for i in lifts:
        if counter < i:
            counter = i
        else:
            backs.append(i)

    return backs

class Test:
    print(setbacks([140, 150, 165, 141, 164, 156, 187, 163]))