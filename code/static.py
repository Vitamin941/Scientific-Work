from sympy import Matrix, Symbol, symbols

t = Symbol('t')
t0, t1, t2 = symbols('t:3')
t0_num, t1_num, t2_num, T_num = 0, 1, 2, 3
T = Symbol('T')

tau = Symbol('tau')
g = Symbol('g')

B = Matrix([
    [0, 0], [1, 0], [0, 0], [0, 1]
])

f = Matrix([
    [0], [0], [0], [-g]
])


def replace_syms_to_nums(expression):
    return expression.replace(t0, t0_num)\
        .replace(t1, t1_num)\
        .replace(t2, t2_num)\
        .replace(T, T_num)
