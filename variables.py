from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr


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
    print(all_variables)
    return all_variables


def set_symbols(array) -> dict:
    all_symbols = {}
    for i in range(0, len(array)):
        all_symbols[str(array[i])] = symbols(array[i])

    print(all_symbols)
    return all_symbols


def replacement(equation, all_symbols):
    for key in all_symbols:
        print(key, all_symbols[key])
        # if key in equation:
        #     new_equation = equation.replace(key)

    print(parse_expr(equation))
