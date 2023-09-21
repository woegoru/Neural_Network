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

    def educ(self, training_pair, speed):#обучени нейрона
        out = self.activate(training_pair[1])#берем обучающую пару выход-вход и активируем нейрон
        if out == training_pair[0]:
            return 1 #получаем верный ответ, если нейрон прошел тест правльно
        self.weight[0] += speed * (training_pair[0] - out) #если ответ неверный изеняем нулевой(пороговый) вес по формуле
        for i in range(1, len(training_pair[1])):
            self.weight[i] += speed * training_pair[1][i - 1] * (training_pair[0] - out) #изменяем остальные веса 
        return 0
          
class Layer(): #слой нейронов
    def __init__(self, neurons_num, input_num):
        self.neurons = list()
        for i in range(neurons_num): #добавляем нейроны в слой
            self.neurons.append(Neuron(input_num))
    
    def activate(self, input): #активируем слой
        output = list() #создаем список для значений выхода
        for neuron in self.neurons:
            output.append(neuron.activate(input)) #составляем вывод ответа (выхода), который выведет слой
        return output
    
    def educ(self, training_s, speed): #обучение списка
        switch = 1 #переключатель, который будет запускать обучение, пока нейрон не выполнит все тесты правильно
        while switch:
            count = 0 #счетчик правильных ответов
            for i in range(len(self.neurons)):
                for j in range(len(training_s[0])):
                    count += self.neurons[i].educ((training_s[0][j][i], training_s[1][j]), speed) 
                    #обучаем слой нейронов и увеличиваем счетчик
            print(count, '/', (len(self.neurons) * len(training_s[0]))) #выводим номер правильного ответа иномер попытки
            if count == (len(self.neurons) * len(training_s[0])): #если количество попыток и правильных ответов совпадает, 
                #прекращаем обучение
                switch = 0
        
               
            

                   
               





