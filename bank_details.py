def bank_details(iban):
    newiban = iban.replace(" ", "")

    if len(newiban) != 22:
        raise ValueError

    countrycode = newiban[0:2]
    check = newiban[2:4]
    bankreference = newiban[4:8]
    sortcode = newiban[8:14]
    accountnumber = newiban[14:22]

    if countrycode != "IE":
        raise ValueError

    if check != "29":
        raise ValueError

    if bankreference != "BOFI" and bankreference != "AIBK":
        raise ValueError

    return [sortcode, accountnumber]


class Test:
    print(bank_details('IE29 AIBK 9311 5212 3456 78'))
