from typing import List

import sympy as sp
from sympy import Matrix, integrate, pprint

from static import *
from integrator import integrate_matrix

sp.init_printing(use_unicode=False, wrap_line=False)

x_0 = Matrix([
    [0], [0], [0], [0]
])

x_T = Matrix([
    [3], [2], [2], [1]
])

alpha = Matrix([
    [2], [1]
])

F = Matrix([
    [1, 0, 1, 0],
    [0, 1, 0, 1]
])


def X(time_moment=None, tau=tau):
    def x(time_moment_start, time_moment_end, ind: List[int]):
        if ind[0] == ind[1]:
            return 1
        else:
            return time_moment_start - time_moment_end

    x11 = x(time_moment, tau, [1, 1])
    x12 = x(time_moment, tau, [1, 2])
    x22 = x(time_moment, tau, [2, 2])
    x33 = x(time_moment, tau, [3, 3])
    x34 = x(time_moment, tau, [3, 4])
    x44 = x(time_moment, tau, [4, 4])

    return Matrix([
        [x11, x12, 0, 0],
        [0, x22, 0, 0],
        [0, 0, x33, x34],
        [0, 0, 0, x44]
    ])


def F_func(time_arg):
    """
    Функция возвращающая матрицу F
    """
    return F * X(time_moments.get("t1"), time_arg) + F * X(time_moments.get("t2"), time_arg)


F_matr = {
    "tau": F_func(tau),
    "t": F_func(t),
    "t0": F_func(time_moments.get("t0"))
}

a = F_matr.get("tau") * B
b = X(time_moments.get("T"), tau) * B
H = a.col_join(b)
Q = H * H.T


def find_tetta_vector():
    column_1 = alpha - F_matr.get("t0") * x_0 - (integrate(F * X(time_moments.get("t1"), t), (t, t0_num, t1_num)) * f) \
               - (integrate(F * X(time_moments.get("t2"), t), (t, t0_num, t2_num)) * f)
    column_2 = x_T - X(time_moments.get("T"), time_moments.get("t0")) * x_0 - integrate(X(time_moments.get("T"), t) * f,
                                                                                        (t, t0_num, T_num))
    return replace_syms_to_nums(column_1.col_join(column_2))


tetta = find_tetta_vector()
Q_integrated = integrate_matrix()

def u(tau):
    u = [0] * 3
    zero_matrix = Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ])
    sum_ = F * X(time_moments.get("t1"),tau)  + F * X(time_moments.get("t2"),tau)
    u[0] = replace_syms_to_nums(sp.simplify(B.T * sum_.T.row_join(X(time_moments.get('T'), tau).T) * Q_integrated.inv() * tetta))
    
    u[1] = replace_syms_to_nums(sp.simplify(B.T * (F * X(time_moments.get("t2"),tau)).T.row_join(X(time_moments.get('T'), tau).T) * Q_integrated.inv() * tetta))
    
    u[2] = replace_syms_to_nums(sp.simplify(B.T * zero_matrix.T.row_join(X(time_moments.get('T'), tau).T) * Q_integrated.inv() * tetta))
    return u


mov_1 = integrate(X(t, tau) * B * u(tau)[0], (tau, 0, t)) + integrate(X(t, tau) * f, (tau, 0, t))
int_1 = integrate(X(t, tau) * B * u(tau)[1], (tau, 1, t)) +  integrate(X(t, tau) * B * u(tau)[0], (tau, 0, 1))
mov_2 = int_1 + integrate(X(t, tau) * f, (tau, 0, t))
int_2 = integrate(X(t, tau) * B * u(tau)[1], (tau, t1_num, t2_num)) +  integrate(X(t, tau) * B * u(tau)[0], (tau, t0_num, t1_num)) + integrate(X(t, tau) * B * u(tau)[2], (tau, t2_num, t)) 
mov_3 = int_2 + integrate(X(t, tau) * f, (tau, 0, t))
#pprint(integrate(X(time_moments.get('t0'), tau) * f, (tau, t0_num, t)))

pprint(replace_syms_to_nums(sp.expand(sp.simplify(mov_1))))
print("-------------------------------------------")
pprint(replace_syms_to_nums(sp.simplify(mov_2)))
print("-------------------------------------------")
pprint(replace_syms_to_nums(sp.simplify(mov_3)))
print("-------------------------------------------")
pprint(replace_syms_to_nums(sp.simplify(F * mov_2 + F * mov_3)))
#sum_1 = F * X[time_moments.get("t1"),time_moments.get("t0")] * x_0 + F * X[time_moments.get](tau,0,t)


#pprint(X(t, tau) * B * u(tau)[1])
#pprint(integrate(X(t, tau) * B * u(tau)[1],(tau,0,t)))
#pprint(X(t, tau) * f)
#pprint(integrate(X(t, tau) * f,(tau,0,t)))