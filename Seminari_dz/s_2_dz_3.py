# Задать список из n чисел последовательности (1+1/n)**n 
# и вывести на экран их сумму
def Cal_num(n):
    result = 0
    sum = 0
    a=[]
    for i in range (1, n+1):
        result = round((1+(1/i))**i, 3)
        sum += result 
        a.append(result)
    print(a) 
    print(f"Сумма = {sum}") 
    
n = int(input('Введите число : '))
Cal_num(n)