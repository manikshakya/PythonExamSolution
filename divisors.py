def divisors(number):
    divisor = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisor.append(i)

    divisor.pop(0)
    divisor.pop()

    return divisor

class Test:
    print(divisors(18))