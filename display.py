import subprocess
from sympy.printing.dot import dotprint


def show(expr):
    output = dotprint(expr)

    with open('output.dot', mode="w") as f:
        f.write(output)

    subprocess.run(['dot', '-Tpng', 'output.dot', '-o', 'output.png'])
