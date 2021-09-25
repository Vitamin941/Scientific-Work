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
		[q11(), q12(), q13(), q14(), q15(), q16()],
		[q21(), q22(), q23(), q24(), q25(), q26()],
		[q31(), q32(), q33(), q34(), q35(), q36()],
		[q41(), q42(), q43(), q44(), q45(), q46()],
		[q51(), q52(), q53(), q54(), q55(), q56()],
		[q61(), q62(), q63(), q64(), q65(), q66()]
	])

def replace_syms_to_nums(expression):
    return expression.replace(t0, t0_num)\
        .replace(t1, t1_num)\
        .replace(t2, t2_num)\
        .replace(T, T_num)


def q11():
	part_one = integrate(2 * (t1 - tau) ** 2 + 4 * (t1 - tau) * (t2 - tau), integral_range_1)
	part_two = integrate(2 * (t2 - tau) ** 2, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q12():
	part_one = integrate(4 * (t1 - tau) + 2 * (t2 - tau), integral_range_1)
	part_two = integrate(2 * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)	

def q13():
	part_one = integrate((T - tau) * (t1 - tau), integral_range_1)
	part_two = integrate((T - tau) * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)	


def q14():
	part_one = integrate((t1 - tau), integral_range_1)
	part_two = integrate((t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q15():
	part_one = integrate((T - tau) * (t1 - tau), integral_range_1)
	part_two = integrate((T - tau) * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q16():
	part_one = integrate((t1 - tau), integral_range_1)
	part_two = integrate((t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q21():
	part_one = integrate(4 * (t1 - tau) + 2 * (t2 - tau), integral_range_1)
	part_two = integrate(2 * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q22():
	part_one = integrate(1 + 2 + 1 + 2, integral_range_1)
	part_two = integrate(1 + 1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q23():
	part_one = integrate((T - tau), integral_range_1)
	part_two = integrate((T - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q24():
	part_one = integrate(1, integral_range_1)
	part_two = integrate(1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q25():
	part_one = integrate((T - tau), integral_range_1)
	part_two = integrate((T - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q26():
	part_one = integrate(1, integral_range_1)
	part_two = integrate(1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q31():
	part_one = integrate((T - tau) * (t1 - tau), integral_range_1)
	part_two = integrate((T - tau) * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q32():
	part_one = integrate((T - tau), integral_range_1)
	part_two = integrate((T - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q33():
	return replace_syms_to_nums(integrate((T - tau)** 2,integral_range_3))

def q34():
	return replace_syms_to_nums(integrate(T - tau,integral_range_3))

def q35():
	return 0

def q36():
	return 0

def q41():
	part_one = integrate(t1 - tau, integral_range_1)
	part_two = integrate(t2 - tau, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q42():
	part_one = integrate(1, integral_range_1)
	part_two = integrate(1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q43():
	return replace_syms_to_nums(integrate(T - tau,integral_range_3))

def q44():
	return replace_syms_to_nums(integrate(1, integral_range_3))

def q45():
	return 0

def q46():
	return 0

def q51():
	part_one = integrate((T - tau) * (t1 - tau), integral_range_1)
	part_two = integrate((T - tau) * (t2 - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q52():
	part_one = integrate((T - tau), integral_range_1)
	part_two = integrate((T - tau), integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q53():
	return 0

def q54():
 	return 0

def q55():
	return replace_syms_to_nums(integrate((T - tau)** 2,integral_range_3))

def q56():
	return replace_syms_to_nums(integrate(T - tau,integral_range_3))

def q61():
	part_one = integrate(t1 - tau,integral_range_1)
	part_two = integrate(t2 - tau, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q62():
	part_one = integrate(1, integral_range_1)
	part_two = integrate(1, integral_range_2)
	return replace_syms_to_nums(part_one + part_two)

def q63():
	return 0

def q64():
	return 0

def q65():
	return replace_syms_to_nums(integrate(T - tau,integral_range_3))

def q66():
	return replace_syms_to_nums(integrate(1 ,integral_range_3))



if __name__ == '__main__':
	sp.pprint(integrate_matrix())
