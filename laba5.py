# Лабораторная работа №5
# Дана функция, f(x) = 1/(1+x*x+y*y), задан интервал [-3; -2] [5,2]
# Найти максимум.

from tkinter import *
from tkinter.scrolledtext import ScrolledText as SCT
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as mpl
import random as ran
import operator
# Матчасть. Алгоритм.
class GenA:
    def __init__(self):
        self.kol_vo = 0
        self.n_gr =[]
        self.v_gr = []
        self.first = []
        self.srt = []
        self.istor_gran =[]
        self.prima =0
        self.fit = []
        self.schet_pokol = 0
        self.sverka = 0
    def main(self, kol_vo, n_gr, v_gr, st1,st2,st3,st4,tx1,tx2,tx3):
        self.kol_vo = int(kol_vo)
        self.n_gr =[float(i) for i in n_gr.split(',')]
        self.v_gr = [float(i) for i in v_gr.split(',')]
        self.istor_gran =[[self.n_gr,self.v_gr]]
        self.first = self.perv_popul()
        self.first_pop = self.first[:-2]
        self.gran = self.first[-2:]
        self.prima = max(self.first_pop[2])
        self.fit = self.fitness(self.first_pop[2],self.prima)
        self.srt = [self.sort(self.first_pop[0],self.fit), self.sort(self.first_pop[1],self.fit),
                    self.sort(self.first_pop[2],self.fit), sorted(self.fit)]
        self.schet_pokol = 1
        self.sverka = 1
        self.st1.delete(1.0, END)
        self.st2.delete(1.0, END)
        self.st3.delete(1.0, END)
        self.st4.delete(1.0, END)
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.st4.insert(1.0, '\n'.join([str(i) for i in self.srt[2]]))
        self.st3.insert(1.0, '\n'.join([str(i) for i in self.srt[3]]))
        self.istor_gran.append(self.gran)
        print("История границ: ",self.istor_gran)
        self.sele = [self.srt[0][0],self.srt[1][0]]
        self.new_gran = self.select(self.istor_gran,self.sele, self.sverka)
        print("Границы после селекции: ", self.new_gran)
        self.istor_gran.append(self.new_gran)
        self.tx1.delete(1.0, END)
        self.tx2.delete(1.0, END)
        self.tx3.delete(1.0, END)
        self.tx1.insert(1.0, str(self.schet_pokol))
        self.tx2.insert(1.0, ' '.join([str(i) for i in self.new_gran[0]]))
        self.tx3.insert(1.0, ' '.join([str(i) for i in self.new_gran[1]]))
        self.gran = self.new_gran

    def func(self):
        uchastn = self.sozdan_uchast(self.gran[0],self.gran[1], self.check)
        spisok_u = uchastn[:-2]
        centrs = uchastn[-2:]
        self.new_pokl = self.evolution(self.gran[0], self.gran[1],spisok_u[0],spisok_u[1], centrs[0], centrs[1])
        self.schet_pokol+=1
        self.sverka+=2
        self.pokl = self.new_pokl[:-2]
        self.gran = self.new_pokl[-2:]
        self.istor_gran.append(self.gran)
        print("История границ: ", self.istor_gran)
        self.prima = max(self.pokl[2])
        self.fit = self.fitness(self.pokl[2],self.prima)
        self.srt = self.srt = [self.sort(self.pokl[0],self.fit), self.sort(self.pokl[1],self.fit),
                    self.sort(self.pokl[2],self.fit), sorted(self.fit)]
        self.tx1.delete(1.0, END)
        self.st1.delete(1.0, END)
        self.st2.delete(1.0, END)
        self.st3.delete(1.0, END)
        self.st4.delete(1.0, END)
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.st4.insert(1.0, '\n'.join([str(i) for i in self.srt[2]]))
        self.st3.insert(1.0, '\n'.join([str(i) for i in self.srt[3]]))
        self.sele = [self.srt[0][0], self.srt[1][0]]
        self.new_gran = self.select(self.istor_gran, self.sele, self.sverka)
        self.istor_gran.append(self.new_gran)
        print("Границы после селекции: ", self.new_gran)
        self.tx1.delete(1.0, END)
        self.tx2.delete(1.0, END)
        self.tx3.delete(1.0, END)
        self.tx1.insert(1.0, str(self.schet_pokol))
        self.tx2.insert(1.0, ' '.join([str(i) for i in self.new_gran[0]]))
        self.tx3.insert(1.0, ' '.join([str(i) for i in self.new_gran[1]]))
        self.gran = self.new_gran


    def new_popula(self,tx4):
        self.check = self.cheking(self.gran[0], self.gran[1])
        print(self.check)
        if self.check!=2:
            self.func()
        else:
            self.tx4.delete(1.0, END)
            ext_x = round((self.gran[1][0]+self.gran[0][0])/2,3)
            ext_y = round((self.gran[1][1]+self.gran[0][1])/2,3)
            self.tx4.insert(1.0, "Максимум функции находится в координатах: "+str(ext_x)+' '+str(ext_y))

    def konec(self, tx4):
        while True:
            self.check = self.cheking(self.gran[0], self.gran[1])
            if self.check!=2:
                self.func()
            else:
                self.tx4.delete(1.0, END)
                ext_x = round((self.gran[1][0] + self.gran[0][0]) / 2, 3)
                ext_y = round((self.gran[1][1] + self.gran[0][1]) / 2, 3)
                self.tx4.insert(1.0, "Максимум функции находится в координатах: "+str(ext_x)+' '+str(ext_y))
                break




    def funcsia(self, chislo_x,chislo_y): # функция подсчета
        return 1/(1+chislo_x**2+chislo_y**2)
    def generac_x(self, granic_n, granic_v): # функция генерации х
        centr0 = round((abs(granic_v-granic_n)/2)+granic_n,3)
        vozm_tochki_u1 = np.arange(granic_n, centr0, 0.001)
        u1_x = ran.choices(vozm_tochki_u1, k=self.kol_vo)
        u1_x = [round(i,3) for i in u1_x]
        vozm_tochki_u2 = np.arange(centr0, granic_v, 0.001)
        u2_x = ran.choices(vozm_tochki_u2, k=self.kol_vo)
        u2_x = [round(i, 3) for i in u2_x]
        return [u1_x,u2_x,centr0]
    def generac_y(self,granic_n, granic_v): # функция генерации у
        centr1 = round((abs(granic_v - granic_n) / 2) + granic_n,3)
        vozm_tochki_u1 = np.arange(granic_n, centr1, 0.001)
        u1_y = ran.choices(vozm_tochki_u1, k=self.kol_vo)
        u1_y = [round(i, 3) for i in u1_y]
        vozm_tochki_u2 = np.arange(centr1, granic_v, 0.001)
        u2_y = ran.choices(vozm_tochki_u2, k=self.kol_vo)
        u2_y = [round(i, 3) for i in u2_y]
        return [u1_y, u2_y, centr1]
    def raschet_z(self, u_x, u_y): # функция подсчёта z
        popul_u1_z = [round(self.funcsia(u_x[0][i], u_y[0][i]), 3) for i in range(self.kol_vo)]
        popul_u2_z = [round(self.funcsia(u_x[1][i], u_y[1][i]), 3) for i in range(self.kol_vo)]
        if max(popul_u1_z) >= max(popul_u2_z):
            granic = 0
            return [u_x[0], u_y[0], popul_u1_z, granic]
        elif max(popul_u1_z) < max(popul_u2_z):
            granic = 1
            return [u_x[1], u_y[1], popul_u2_z, granic]

    def sorevnovanie(self, granic_n, granic_v, spisok_u_x, spisok_u_y, centr0, centr1): # функция, определяющая, которая из участников станет популяцией
        rezult = self.raschet_z(spisok_u_x, spisok_u_y)
        rez_popul = rezult[:-1]
        print("Получившаяся популяция: ", rez_popul)
        proverka = int(rezult[-1:][0])
        if proverka == 0:
            granic_v = [centr0, centr1]
        elif proverka == 1:
            granic_n = [centr0, centr1]
        print("Новые границы: ", [granic_n, granic_v])
        return rez_popul + [granic_n, granic_v]

    def perv_popul(self): # функция генерации первой популяции
        x_c = self.generac_x(self.n_gr[0], self.v_gr[0])
        y_c = self.generac_y(self.n_gr[1], self.v_gr[1])
        perv_popul = self.sorevnovanie(self.n_gr, self.v_gr, x_c[:-1], y_c[:-1], x_c[2], y_c[2])
        return perv_popul

    def fitness(self, popul, prima): # функция расчёта фитнесса
        out_fitness = list(map(lambda x: round(abs((prima - x) / prima), 3), popul))
        return out_fitness

    def sort(self, popul, fitness): # функция сортировки
        a = sorted(zip(popul, fitness), key=operator.itemgetter(1))
        sorti = []
        for i in range(len(a)):
            sorti.append(a[i][0])
        return sorti

    def select(self,spisok_gran, kandidat, nomer): # функция выбора новых границ
        if spisok_gran[nomer][0]==spisok_gran[nomer-1][0]:
            return [kandidat, spisok_gran[nomer][1]]
        elif spisok_gran[nomer][1]==spisok_gran[nomer-1][1]:
            return [spisok_gran[nomer][0], kandidat]

    def cheking(self,granic_n, granic_v): # проверка возможности продолжения поиска
        kon_x = abs(granic_v[0] - granic_n[0])
        kon_y = abs(granic_v[1] - granic_n[1])
        if kon_x <= 0.002 and kon_y <= 0.002:
            otvet_ochka = 2  # параметр, отвечающий за продолжение цикла
        elif kon_x <= 0.002:
            otvet_ochka = 0
        elif kon_y <= 0.002:
            otvet_ochka = 1
        else:
            otvet_ochka = 3
        return otvet_ochka

    def sozdan_uchast(self, granic_n, granic_v, poverka): # активируется после чекинга, создает участников соревнования.
        if poverka==0:
            spisok_u_x = [[round((granic_v[0] + granic_n[0]) / 2, 3)] * self.kol_vo,
                          [round((granic_v[0] + granic_n[0]) / 2, 3)] * self.kol_vo]
            centr0 = round((granic_v[0] + granic_n[0]) / 2, 3)
            spisok_y = self.generac_y(granic_n[1], granic_v[1])
            spisok_u_y = spisok_y[:-1]
            centr1 = spisok_y[-1:][0]
        elif poverka==1:
            spisok_x = self.generac_x(granic_n[0], granic_v[0])
            spisok_u_x = spisok_x[:-1]
            centr0 = spisok_x[-1:][0]
            spisok_u_y = [[round((granic_v[1] + granic_n[1]) / 2, 3)] * self.kol_vo,
                          [round((granic_v[1] + granic_n[1]) / 2, 3)] * self.kol_vo]
            centr1 = round((granic_v[1] + granic_n[1]) / 2, 3)
        else:
            spisok_x = self.generac_x(granic_n[0], granic_v[0])
            spisok_u_x = spisok_x[:-1]
            centr0 = spisok_x[-1:][0]
            spisok_y = self.generac_y(granic_n[1], granic_v[1])
            spisok_u_y = spisok_y[:-1]
            centr1 = spisok_y[-1:][0]
        return [spisok_u_x, spisok_u_y, centr0, centr1]



    def evolution(self, granic_n, granic_v, spisok_u_x, spisok_u_y, centr0, centr1): # функция эволюции
        evol = self.sorevnovanie(granic_n, granic_v, spisok_u_x, spisok_u_y, centr0, centr1)
        return evol


