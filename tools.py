def get_brackets(equation) -> tuple:
    opening = list()
    closing = list()

    for i in range(0, len(equation)):
        if equation[i] == '(':
            opening.append(i)

        if equation[i] == ')':
            closing.append(i)

    return (opening, closing)


def get_operators(equation, opening, closing) -> list:
    operators = list()
    max_operator = len(opening) - 1
    for i in range(0, max_operator):
        operator = equation[closing[i]+1:opening[i+1]]
        operators.append(operator)

    return operators


def get_sub_eq(equation, opening, closing) -> list:
    parts = list()
    for i in range(0, len(opening)):
        value_x = opening[i] + 1
        value_y = closing[i]
        parts.append(equation[value_x:value_y])

    return parts
