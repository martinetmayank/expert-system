from sympy import symbols, expand
from utils import get_brackets, get_sub_eq, get_operators


def main():
    pass


if __name__ == "__main__":
    a = symbols('a')
    b = symbols('b')
    c = symbols('c')
    d = symbols('d')
    x = symbols('x')
    y = symbols('y')

    equation = '(ax + by)*(cx + dy)'
    opening, closing = get_brackets(equation)
    sub_equations = get_sub_eq(equation, opening, closing)
    operators = get_operators(equation, opening, closing)
