from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from functions import t0_num, t1_num, t2_num, T_num

x,y,t = symbols('x y t')
STEP = 0.002

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

        for relay in range(len(self.move)):
            x_points.append([self.x_func[relay](t) for t in np.arange(self.times[relay],self.times[relay + 1],STEP)])
            y_points.append([self.y_func[relay](t) for t in np.arange(self.times[relay],self.times[relay + 1],STEP)])

        for x,y in zip(x_points, y_points):
            plt.plot(x,y,'b')

        xticks = []
        yticks = []

        for xfunc, yfunc, time in zip(self.x_func, self.y_func, range(len(self.times))):
            xticks.append(xfunc(self.times[time + 1]))
            yticks.append(yfunc(self.times[time + 1]))
        plt.xticks(xticks)
        plt.yticks(yticks)
        
        plt.plot(xticks, yticks,'ro')

        plt.grid()
        plt.show()

    