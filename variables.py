from sympy import symbols
from sympy.simplify.simplify import simplify


def get_variables(eq):
    all_variables = list()
    for sub_eq in eq:
        var = ''
        if '+' in sub_eq:
            var = sub_eq.split('+')
        elif '-' in sub_eq:
            var = sub_eq.split('-')
        elif '/' in sub_eq:
            var = sub_eq.split('/')
        elif '*' in sub_eq:
            var = sub_eq.split('*')

        all_variables.extend(var)

    all_variables = [x.strip(' ') for x in all_variables]
    return all_variables


def set_symbols(array) -> dict:
    all_symbols = {}
    for i in range(0, len(array)):
        all_symbols[str(array[i])] = symbols(array[i])

    return all_symbols


def split(equation):
    equation = equation.split(' ')
    split = []
    for x in equation:
        if '(' in x:
            out = x.split('(')
            split.extend('(')
            for y in out:
                if y != '':
                    split.append(y)

        elif ')' in x:
            out = x.split(')')
            for y in out:
                if y != '':
                    split.append(y)
            split.extend(')')

        else:
            split.extend(x)

    return split


def replace(splitted):
    count = 0
    for x in splitted:
        if count == 0:
            expr = symbols(x)
            count += 1
        else:
            expr += symbols(x)

    final_expr = "".join(splitted)
    final_expr = simplify(final_expr)
    return final_expr
