# Лабораторная работа №2
# Поиск корней диофантового уравнения.
# Задано уравнение a+2b+3c+4d = 30. Найти a,b,c,d.
from tkinter import *
from tkinter.scrolledtext import ScrolledText as SCT
import random as ran
import numpy as np
import numpy.random as npr
import operator

class GenA:
    def __init__(self):
        self.koeffs = []
        self.equal = 0
        self.kol_vo = 0
        self.ch_mut = 0
        self.razm_stag = 0
        self.catacl = 0
        self.fit = []
        self.srt=[]
        self.schet_pokol =0
        self.istor_fit = []
        self.sverka = 0
    def main(self, kol_vo, ch_mut, razm_stag, catacl, st1, st2,tx1):
        self.koeffs = [1, 2, 3, 4]
        self.equal = 30
        self.istor_fit = []
        self.kol_vo = int(kol_vo)
        self.ch_mut = int(ch_mut)
        self.razm_stag = int(razm_stag)
        self.catacl = int(catacl)
        self.first = self.perv_popul()
        print('Первая популяция: ',self.first)
        self.schet_pokol=1
        self.summs = self.summ(self.first)
        print('Расстояния от 30: ',self.summs)
        self.fit = self.fitness(self.summs)
        print('Фитнесс значений: ',self.fit)
        self.srt = self.sort(self.first, self.fit)
        self.istor_fit.append(self.srt[1][0])
        st1.delete(1.0, END)
        st2.delete(1.0, END)
        tx1.delete(1.0, END)
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.tx1.insert(1.0, str(self.schet_pokol))
        self.pokol = self.evoluc(self.first,self.fit)



    def perv_popul(self):
        out=[(ran.sample(range(1,self.equal), k=len(self.koeffs))) for i in range(self.kol_vo)]
        return out
    def func(self):
        self.schet_pokol += 1
        self.check = self.summ(self.pokol)
        self.fit = self.fitness(self.check)
        self.srt = self.sort(self.pokol, self.fit)
        self.istor_fit.append(self.srt[1][0])
        self.st1.delete(1.0, END)
        self.st2.delete(1.0, END)
        self.tx1.delete(1.0, END)
        self.st1.insert(1.0, '\n'.join([str(i) for i in self.srt[0]]))
        self.st2.insert(1.0, '\n'.join([str(i) for i in self.srt[1]]))
        self.tx1.insert(1.0, str(self.schet_pokol))
        if self.schet_pokol%self.ch_mut==0:
            r_ind = ran.randint(0, len(self.pokol)-1)
            self.pokol[r_ind] = self.mutac(self.pokol[r_ind])
        if self.schet_pokol>self.razm_stag:
            niz=self.schet_pokol-self.razm_stag
            promej = self.istor_fit[niz:]
            check = promej[-1]
            if promej.count(check)>=self.razm_stag-1:
                self.pokol = self.stagn(self.pokol)
        if self.schet_pokol%self.catacl==0:
            self.pokol = self.cataclizm()
        self.new_pokol = self.evoluc(self.pokol, self.fit)
        self.pokol = self.new_pokol
        if self.schet_pokol%100==0:
            print(self.check)
            print(self.fit)
            print(self.pokol)



    def konec(self, tx2):
        while True:
            check = self.summ(self.pokol)
            if min(check)==0:
                final_ind = check.index(int(0))
                solve = self.pokol[final_ind]
                tx2.delete(1.0, END)
                tx2.insert(1.0, ' '.join(str(solve)))
                break
            else:
                self.func()




    def new_popul(self,tx2):
        check = self.summ(self.pokol)
        if min(check)==0:
            final_ind = check.index(int(0))
            solve = self.pokol[final_ind]
            tx2.delete(1.0, END)
            tx2.insert(1.0, ' '.join(str(solve)))
        else:
            self.func()



    def summ(self, popul):
        out_s = [np.dot(i,self.koeffs) for i in popul]
        out = [int(abs(i-self.equal)) for i in out_s]
        return out
    def fitness(self,summs):
        print(summs)
        out_s =[float(i)**(-1) for i in summs]
        prom_s = sum(out_s)
        out_f =[round(100*(i/prom_s),2) for i in out_s]
        return out_f
    def sort(self, popul, fitness):
        spis = zip(popul,fitness)
        srt_f = sorted(spis, key=operator.itemgetter(1), reverse= True)
        srt=[]
        for i in range(len(srt_f)):
            srt.append(srt_f[i][0])
        fitness = sorted(fitness, reverse=True)
        return [srt, fitness]
    def ruletka (self, popul, fitness):
        out = ran.choices(popul, weights=fitness, k=self.kol_vo)
        return out
    def crossing(self, parent1,parent2):
        tochka = ran.randint(1, len(parent1))
        child0 = parent1[:tochka]+parent2[tochka:]
        child1 = parent2[:tochka]+parent1[tochka:]
        children = [child0, child1]
        prigs = self.summ(children)
        a = prigs.index(min(prigs))
        return children[a]
    def select(self, parents, fit_p, children, fit_chil):
        full_parents = list(zip(parents, fit_p))
        full_child = list(zip(children, fit_chil))
        full = full_parents+full_child
        pops = sorted(full, key=operator.itemgetter(1), reverse=True)
        out = pops[:self.kol_vo]
        return out
    def mutac(self,osob):
        r_ind = ran.randint(0,len(osob)-1)
        r_ch = ran.randint(1,self.equal)
        osob[r_ind] = r_ch
        return osob

    def evoluc(self, popul,fitness):
        pul_otcov = self.ruletka(popul, fitness)
        pul_mater = self.ruletka(popul, fitness)
        childs = [self.crossing(pul_otcov[i], pul_mater[i]) for i in range(self.kol_vo)]
        self.check = self.summ(childs)
        if min(self.check)==0:
            return childs
        else:
            fitn_ch = self.fitness(self.check)
            next_pok = self.select(popul,fitness,childs,fitn_ch)
            next_pokol = []
            for i in range(len(next_pok)):
                next_pokol.append(next_pok[i][0])
            return next_pokol
    def stagn(self, popul):
        r_ind = ran.randint(0,len(popul)-1)
        popul[r_ind]=ran.sample(range(1, self.equal), k=len(self.koeffs))
        return popul

    def cataclizm(self):
        out_popul = []
        for i in range(self.kol_vo):
            out_popul.append([ran.randint(1, self.equal // self.koeffs[j]) for j in range(len(self.koeffs))])
        return out_popul





class Forma(GenA):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x520')
        self.root.title("Лабораторная работа №2")
        self.l1 = Label(self.root, text='Задано уравнение a+2b+3c+4d = 30.' + '\n' + 'Найти a,b,c,d.')
        self.l2 = Label(self.root, text='Введите количество особей: ')
        # self.l11 = Label(self.root, text='Введите верхнюю границу: ')
        self.l3 = Label(self.root, text='Введите частоту мутации: ')
        self.l4 = Label(self.root, text='Введите размер стагнации: ')
        self.l5 = Label(self.root, text='Введите число поколения для катаклизма: ')
        self.l6 = Label(self.root, text='Популяция')
        self.l7 = Label(self.root, text='Фитнесс')
        self.l8 = Label(self.root, text='Поколение №: ')
        self.l9 = Label(self.root, text='Решение: ')


        self.b1 = Button(self.root, text='Получить первую\nпопуляцию', width=15, height=2, command = self.first_pokol)
        self.b2 = Button(self.root, text='Следующая\nпопуляция', width=15, height=2, command = self.next_pokol)
        self.b3 = Button(self.root, text='Циклический\nпоиск', width=15, height=2, command = self.okonch)
        #
        self.st1 = SCT(self.root, width=15, height=15)
        self.st2 = SCT(self.root, width=12, height=15)
        self.tx1 = Text(self.root, width=5, height=1)
        self.tx2 = Text(self.root, width=40, height=1)
        #
        self.e1 = Entry(self.root, width=10)
        self.e2 = Entry(self.root, width=10)
        self.e3 = Entry(self.root, width=10)
        self.e4 = Entry(self.root, width=10)
        #
        self.l1.place(x=100, y=10)
        self.l2.place(x=10, y=50)
        self.l3.place(x=10, y=80)
        self.l4.place(x=10, y=110)
        self.l5.place(x=10, y=140)
        self.l6.place(x=30, y=180)
        self.l7.place(x=150, y=180)
        self.l8.place(x=10, y=450)
        self.l9.place(x=10, y=480)

        self.e1.place(x=180, y=50)
        self.e2.place(x=180, y=80)
        self.e3.place(x=180, y=110)
        self.e4.place(x=250, y=140)
        #
        self.b1.place(x=270, y=200)
        self.b2.place(x=270, y=300)
        self.b3.place(x=270, y=400)
        #
        self.st1.place(x=20, y=200)
        self.st2.place(x=150, y=200)
        self.tx1.place(x=100, y=450)
        self.tx2.place(x=70, y=480)


        self.root.mainloop()

    def first_pokol(self):
        self.main(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),self.st1, self.st2, self.tx1)
    def next_pokol(self):
        self.new_popul(self.tx2)
    def okonch(self):
        self.konec(self.tx2)

if __name__ == '__main__':
    a = Forma()