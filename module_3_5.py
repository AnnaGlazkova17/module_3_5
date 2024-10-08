def get_multiplied_digits(number):
    number = int(number) # преобразуем в число, автоматически уберутся нули, если они были в начале числа
    str_number = str(number) # преобразуем переменную в сторку, чтобы вытащить первую цифру, которая точно не ноль
    first = int(str_number[0]) # присваиваем переменной первую цифру
    if len(str_number) == 1 and first != 0: # условие для выхода из рекурсии, если длина стороки равно 1 символу
        return first # возвращаем только последнюю цифру
    elif len(str_number) == 1 and first == 0: # если последня цифра ноль, то возвращаем 1
        return 1
    return first * get_multiplied_digits(int(str_number[1:])) # рекурсия по условия задачи

result = get_multiplied_digits(40203)
print(result)
