from sympy import integrate, Matrix, simplify, symbols, Symbol
import sympy as sp

t = Symbol('t')
times = [Symbol('t0'), Symbol('t1'), Symbol('t2'), Symbol('T')]
t0_num, t1_num, t2_num, T_num = 0,1,2,3

tau = Symbol('tau')
g = Symbol('g')

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

A = Matrix([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
])

integral_range_1 = (tau, t0_num, t1_num)
integral_range_2 = (tau, t0_num, t2_num)
integral_range_3 = (tau, t0_num, T_num)

def init_times(times):
    t0_num, t1_num, t2_num, T_num = times

def replace_syms_to_nums(expression, times):
    return expression.replace(times[0], t0_num) \
        .replace(times[1], t1_num) \
        .replace(times[2], t2_num) \
        .replace(times[3], T_num)


def fundamental_matrix(time_moment=None, tau=tau):
    def element(time_moment_start, time_moment_end, ind):
        return 1 if ind[0] == ind[1] else time_moment_start - time_moment_end

    element11 = element(time_moment, tau, [1, 1])
    element12 = element(time_moment, tau, [1, 2])
    element22 = element(time_moment, tau, [2, 2])
    element33 = element(time_moment, tau, [3, 3])
    element34 = element(time_moment, tau, [3, 4])
    element44 = element(time_moment, tau, [4, 4])

    return Matrix([
        [element11, element12, 0, 0],
        [0, element22, 0, 0],
        [0, 0, element33, element34],
        [0, 0, 0, element44]
    ])


def F_matrix(times, time_arg):
    """
    Функция вычисления матрицы F.
    :param times:
    :param time_arg:
    :return:
    """
    return F * fundamental_matrix(times[1], time_arg) + F * fundamental_matrix(times[2], time_arg)


def find_tetta_vector(F_t0, x0, xT):
    column_1 = alpha - F_t0 * x0 - (integrate(F * fundamental_matrix(times[1], t), (t, t0_num, t1_num)) * f) - (
                integrate(F * fundamental_matrix(times[2], t), (t, t0_num, t2_num)) * f)
    column_2 = xT - fundamental_matrix(times[3], times[0]) * x0 - integrate(fundamental_matrix(times[3], t) * f,
                                                                            (t, t0_num, T_num))

    return replace_syms_to_nums(column_1.col_join(column_2), times)


def simple(expression, times):
    return replace_syms_to_nums(simplify(expression), times)


def control(tau, Q, tetta):
    """
    Функция вычисляющая управления в различные моменты времени
    :return: Вектор управления
    """
    u = [0] * 3
    zero_matrix = Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])
    u[0] = simple((B.T * F_matrix(times, tau).T.row_join(fundamental_matrix(times[3], tau).T) * Q.inv() * tetta), times)

    u[1] = simple((B.T * (F * fundamental_matrix(times[2], tau)).T.row_join(
        fundamental_matrix(times[3], tau).T) * Q.inv() * tetta), times)

    u[2] = simple((B.T * zero_matrix.T.row_join(fundamental_matrix(times[3], tau).T) * Q.inv() * tetta), times)
    return u


def movement(u):
    """
    Функция вычисления движения по участкам времени.
    :param u: Вектор управления
    :return:
    """
    mov1 = integrate(fundamental_matrix(t, tau) * B * u[0], (tau, 0, t)) + integrate(fundamental_matrix(t, tau) * f,
                                                                                     (tau, 0, t))
    int1 = integrate(fundamental_matrix(t, tau) * B * u[1], (tau, 1, t)) + integrate(
        fundamental_matrix(t, tau) * B * u[0], (tau, 0, 1))
    mov2 = int1 + integrate(fundamental_matrix(t, tau) * f, (tau, 0, t))

    int2 = integrate(fundamental_matrix(t, tau) * B * u[2], (tau, t2_num, t)) + integrate(
        fundamental_matrix(t, tau) * B * u[1], (tau, t1_num, t2_num)) + integrate(fundamental_matrix(t, tau) * B * u[0],
                                                                                  (tau, t0_num, t1_num))
    mov3 = int2 + integrate(fundamental_matrix(t, tau) * f, (tau, 0, t))
    return simple(mov1, times), simple(mov2, times), simple(mov3, times)



def integrate_matrix(Q: Matrix):
    return Matrix([
        [a1(), a2(), b(1, 1), b(0, 1), b(1, 1), b(0, 1)],
        [a2(), a3(), b(1, 0), b(0, 0), b(1, 0), b(0, 0)],
        [b(1, 1), b(1, 0), c(2), c(1), 0, 0],
        [b(0, 1), b(0, 0), c(1), c(0), 0, 0],
        [b(1, 1), b(1, 0), 0, 0, c(2), c(1)],
        [b(0, 1), b(0, 0), 0, 0, c(1), c(0)]
    ])


def a1():
    part_one = integrate(2 * (times[1] - tau) ** 2 + 4 * (times[1] - tau) * (times[2] - tau), integral_range_1)
    part_two = integrate(2 * (times[2] - tau) ** 2, integral_range_2)
    return replace_syms_to_nums(part_one + part_two, times)


def a2():
    part_one = integrate(4 * (times[1] - tau) + 2 * (times[2] - tau), integral_range_1)
    part_two = integrate(2 * (times[2] - tau), integral_range_2)
    return replace_syms_to_nums(part_one + part_two, times)


def a3():
    part_one = integrate(1 + 2 + 1 + 2, integral_range_1)
    part_two = integrate(1 + 1, integral_range_2)
    return replace_syms_to_nums(part_one + part_two, times)


def b(st1, st2):
    part_one = integrate((times[3] - tau) ** st1 * (times[1] - tau) ** st2, integral_range_1)
    part_two = integrate((times[3] - tau) ** st1 * (times[2] - tau) ** st2, integral_range_2)
    return replace_syms_to_nums(part_one + part_two, times)


def c(st):
    return replace_syms_to_nums(integrate((times[3] - tau) ** st, integral_range_3), times)
