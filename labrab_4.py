# Лабораторная работа №4
# Дана функция, f(x) = 24+2x-7x^2+2x^3, задан интервал [-3; 5]
# Найти минимум и максимум.

from tkinter import *
from tkinter.scrolledtext import ScrolledText as SCT
import numpy as np
import matplotlib.pyplot as mpl
import random
import operator
# Матчасть, алгоритм
class Gen_A:
    def __init__(self):
        self.vozm_tochki = []
        self.choice = 2
        self.kol_vo = 0
        self.srt = [' ']
    def main(self, kol_vo_osob, choice, st1, st2, st3, tx1, tx2):
        self.n_gr = -3
        self.v_gr = 5
        self.koeffs = [2, -7, 2, 24]
        self.stepeni = [3, 2, 1, 0]
        self.kol_vo = int(kol_vo_osob)
        self.choice = int(choice)
        self.schet_pokol = 1
        st1.delete(1.0, END)
        st2.delete(1.0, END)
        st3.delete(1.0, END)
        tx1.delete(1.0, END)
        tx2.delete(1.0, END)
        self.vozm_tochki = list(np.arange(self.n_gr, self.v_gr, 0.01))
        self.vozm_tochki = list(map(lambda x: round(x, 2), self.vozm_tochki))
        self.pokol = self.perv_popul()
        if self.choice==1:
            self.prima = max(self.pokol[1])
        elif self.choice==0:
            self.prima = min(self.pokol[1])
        self.fit = self.fitness(self.pokol[1], self.prima)
        self.sele = [[self.n_gr, np.dot(self.koeffs, self.stepeny(self.n_gr))],
        [self.v_gr, np.dot(self.koeffs, self.stepeny(self.v_gr))]]
        self.srt = [self.sort(self.pokol[0], self.fit), self.sort(self.pokol[1], self.fit), sorted(self.fit)]
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.st3.insert(1.0, '\n'.join([str(i) for i in self.srt[2]]))
        self.tx1.insert(1.0, str(self.schet_pokol))
        self.tx2.insert(1.0, ' '.join(str(i) for i in self.sele))
    def konec(self, tx3):
        if self.choice==1:
            while max(self.pokol[0])<self.v_gr:
                self.func()
        if self.choice==0:
            while min(self.pokol[0])>self.n_gr:
                self.func()
        self.func()
        if self.choice == 0:
            tx3.delete(1.0, END)
            self.tx3.insert(1.0, 'Локальный минимум: ' + str([self.srt[0][0], self.srt[1][0]]))
        elif self.choice == 1:
            tx3.delete(1.0, END)
            self.tx3.insert(1.0, 'Локальный максимум: ' + str([self.srt[0][0], self.srt[1][0]]))
    def new_popula(self, tx3):
        if self.choice==0:
            if self.n_gr not in self.pokol[0]:
                self.func()
            elif self.n_gr in self.pokol[0]:
                tx3.delete(1.0,END)
                self.tx3.insert(1.0, 'Локальный минимум: ' + str([self.srt[0][0], self.srt[1][0]]))
        if self.choice==1:
            if self.v_gr not in self.pokol[0]:
                self.func()
            elif self.n_gr in self.pokol[0]:
                tx3.delete(1.0,END)
                self.tx3.insert(1.0, 'Локальный максимум: '+ str([self.srt[0][0],self.srt[1][0]]))

    def func(self):
        self.schet_pokol+=1
        self.next_pokol = self.evolution(self.sele[0][0], self.sele[1][0])
        self.pokol = self.next_pokol
        if self.choice==1:
            self.prima = max(self.pokol[1])
        elif self.choice==0:
            self.prima = min(self.pokol[1])
        fit = self.fitness(self.pokol[1], self.prima)
        self.srt = [self.sort(self.pokol[0], fit), self.sort(self.pokol[1], fit), sorted(fit)]
        self.sele = self.selection(self.sele[0], self.sele[1],[self.srt[0][0],self.srt[1][0]])
        self.st1.delete(1.0, END)
        self.st2.delete(1.0, END)
        self.st3.delete(1.0, END)
        self.tx1.delete(1.0, END)
        self.tx2.delete(1.0, END)
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.st3.insert(1.0, '\n'.join([str(i) for i in self.srt[2]]))
        self.tx1.insert(1.0, str(self.schet_pokol))
        self.tx2.insert(1.0, ' '.join(str(i) for i in self.sele))


    def stepeny(self, chislo):
        return list(map(lambda x: chislo ** x, self.stepeni))
    def perv_popul(self):
        out_popul_x = list(random.choices(self.vozm_tochki, k=self.kol_vo))
        out_popul_y = list(map(lambda x: round(sum(list(np.dot(self.koeffs, x))), 2), out_popul_x))
        out_popul = [out_popul_x, out_popul_y]
        return out_popul
    def fitness(self, popul, prima):
        out_fitness = list(map(lambda x: round(100*(abs((prima-x)/prima)),2), popul))
        return out_fitness
    def sort (self, popul,fitness):
        a = sorted(zip(popul, fitness), key=operator.itemgetter(1))
        sorti = []
        for i in range(len(a)):
            sorti.append(a[i][0])
        return sorti

    def selection(self, granic_n, granic_v, parent):
        if self.choice == 0:
            if granic_n[1] >= parent[1]:
                granic_n = parent
            else:
                granic_v = parent
        elif self.choice == 1:
            if granic_v[1] <= parent[1]:
                granic_v = parent
            else:
                granic_n = parent
        out = [granic_n, granic_v]
        return out

    def evolution(self, granic_n, granic_v):
        vozm_tochki_x = list(np.arange(granic_n, granic_v, 0.001))
        vozm_tochki_x_vyb = random.choices(vozm_tochki_x, k=self.kol_vo)
        new_popul_x = list(map(lambda x: round(x, 3), vozm_tochki_x_vyb))
        stepeni_x = list(map(lambda x: self.stepeny(x), new_popul_x))
        new_popul_y_1 = list(map(lambda x: np.dot(self.koeffs, x), stepeni_x))
        new_popul_y = [round(float(i), 3) for i in new_popul_y_1]
        return [new_popul_x, new_popul_y]

