# WARNING ----------------------------------------------------------------------
# Don't check this code! It's terrible

import sympy as sp
from sympy import integrate, Matrix
from static import *

integral_range_1 = (tau, t0_num, t1_num)
integral_range_2 = (tau, t0_num, t2_num)
integral_range_3 = (tau, t0_num, T_num)

def integrate_matrix():
	return Matrix([
		[a1(), a2(), b(1, 1), b(0, 1), b(1, 1), b(0, 1)],
		[a2(), a3(), b(1, 0), b(0, 0), b(1, 0), b(0, 0)],
		[b(1, 1), b(1, 0), c(2), c(1), 0   , 0   ],
		[b(0, 1), b(0, 0), c(1), c(0), 0   , 0   ],
		[b(1, 1), b(1, 0), 0   , 0   , c(2), c(1)],
		[b(0, 1), b(0, 0), 0   , 0   , c(1), c(0)]
	])

def a1():
	part_one = integrate(2 * (time_moments.get("t1") - tau) ** 2 + 4 * (time_moments.get("t1") - tau) * (time_moments.get("t2") - tau), integral_range_1)
	part_two = integrate(2 * (time_moments.get("t2") - tau) ** 2, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def a2():
	part_one = integrate(4 * (time_moments.get("t1") - tau) + 2 * (time_moments.get("t2") - tau), integral_range_1)
	part_two = integrate(2 * (time_moments.get("t2") - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)	

def a3():
	part_one = integrate(1 + 2 + 1 + 2, integral_range_1)
	part_two = integrate(1 + 1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)



def b(st1, st2):
	part_one = integrate((time_moments.get("T") - tau)**st1 * (time_moments.get("t1") - tau)**st2, integral_range_1)
	part_two = integrate((time_moments.get("T") - tau)**st1 * (time_moments.get("t2") - tau)**st2, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)	



def c(st):
	return replace_syms_to_nums(integrate((time_moments.get("T") - tau)** st,integral_range_3))

if __name__ == '__main__':
	sp.pprint(integrate_matrix())
