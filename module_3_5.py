def get_multiplied_digits(number):
    number = int(number) # преобразуем в число, автоматически уберутся нули, если они были в начале числа
    str_number = str(number) # преобразуем переменную в сторку, чтобы вытащить первую цифру, которая точно не ноль
    first = int(str_number[0]) # присваиваем переменной первую цифру
    if len(str_number) == 1: # условие для выхода из рекурсии, если длина стороки равно 1 символу
        return first # возвращаем только последнюю цифру
    return first * get_multiplied_digits(int(str_number[1:])) # рекурсия по условия задачи

result = get_multiplied_digits(40203)
print(result)
