import re

def simple_calculator(expression):

    numbers = re.split(r"\-|\+", expression)
    numbers = list(map(int, numbers))

    operators = re.findall(r"\-|\+", expression)
    result = 0

    if len(numbers) == 1:
        return numbers[0]

    for i in range(len(operators)):
        if i == 0:
            if operators[i] == "-":
                result = numbers[i] - numbers[i + 1]
            elif operators[i] == "+":
                result = numbers[i] + numbers[i + 1]
        else:
            if operators[i] == "-":
                result -= numbers[i + 1]
            elif operators[i] == "+":
                result += numbers[i + 1]
        
    return result

assert simple_calculator("5+5") == 10
assert simple_calculator("10-6") == 4
assert simple_calculator("1+2-4+124-212") == -89
assert simple_calculator("214") == 214