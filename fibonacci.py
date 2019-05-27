def fibonacci(number_1, number_2, first, count):
    print(str(number_1))
    if first < count:
        first+=1
        return fibonacci(number_2, number_1 + number_2, first, count)

fibonacci(1, 1, 1, 100)

def list_fibonacci(number_1, number_2, first, count, list_f):
    list_f.append(str(number_1))
    if first < count:
        first+=1
        return list_fibonacci(number_2, number_1 + number_2, first, count, list_f)

    return list_f

list_f = list_fibonacci(1, 1, 1, 100, list())

print(str(list_f))
