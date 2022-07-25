# Реализуйте алгоритм перемешивания списка.
my_list = [] 
for i in range(5):
    num = input('Введите элемент списка  = ')
    my_list.append(num) 
print(f"Исходный список    {my_list}") 
i=0 
for i in range(3):
    if i==0:
        (my_list[i], my_list[i+2]) = (my_list[i+2], my_list[i])
    if i==1:
        (my_list[i], my_list[i+3]) = (my_list[i+3], my_list[i])
    if i==2:
        (my_list[i+1], my_list[i+2]) = (my_list[i+2], my_list[i+1])    
print(f"Перемешаный список {my_list}")
