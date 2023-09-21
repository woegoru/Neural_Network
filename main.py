#присоединяем используемые файлы
import neural_networks as nn
import training_s as trs

masha = nn.Layer(10, 35) #создаем нейронную сеть Маша, состоящую из слоя 10 нейронов с 35 выходами
masha.educ(trs.training_s_init('C:/Users/dasha/OneDrive/Рабочий стол/training_sample'), 0.1) #обучаем нейронную сеть
print(masha.activate(trs.cnvrt('C:/Users/dasha/OneDrive/Рабочий стол/training_sample/input/0.png'))) #выводим ответ


