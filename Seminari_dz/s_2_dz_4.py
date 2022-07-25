# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число. 

num = int(input('Введите число  = ')) 
my_list = [] 
for i in range(-num,num+1): 
    my_list.append(i) 
print(my_list) 
proiz=1
# with open('c:/Users/User/Documents/Python/Python/Seminari_dz/file.txt', 'r') as f: # абсолютный путь
with open('Python/Seminari_dz/file.txt', 'r') as f: # относительный путь
    for line in f:
        p=int(line)
        print(f"my_list[{p}] = {my_list[p]}")
        proiz *= my_list[p]
    print(f"proiz = {proiz}")

# with open('c:/Users/User/Documents/Python/Python/Seminari_dz/file.txt', 'w') as f:
#     f.close()  # создание файла file.txt и его закрытие
