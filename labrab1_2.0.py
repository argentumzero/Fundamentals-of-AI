from tkinter import *
import random as ran
import operator


class gen_a:
    def __init__(self):
        self.ish_slovo = ''
        self.alfavit = ''
        self.kol_osoby = ''
        self.chast_mut = ''
        self.first_popul = ''
        self.pokol = ''
        self.schet_pokol = 0
        self.str = [' ']
        self.text = ''

    def main(self, alfavit, ish_slovo, kol_osoby, chast_mut, text):
        self.ish_slovo = ish_slovo
        self.alfavit = alfavit
        self.kol_osoby = int(kol_osoby)
        self.chast_mut = int(chast_mut)
        self.pokol = self.perv_pokolenie()
        text.delete(1.0, END)
        text.insert(1.0, str(self.pokol) + '\n')
        self.first_popul = self.pokol
        self.schet_pokol = 1
        self.srt = [' ']
        self.text = text

    def all_pokol(self):
        while self.srt.count(self.ish_slovo) <= 3:
            self.func()
        self.func()

    def func(self):
        fit = self.cikl_proverki(self.pokol)
        self.srt = self.sort(fit, self.pokol)
        next_pokol = self.evolution(self.srt)
        mutac = ''
        if self.schet_pokol % self.chast_mut == 0:
            i = ran.choice(range(0, len(next_pokol)))
            mutac = self.mutate(next_pokol[i])
            next_pokol[i] = mutac
        self.text.insert(1.0, 'Фитнесс: ' + str(sorted(fit)[::-1]) + '\n')
        self.text.insert(1.0, 'Отсортированные значения: ' + ' '.join(self.srt) + '\n')
        self.text.insert(1.0, 'Новое поколение: ' + ' '.join(next_pokol) + "; номер поколения: " + str(
            self.schet_pokol) + '\n')
        self.text.insert(1.0, '\n')
        self.schet_pokol += 1
        self.pokol = next_pokol

    def new_popul(self):
        if self.ish_slovo not in self.srt:
            self.func()

    # Данная лабораторная работа представляет собой генетический алгоритм,
    # составленный для поиска заданного слова, как в игре "Угадай слово".
    # Для начала создадим графический интерфейс
    # функция получения нулевого поколения (нулевой популяции)
    def perv_pokolenie(self):
        return [''.join(ran.choices(list(self.alfavit.replace(' ', '')), k=len(self.ish_slovo))) for i in
                range(self.kol_osoby)]

    # 2 функции проверки соответствия целевому слову, чем больше выходной параметр несоответствия,
    # тем меньше приспособлена функция, во второй функции фитнес заводится в массив для дальнейшей сортировки
    def sootv(self, memb2):
        ne_sootv = 0
        for c1, c2 in zip(self.ish_slovo, memb2):
            if c1 == c2:
                ne_sootv += 1
        return ne_sootv

    def cikl_proverki(self, b):
        return [self.sootv(i) for i in b]

    # функция мутации, из всего набора генов(алфавита), выбирается любой и вставляется
    # на случайное место в мутируемом слове
    def mutate(self, slovo):
        r_ind = ran.choice(range(0, len(slovo)))
        r_simv = ran.choice(self.alfavit)
        out_slovo = list(slovo[:])
        out_slovo[r_ind] = r_simv
        out_slovo = ''.join(out_slovo)
        return out_slovo

    # функция сортировки, преобразует два массива в словарь, сортирует по ключам, возвращает массив
    # из ключей и значений, после чего с помощью цикла вытаскиваются из массива отсортированные слова
    def sort(self, fitness, popul):
        slovar = zip(popul, fitness)
        a = sorted(slovar, key=operator.itemgetter(1))
        sorti = []
        for i in range(len(a)):
            sorti.append(a[i][0])
        sorti.reverse()
        return sorti

    # функция кроссинговера, выбирается случайная точка пересечения, далее как в биологии:
    # один родитель передает гены до обозначеной точки, а другой после, формируется новый организм (ребенок_1)
    # и наоборот - соединяются две другие части генов, появляется второй организм (ребенок_2)
    def cross(self, parent_1, parent_2):
        tochka = ran.randint(1, len(parent_1) - 1)
        child_1 = parent_1[:tochka] + parent_2[tochka:]
        child_2 = parent_2[:tochka] + parent_2[tochka:]
        return [child_1, child_2]

    # функция эволюции: неудачных особей заменяют дети самых приспособленных родителей, формируется новая популяция
    def evolution(self, popul):
        par_1 = popul[ran.randint(0, len(popul) // 2)]
        par_2 = popul[ran.randint(0, len(popul) // 2)]
        childs = self.cross(par_1, par_2)
        popul[ran.randint(len(popul) // 2, len(popul) - 1)] = childs[0]
        popul[ran.randint(len(popul) // 2, len(popul) - 1)] = childs[1]
        return popul


class inter(gen_a):
    def __init__(self):
        self.root = Tk()
        self.root.title('Лабораторная работа №1')
        self.root.geometry('800x600')

        self.l1 = Label(self.root, text='Алфавит: ')
        self.l2 = Label(self.root, text='Целевое слово: ')
        self.l3 = Label(self.root, text='Количество особей: ')
        self.l4 = Label(self.root, text='Частота мутации: ')

        self.en1 = Entry(self.root, width=80)
        self.en2 = Entry(self.root)
        self.en3 = Entry(self.root)
        self.en4 = Entry(self.root)

        self.tx1 = Text(self.root, wrap=WORD)

        self.b1 = Button(self.root, text='Циклическая\nгенерация\nпопуляций', command=self.start)
        self.b2 = Button(self.root, text='Получить 1-ю\nпопуляцию', command=self.first_popylation)
        self.b3 = Button(self.root, text='Новая\nпопуляция', command=self.new_popylation)

        self.l1.place(x=0, y=10)
        self.l2.place(x=0, y=35)
        self.l3.place(x=250, y=35)
        self.l4.place(x=0, y=60)

        self.en1.place(x=70, y=10)
        self.en2.place(x=105, y=35)
        self.en3.place(x=370, y=35)
        self.en4.place(x=110, y=60)

        self.tx1.place(x=10, y=130)

        self.b1.place(x=660, y=230)
        self.b2.place(x=660, y=130)
        self.b3.place(x=660, y=180)

        self.root.mainloop()

    def start(self):
        self.main(self.en1.get(), self.en2.get(), self.en3.get(), self.en4.get(), self.tx1)
        self.all_pokol()

    def first_popylation(self):
        self.main(self.en1.get(), self.en2.get(), self.en3.get(), self.en4.get(), self.tx1)

    def new_popylation(self):
        self.new_popul()


if __name__ == "__main__":
    a = inter()