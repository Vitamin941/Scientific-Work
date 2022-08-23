from sympy import Matrix, expand, symbols, Symbol
from functions import *
from util_result import Figure, write_to_file

def solve(x0, xT,writer='latex'):
    B = Matrix([
        [0, 0], [1, 0], [0, 0], [0, 1]
    ])
    t = Symbol('t')
    times = [Symbol('t0'), Symbol('t1'), Symbol('t2'), Symbol('T')]
    tau = Symbol('tau')

    F_tau = F_matrix(times, tau)
    F_t0 = F_matrix(times, times[0])

    a = F_tau * B
    b = fundamental_matrix(times[3], tau) * B
    H = a.col_join(b)
    Q = H * H.T

    tetta = find_tetta_vector(F_t0, x0, xT)

    Q_integrated = integrate_matrix(Q)

    u = control(tau, Q_integrated, tetta)
    move = movement(u)
    write_to_file(move)

    figure = Figure(move, u)
    figure.plot_move()

if __name__ == '__main__':
    solve(Matrix([0, 0, 0, 0]), Matrix([3, 2, 2, 1]))
