import numpy as np
import random as rd
from presets import *
from targets import *
from letters_enum import *
import matplotlib.pyplot as plt

class Madalaine:


    def __init__(self, learn_rate, option_data):

        self.learn_rate = float(learn_rate)
        self.threshold = 0.0
        self.condition = option_data[0]
        self.stop_value = [float(x) for x in option_data[1]]
        self.v = []
        self.v0 = []

    def training(self):

        entries= []

        for i in range(1, 4):
            for var in ["A", "B", "C", "D", "E", "J", "K"]:
                array = np.array(globals()[f"get_{var}{i}"]()).flatten()
                entries.append(array)

        (n_patterns, n_entries) = np.shape(entries)

        targets = get_targets()

        (n_outs, n_targets) = np.shape(targets)


        self.v = np.zeros((n_entries, n_outs))

        for i in range(n_entries):
            for j in range(n_outs):
                self.v[i][j] = rd.uniform(-0.5, 0.5)

        self.v0 = np.zeros((n_outs))

        for j in range(n_outs):
                self.v0[j] = rd.uniform(-0.5, 0.5)

        yin = np.zeros((n_outs, 1))
        y = np.zeros((n_outs, 1))

        error = 1.0
        cicle = 0

        cicles = []
        errors = []

        plt.ion()
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.canvas.manager.set_window_title("Gráfico de Treinamento")

        while (self.condition == "Erro Tolerado" and error >= self.stop_value) or (self.condition == "Número de Ciclos" and cicle < self.stop_value):
            cicle = cicle + 1
            error = 0.0
            k = 0

            for i in range(n_patterns):
                letter = np.array(entries)[i, :]
                for m in range(n_outs):
                    sum_value = 0
                    for n in range(n_entries):
                        sum_value = sum_value + letter[n] * self.v[n][m]

                    yin[m] = sum_value + self.v0[m]

                for j in range(n_outs):
                    if yin[j] >= self.threshold:
                        y[j] = 1
                    else:
                        y[j] = 0

                if k > 6:
                    k = 0


                for j in range(n_outs):
                    error = error + 0.5*((targets[k][j]-y[j])**2)

                last_v = self.v

                for m in range(n_entries):
                    for n in range(n_outs):
                        self.v[m][n] = last_v[m][n] + self.learn_rate * (targets[n][k] - y[n]) * letter[m]


                last_v0 = self.v0

                for j in range(n_outs):
                    self.v0[j] = last_v0[j] + self.learn_rate*(targets[j][k]-y[j])

                k = k + 1

            print(cicle)
            print(error)
            cicles.append(cicle)
            errors.append(error)
                
            ax.cla()
            ax.plot(cicles, errors, marker="o")
            ax.set_title(f"Ciclo: {cicle}, Erro: {float(error):.4f}")
            ax.set_xlabel("Ciclos")
            ax.set_ylabel("Erro")
            plt.draw()
            plt.pause(0.1)

        plt.ioff()
        plt.show()

    def model(self, letter):

        entry = np.array(letter).flatten()

        entries = entry.size

        targets = get_targets()

        (n_outs, n_targets) = np.shape(targets)

        yin = np.zeros((n_outs, 1))
        y = np.zeros((n_outs, 1))

        for j in range(n_outs):
            sum_value = 0
            for i in range(entries):
                sum_value = sum_value + entry[i]*self.v[i][j]

            yin[j] = sum_value + self.v0[j]

        for j in range(n_outs):
            if yin[j] >= self.threshold:
                y[j] = 1
            else:
                y[j] = 0
        
        value = tuple(np.array(y).flatten().astype(int))
        enum = Letter(value)
        
        return enum.name


    def set_condition(self, condition):
        self.condition = condition

    def set_stop_value(self, value):
        self.stop_value = float(value)

    def set_learn_rate(self, lr):
        self.learn_rate = float(lr)    
