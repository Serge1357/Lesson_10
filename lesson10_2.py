try:
    numbers = eval(input("введить список із числами"))
    sorted_numbers = sorted(numbers)
    k = 0
    for i in range(len(sorted_numbers)-1):
        if sorted_numbers[i] == sorted_numbers[i+1]:
            k = 1
    if k == 0:
        print("Усі числа у списку унікальні")
    else:
        print("у списку наявні співпадіння")
except NameError:
    print("надано не числовой список")
except TypeError:
    print("надано лише одно число")