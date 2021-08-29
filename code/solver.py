from typing import List

import sympy as sp
from sympy import Matrix, integrate, pprint

sp.init_printing(use_unicode=False, wrap_line=True)

true = True
false = False
t = sp.Symbol('t')
t0, t1, t2 = sp.symbols('t:3')
T = sp.Symbol('T')
t0_num, t1_num, t2_num, T_num = 0, 1, 2, 3
tau = sp.Symbol('tau')
g = sp.Symbol('g')

x_0 = Matrix([
    [0], [0], [0], [0]
])

x_T = Matrix([
    [3], [2], [2], [1]
])

alpha = Matrix([
    [2], [1]
])

B = Matrix([
    [0, 0], [1, 0], [0, 0], [0, 1]
])
f = Matrix([
    [0], [0], [0], [-g]
])

F = Matrix([
    [1, 0, 1, 0],
    [0, 1, 0, 1]
])

# F_kostyl = Matrix([
#     [1, 0, 1, 5/12],
#     [0, 1, 0, 1/2]
# ]) 


# def init_x_vector(t: sp.symbols):
#     x1 = sp.Function('x1')
#     x2 = sp.Function('x2')
#     x3 = sp.Function('x3')
#     x4 = sp.Function('x4')

#     return sp.Matrix([
#         [x1(1)],[x2(1)],[x3(1)],[x4(1)]
#     ])


def X(t=None, tau=tau):
    """

    :param t:
    :param tau:
    :return:
    """

    def x(t, T, ind: List[int]):
        """

        :param t:
        :param T:
        :param ind:
        :return:
        """
        if ind[0] == ind[1]:
            return 1
        else:
            return t - T

    x11 = x(t, tau, [1, 1])
    x12 = x(t, tau, [1, 2])
    x22 = x(t, tau, [2, 2])
    x33 = x(t, tau, [3, 3])
    x34 = x(t, tau, [3, 4])
    x44 = x(t, tau, [4, 4])

    return sp.Matrix([
        [x11, x12, 0, 0],
        [0, x22, 0, 0],
        [0, 0, x33, x34],
        [0, 0, 0, x44]
    ])


def F_func(arg=None):
    """

    :param arg:
    :return:
    """
    return F * X(t1, arg) + F * X(t2, arg)


F_tau = F_func(tau)
F_t = F_func(t)
F_t0 = F_func(t0)

# pprint(F_tau)
# pprint(F_t)
# pprint(F_t0)

a = F_tau * B
b = X(T, tau) * B
H = a.col_join(b)
Q = sp.Mul(H * H.T, evaluate=true)
pprint(Q, num_columns=200)
eq = sp.expand(Q[0, 0], deep=False)
#pprint(sp.Mul(H[0, 0] * H.T[0, 0], evaluate=False), num_columns=100)
# pprint(eq)


def integrate_eq(exp):
    """

    :param exp:
    :return:
    """
    result = 0
    for arg in exp.args:
        t_str = find_str_eqvivalent_in_symbol(str(arg))
        if t_str == 't1':
            print(f"{arg} -----> {integrate(replace_syms_to_nums(arg), (tau, 0, t1_num))}")
            result = result + integrate(replace_syms_to_nums(arg), (tau, 0, t1_num))
        elif t_str == 't2':
            print(f"{arg} -----> {integrate(replace_syms_to_nums(arg), (tau, 0, t2_num))}")
            result = result + integrate(replace_syms_to_nums(arg), (tau, 0, t2_num))
        else:
            print(f"{arg} -----> {integrate(replace_syms_to_nums(arg), (tau, 0, T_num))}")
            integral_t1 = integrate(arg, (tau, 0, t1_num)) / 2
            integral_t2 = integrate(arg, (tau, 0, t2_num)) / 2
            # result = result + integrate(replace_syms_to_nums(arg), (tau, 0, T_num))
            result = result + integral_t1 + integral_t2
    return result


def find_str_eqvivalent_in_symbol(arg):
    """

    :param arg:
    :return:
    """
    if 't1' in arg:
        return 't1'
    elif 't2' in arg:
        return 't2'
    else:
        return None


def replace_syms_to_nums(expression):
    """

    :param expression:
    :return:
    """
    return expression.replace(t0, t0_num)\
        .replace(t1, t1_num)\
        .replace(t2, t2_num)\
        .replace(T, T_num)


#pprint(replace_syms_to_nums(integrate_eq(eq)))
#pprint(integrate_eq(eq))


_column_1 = alpha - F_t0 * x_0 - integrate(F_t * f, (t, t0_num, T_num))
_column_2 = x_T - X(T, t0) * x_0 - integrate(X(T, t) * f, (t, t0_num, T_num))

#pprint(replace_syms_to_nums(_column_1).col_join(replace_syms_to_nums(_column_2)))

# pprint(eq)
# pprint(eq_replaced)
# pprint(integrate(eq_replaced, (tau, t0_num, t2_num)))

# for j in eq.args:
#     print(j.args)
#     j_i = sp.integrate(j.args[1], (tau,t0_num,t1_num))
#     sp.pprint(sp.Mul(j.args[0], j_i))
#
# #a = str(eq).split("+")
# a = re.split('[+-]',str(eq))
# print(sp.Function(a[0]))
