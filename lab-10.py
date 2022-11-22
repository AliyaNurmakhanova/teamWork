#10 кірістірілген функцияны алып, бір бірімен үйлестіріп бағдарлама жазамыз. Функциялар осыған дейін біз қолданбаған болуы қажет.

#бир функция орындалып сол файлдын ишине салынып турса деп ойластырдым
#не туралы жасауға болатынын қарастырып көріндерші, мен оларды файлдарга салып отырумен айналысамын деп
#2 кірістірілген функциядан алып бирдене жасаса тема болады

sometext = 'Salem'
file = open('smth.txt', 'w')
file.write(str(sometext))
file.close()

file = open('text.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('text.txt', 'r')
line = file.readline()
print('\n', line)
file.close()

file = open('text.txt', 'r')
word = file.read(6)
print('\n', word)
file.close()