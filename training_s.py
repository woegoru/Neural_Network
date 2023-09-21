import numpy as np
from PIL import Image #библиотека обработки изображений
from pathlib import Path #библиотека для манипулирования путями

def cnvrt(path): #конвертация картинки в список
    picture = Image.open(path) #открытие картинки
    picture.load() #загрузка картинки
    a = np.array(picture.convert('1'), dtype='int32')
    l = list()
    for el in a: #из матрицы данных получаем список 
        l += list(el)
    return l

def training_s_init(path): #собираем обучающую выборку
    input_fld = Path(path + '/input') #получаем путь к папке
    output_f = open(path + '/output.txt') #открываем файл с выходами обучающей выборки
    output_l = output_f.readline() #считываем строку выхода
    out = list() #список для выходов
    while output_l:
        out.append(list((int(elem) for elem in output_l.split('\n')[0]))) #получаем список выходов обучающей выборки
        output_l = output_f.readline() #считываем следующую строку выхода
    inp = list() #список для входов
    for i in range(len(list(input_fld.iterdir()))):
        inp.append(cnvrt(path + f'/input/{i}.png')) #собираем вход из конвертированной в строку картинки
    return (out, inp) #возвращаем обучающую выборку, состоящую из списков




            



