# 1.	Se tiene un concurso de programas que sean capaces de evaluar expresiones algebraicas,
# se tendrán la asignación ‘=’, la suma, resta, multiplicación y división, además se trabajaran
# con valores de tipo real. La entrada estará compuesta por una cantidad de operaciones N y a
# continuación N cadenas que contendrán asignaciones a variables y también uso de los valores
# de dichas variables. Al final el programa debe imprimir los valores de todas las variables en
# orden alfabético.

# Input
# 3
# X=2
# Y=X+4
# X=Y-1

# Output
# X=5, Y=6

# input
# 5
# A=2+2
# B=A*A
# C=A+B*2
# B=A-1
# A=2

# output
# A=2,B=3,C=36

n = int(input())
variables = {}

for _ in range(n):
    line = input().replace(' ', '')
    var, expr = line.split('=')
    # Evaluate the expression using current variables
    try:
        value = eval(expr, {}, variables)
    except Exception:
        value = 0
    variables[var] = value

# Print variables in alphabetical order
output = ','.join(f"{k}={int(v) if int(v) == v else v}" for k, v in sorted(variables.items()))
print(output)