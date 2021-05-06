from tools import get_brackets, get_sub_eq, get_operators
from variables import get_variables, replace, set_symbols, split
from display import show
from sympy import expand


def main():
    opening, closing = get_brackets(equation)
    sub_equations = get_sub_eq(equation, opening, closing)
    main_operator = get_operators(equation, opening, closing)

    all_variables = get_variables(sub_equations)
    all_symbols = set_symbols(all_variables)

    # print(f'sub_equations {sub_equations}')
    # print(f'main_operator {main_operator}')
    # print(f'all_variables {all_variables}')
    # print(f'all_symbols {all_symbols}')
    splitted_eq = split(equation)
    expr = replace(splitted_eq)
    expanded_form = expand(expr)
    show(expanded_form)


if __name__ == "__main__":
    equation = '(axy + by) * (cx + dy)'
    main()