# Создание формы.
class Forma(Gen_A):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('610x500')
        self.root.title("Лабораторная работа №4")
        self.l1 = Label(self.root, text = 'Задана функция f(x) = 24+2x-7x^2+2x^3'+'\n'+'Задан интервал [-3; 5]'
                                          +'\n'+'Найти минимум и максимум функции.')
        self.l2 = Label(self.root, text = 'Выберите, что ищем: ')
        self.l3 = Label(self.root, text = 'Значение х')
        self.l4 = Label(self.root, text = 'Значение у')
        self.l5 = Label(self.root, text = 'Фитнесс')
        self.l6 = Label(self.root, text = 'Введите желаемое количество особей: ')
        self.l7 = Label(self.root, text = 'Решение: ')
        self.l8 = Label(self.root, text = 'Номер поколения: ')
        self.l9 = Label(self.root, text = 'Нижняя и верхняя границы: ')

        self.b1 = Button(self.root, text = 'Построить график функции', command = self.stroim_lico)
        self.b2 = Button(self.root, text = 'Получить первую\nпопуляцию', width = 13, height = 2, command=self.first_population )
        self.b3 = Button(self.root, text = 'Следующая\nпопуляция', width = 10, height = 2, command=self.new_pokolenie )
        self.b4 = Button(self.root, text = 'Циклический\nпоиск', width = 11, height = 2, command=self.do_konca )

        self.choice = IntVar(value=2)
        self.r1 = Radiobutton(self.root, text = 'min', variable = self.choice, value = int(0))
        self.r2 = Radiobutton(self.root, text = 'max', variable = self.choice, value = int(1))

        self.st1 = SCT(self.root, width =10, height = 15)
        self.st2 = SCT(self.root, width =10, height = 15)
        self.st3 = SCT(self.root, width =10, height = 15)
        self.tx1 = Text(self.root, width=5, height = 1)
        self.tx2 = Text(self.root, width=33, height = 1)
        self.tx3 = Text(self.root, width=60, height = 1)

        self.e1 = Entry(self.root, width = 10)

        self.l1.place(x=20, y=10)
        self.l2.place(x=20, y=120)
        self.l3.place(x=320, y=10)
        self.l4.place(x=420, y=10)
        self.l5.place(x=520, y=10)
        self.l6.place(x=10, y=150)
        self.l7.place(x=10, y=350)
        self.l8.place(x=10, y=190)
        self.l9.place(x=10, y=220)

        self.e1.place(x=250, y=150)

        self.b1.place(x=40, y=80)
        self.b2.place(x=320, y=300)
        self.b3.place(x=435, y=300)
        self.b4.place(x=520, y=300)

        self.r1.place(x=150, y=120)
        self.r2.place(x=200, y=120)

        self.st1.place(x=320, y=40)
        self.st2.place(x=420, y=40)
        self.st3.place(x=520, y=40)
        self.tx1.place(x=160, y=190)
        self.tx2.place(x=20, y=240)
        self.tx3.place(x=70, y=350)

        self.root.mainloop()
    def stroim_lico(self):
        f = lambda x: 2*x**3-7*x**2+2*x+24
        mpl.subplots()
        x = np.linspace(-3, 5, 100)
        mpl.plot(x, f(x))
        mpl.show()
    def first_population(self):
        self.main(self.e1.get(), self.choice.get(), self.st1, self.st2, self.st3, self.tx1, self.tx2)

    def new_pokolenie(self):
        self.new_popula(self.tx3)

    def do_konca(self):
        self.konec(self.tx3)

if __name__ == '__main__':
    a= Forma()