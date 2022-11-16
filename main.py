# Лабараториялық жұмыс №9
# 5 студент бірігіп, өз функциясын GidHub-та 1 репозиториге салып, топпен жұмыс жасауды үйренсін.
# Функцияналды және функционалды емес функция құру. Және олардың айырмашылықтарын айыру
# Функцияның ішінде функция шақыруға мысал
# Нәтижесінде тізім, кортеж, сөздік қайтаратын функция жазу
# Map, Filter и Reduce функцияларын қолданып мысал келтіреміз. Айырмашылықтарын анықтаймыз.
from functools import reduce

#Akimzhan Zhanerke
objects = []
def objects_add(obj):
    for i in range(4):
        objects.append(float(input()))
        # if objects[i] == ' ':
        #     break

def objects_show(obj):
    print(objects)

objects_add(objects)
objects_show(objects)

def reduce_func(el_prev, el):
    return el_prev+el

def GPA(obj):
    mapped=list(map(lambda x:x*3,objects))
    print(mapped)
    summa = reduce(reduce_func,mapped)
    #summa_grades = reduce(reduce_func,objects)
    print(summa/12)

GPA(objects)