class Forma(GenA):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title("Лабораторная работа №5")
        self.l1 = Label(self.root, text='Задана функция f(x,y) = 1/(1+x*x+y*y)' + '\n'
                                        + '\n' + 'Найти максимум функции.')
        self.l2 = Label(self.root, text='Введите нижнюю границу: ')
        self.l11 = Label(self.root, text='Введите верхнюю границу: ')
        self.l3 = Label(self.root, text='Значение х')
        self.l4 = Label(self.root, text='Значение у')
        self.l5 = Label(self.root, text='Фитнесс')
        self.l6 = Label(self.root, text='Введите желаемое количество особей: ')
        self.l7 = Label(self.root, text='Решение: ')
        self.l8 = Label(self.root, text='Номер поколения: ')
        self.l9 = Label(self.root, text='Новая нижняя граница: ')
        self.l10 = Label(self.root, text='Значение f(x,y)')
        self.l12 = Label(self.root, text='Новая верхняя граница: ')

        self.b1 = Button(self.root, text='Построить график функции', command=self.stroim_lico)
        self.b2 = Button(self.root, text='Получить первую\nпопуляцию', width=13, height=2,
                         command=self.perv_pokol)
        self.b3 = Button(self.root, text='Следующая\nпопуляция', width=10, height=2, command = self.next_pokol)
        self.b4 = Button(self.root, text='Циклический\nпоиск', width=11, height=2, command = self.okonc)

        self.st1 = SCT(self.root, width=10, height=15)
        self.st2 = SCT(self.root, width=10, height=15)
        self.st3 = SCT(self.root, width=10, height=15)
        self.st4 = SCT(self.root, width=10, height=15)
        self.tx1 = Text(self.root, width=5, height=1)
        self.tx2 = Text(self.root, width=15, height=1)
        self.tx3 = Text(self.root, width=15, height=1)
        self.tx4 = Text(self.root, width=60, height=1)

        self.e1 = Entry(self.root, width=10)
        self.e2 = Entry(self.root, width=15)
        self.e3 = Entry(self.root, width=15)

        self.l1.place(x=20, y=10)
        self.l2.place(x=10, y=160)
        self.l3.place(x=320, y=10)
        self.l4.place(x=420, y=10)
        self.l5.place(x=620, y=10)
        self.l6.place(x=10, y=120)
        self.l7.place(x=10, y=380)
        self.l8.place(x=10, y=250)
        self.l9.place(x=10, y=300)
        self.l10.place(x=520, y=10)
        self.l11.place(x=10, y=200)
        self.l12.place(x=10, y=340)

        self.e1.place(x=250, y=120)
        self.e2.place(x=200, y=160)
        self.e3.place(x=200, y=200)

        self.b1.place(x=40, y=80)
        self.b2.place(x=320, y=300)
        self.b3.place(x=435, y=300)
        self.b4.place(x=520, y=300)

        self.st1.place(x=320, y=40)
        self.st2.place(x=420, y=40)
        self.st3.place(x=620, y=40)
        self.st4.place(x=520, y=40)
        self.tx1.place(x=160, y=250)
        self.tx2.place(x=150, y=300)
        self.tx3.place(x=150, y=340)
        self.tx4.place(x=70, y=380)

        self.root.mainloop()
    def stroim_lico(self):
        f = lambda x, y: 1/(1+x*x+y*y)
        fig = mpl.figure(figsize=(10,10))
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        xval = np.linspace(-3, 5, 100)
        yval = np.linspace(-3, 5, 100)
        x, y = np.meshgrid(xval, yval)
        f_xy = f(x, y)
        ax.plot_surface(x, y, f_xy, rstride = 10, cstride = 10, cmap = cm.plasma)
        mpl.show()
    def perv_pokol(self):
        self.main(self.e1.get(), self.e2.get(), self.e3.get(), self.st1, self.st2, self.st3, self.st4,
                  self.tx1,self.tx2, self.tx3)
    def next_pokol(self):
        self.new_popula(self.tx4)

    def okonc(self):
        self.konec(self.tx4)


if __name__ == '__main__':
    a= Forma()
