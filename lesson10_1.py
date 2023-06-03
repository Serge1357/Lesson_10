def month_by_number(number):
    perelik = {"1": "січень", "2": "лютий","3": "березень", "4": "квітень",
               "5": "травень", "6": "червень","7": "липень", "8": "серпень",
               "9": "вересень", "10": "жовтень","11": "листопад", "12": "грудень"}
    try:
        return perelik[number]
    except KeyError as ex:
        number = str(number)
        try:
            return perelik[number]
        except KeyError as ex:
            print(f"аргумент {number}  не є номером місяця")
            return ""


print(month_by_number("3"))
print(month_by_number(7))
print(month_by_number("vvdd"))