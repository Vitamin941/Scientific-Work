from sympy import Matrix, Symbol, symbols

t = Symbol('t')
t0_num, t1_num, t2_num, T_num = 0, 1, 2, 3
time_moments = {
    "t0": Symbol("t0"),
    "t1": Symbol("t1"),
    "t2": Symbol("t2"),
    "T": Symbol('T')
}
tau = Symbol('tau')
g = Symbol('g')

B = Matrix([
    [0, 0], [1, 0], [0, 0], [0, 1]
])

f = Matrix([
    [0], [0], [0], [-g]
])


def replace_syms_to_nums(expression):
    return expression.replace(time_moments.get("t0"), t0_num)\
        .replace(time_moments.get("t1"), t1_num)\
        .replace(time_moments.get("t2"), t2_num)\
        .replace(time_moments.get("T"), T_num)
