# Лабараториялық жұмыс №9
# 5 студент бірігіп, өз функциясын GidHub-та 1 репозиториге салып, топпен жұмыс жасауды үйренсін.
# Функцияналды және функционалды емес функция құру. Және олардың айырмашылықтарын айыру
# Функцияның ішінде функция шақыруға мысал
# Нәтижесінде тізім, кортеж, сөздік қайтаратын функция жазу
# Map, Filter и Reduce функцияларын қолданып мысал келтіреміз. Айырмашылықтарын анықтаймыз.

#Akimzhan Zhanerke
objects = []
def objects_add(obj):
    for i in range(10):
        objects.append(input())
        if objects[i] == ' ':
            break

def objects_show(obj):
    print(objects)

objects_add(objects)
objects_show(objects)

def GPA(obj):
    mapped=list(map(lambda x:x/3,objects))
    print(mapped)

GPA(objects)