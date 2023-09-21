#программа инициализации нейрона и его обучения. Нейрон может распознать одну цифру.

from random import random 

class Neuron(): #инициализация нейрона
    def __init__(self, input_num):
        self.weight = list() #нулевой вес нейрона
        for i in range(input_num + 1):
            self.weight.append(random()) #создание списка весов нейрона кроме нулевого

    def limit(self, s): #определение порога
        if s > 0:
            return 1
        return 0
        
    def activate(self, input): #активация нейрона
        if len(self.weight)-1 != len(input):
            raise Exception('mnoga bukaf') #ошибка, которая возникает, если введено данных больше, чем входов
        s = 0
        s += self.weight[0] #сумма увеличивается на нулевой вес
        for i in range(len(self.weight) - 1):
            s += input[i]*self.weight[i + 1] #действие(сумма), которое выполняется внутри нейрона по формуле
        return self.limit(s)

    def educ(self, traning_s, speed): #обучение нейрона (параметр traning_s содержит в себе выходы[0] и входы[1] - пример 
        #правильного выполнения задания нероном)
        switch = 1 #переключатель, который будет запускать обучение, пока нейрон не выполнит все тесты правильно
        while switch:
            count = 0 #счетчик правильных ответов
            for i in range(len(traning_s[1])):
                neuron_out = self.activate(traning_s[1][i])# активируем нейрон и подаем ему данные на входы
                if neuron_out == traning_s[0][i]:
                    count += 1 #если ответ нейрона верный, увеличиваем счетчик
                else:
                    self.weight[0] = self.weight[0] + speed * (traning_s[0][i] - neuron_out) #увеличиваем нулевой(пороговый) 
                    #вес при неверном ответе
                    for j in range(1, len(self.weight)):
                        self.weight[j] = self.weight[j] + speed * traning_s[1][i][j - 1] * (traning_s[0][i] - neuron_out)
                        #увеличиваем остальные веса при неверном ответе нейрона
            if count == len(traning_s[1]): #когда количество верных ответов совпадает с количеством тестов, цикл заканчивается
                switch = 0
            
#сборка входных данных обучающей выборки
one = (0, 0, 1, 0, 0, 1, 0, 0, 1)
two = (1, 0, 1, 1, 0, 1, 1, 0, 1)
three = ( 1, 1, 1, 1, 1, 1, 1, 1, 1)
input = (one, two, three)
#выходные данные обучающей выборки(правильные ответы, которые мы ждем от нейрона)
output = (0, 1, 0) #здесь нейрон должен определять цифру два ответом 1
#сборка выборки
traning_s = (output, input)
masha = Neuron(9) #создание(инициализация) нейрона
masha.educ(traning_s, 0.1) #запуск обучения нейрона

print(masha.activate(three)) #при вводе в скобках определенного числа, обученный нейрон должен выдать соответствующий
#результат
