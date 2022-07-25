# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def Cal_num(num):
    result = 1
    a=[]
    for i in range (1, num+1):
        result *= i
        a.append(result)
    print(a)  
num = int(input('Введите число : '))
Cal_num(num)