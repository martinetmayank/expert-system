from sympy.core.function import expand
from sympy.core.symbol import symbols
from sympy.simplify.simplify import simplify
from utils import get_brackets, get_sub_eq, get_operators
from variables import get_variables, replacement, set_symbols
from display import show


def main():
    pass


if __name__ == "__main__":

    equation = '(axy + by)*(cx + dy)'
    opening, closing = get_brackets(equation)
    sub_equations = get_sub_eq(equation, opening, closing)
    operators = get_operators(equation, opening, closing)

    print(sub_equations)
    print(operators)
    all_variables = get_variables(sub_equations)
    all_symbols = set_symbols(all_variables)
    # replacement(equation, all_symbols)
