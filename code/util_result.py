import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import datetime
from sympy import *
from functions import t0_num, t1_num, t2_num, T_num

x,y,t = symbols('x y t')
STEP = 0.002
current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
result_path = os.path.join(current_path, 'out')


def write_to_file(move,writer='latex'):
    if not os.path.exists(result_path):
        print('Папка для хранения результатов создана')
        os.mkdir(result_path)
    
    with open(os.path.join(result_path, f'result-{writer}-{datetime.datetime.now().date()}.txt'), 'w') as f:
        if writer == 'latex':
            f.write(latex(move))
        elif writer == 'txt':
            for vector in move:
                f.write(str(vector) + '\n')
        else:
            print('Output type isn\'t latex and isn\'t txt')

class Figure():
    def __init__(self, move, control):
        self.times = (t0_num, t1_num, t2_num, T_num)
        self.move = move
        self.control = control
        self.x_func = []
        self.y_func = []
        for relay in range(len(move)):
            self.x_func.append(lambdify(t,move[relay][0]))
            self.y_func.append(lambdify(t,move[relay][2]))

    def plot_move(self):
        x_points = []
        y_points = []

        plt.xlabel('x1(t)')
        plt.ylabel('x3(t)')
        plt.title('Уравнение движения')

        for relay in range(len(self.move)):
            x_points.append([self.x_func[relay](t) for t in np.arange(self.times[relay],self.times[relay + 1],STEP)])
            y_points.append([self.y_func[relay](t) for t in np.arange(self.times[relay],self.times[relay + 1],STEP)])

        for x,y in zip(x_points, y_points):
            plt.plot(x,y,'b')

        xticks = []
        yticks = []

        for xfunc, yfunc, time in zip(self.x_func, self.y_func, range(len(self.times) - 2)):
            xticks.append(xfunc(self.times[time + 1]))
            yticks.append(yfunc(self.times[time + 1]))
        plt.plot(xticks, yticks,'ro')

        plt.grid()
        plt.show()

    