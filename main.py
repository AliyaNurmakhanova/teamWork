# Лабараториялық жұмыс №9
# 5 студент бірігіп, өз функциясын GidHub-та 1 репозиториге салып, топпен жұмыс жасауды үйренсін.
# Функцияналды және функционалды емес функция құру. Және олардың айырмашылықтарын айыру
# Функцияның ішінде функция шақыруға мысал
# Нәтижесінде тізім, кортеж, сөздік қайтаратын функция жазу
# Map, Filter и Reduce функцияларын қолданып мысал келтіреміз. Айырмашылықтарын анықтаймыз.
from functools import reduce

# Akimzhan Zhanerke
objects = []
def objects_add(obj):
    for i in range(4):
        objects.append(int(input()))

# Akimzhan Zhanerke
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
    mapped = list(map(lambda x: x/3, objects))
    summa = reduce(reduce_func, mapped)
    print(summa)

# objects_show(objects)

# Yntymak Ryskeldi
def reduce_func(el_prev, el):
    return el_prev+el

# Yerzhanova Almash
def GPA(obj):
    mapped = list(map(lambda x: x*3, objects))
    summa = reduce(reduce_func, mapped) # Yntymak Ryskeldi
    print('GPA:', summa/12)

GPA(objects)

# Nurmakhanova Aliya
def dateInputs():
    date_entry = ()
    while True:
        date = input("Введите дату поступления в университет : ")
        if not date:
            break
        date_entry = date_entry + (date,)
    return date_entry

def specialityInputs():
    specialities = ()
    while True:
        speciality = input("Введите специальность : ")
        if not speciality:
            break
        specialities = specialities + (speciality,)
    return specialities

print(dateInputs())
print(specialityInputs())