
# Задание 1
price=float(input("Введите цену 1 кг конфет: "))
for kg in range(1,11):
    print(kg,"кг =",price*kg)


# Задание 2
a=int(input("Введите a: "))
b=int(input("Введите b: "))
summa=0
count=0
for i in range(a,b+1):
    summa+=i
    count+=1
average=summa/count
print("Среднее арифметическое:",average)


# Задание 3
summa=0
for i in range(1,21):
    price=float(input(f"Введите стоимость товара {i}: "))
    summa+=price
average=summa/20
print("Средняя стоимость товара:",average)


# Задание 4
cells=1
for hour in range(3,25,3):
    cells*=2
    print(f"Через {hour} часов: {cells} клеток")


# Задание 5
distance=10
total=0
for day in range(1,11):
    print(f"День {day}: {distance:.2f} км")
    if day<=7:
        total+=distance
    distance*=1.1
print(f"Суммарный путь за первые 7 дней: {total:.2f} км")


# Задание 6
n=int(input("Введите количество чисел: "))
summa=0
positive=0
for i in range(n):
    x=int(input(f"Введите число {i+1}: "))
    summa+=x
    if x>0:
        positive+=1
print("Сумма всех чисел:",summa)
print("Количество положительных чисел:",positive)


# Задание 7
x=0
for i in range(1,11):
    x+=1/i
print("X =",x)


# Задание 8
z=1
for i in range(2,21,2):
    z*=i
print("Z =",z)


# Задание 9
x=float(input("Введите x: "))
y=0
for i in range(1,10):
    if i%2==1:
        y-=i**2*x
    else:
        y+=i**2*x
print("Y =",y)


# Задание 10
x=float(input("Введите x: "))
y=0
for i in range(1,18,2):
    y+=x/i
print("Y =",y)


# Задание 11
n=int(input("Введите n: "))
y=1
for i in range(1,n+1):
    y*=i
print("n! =",y)


# Задание 12
y=0
for i in range(0,11):
    if i%2==0:
        y+=3**i
    else:
        y-=3**i
print("Y =",y)


# Задание 13
n=int(input("Введите количество чисел: "))
a=[]
for i in range(n):
    x=float(input(f"Введите число {i+1}: "))
    a.append(x)
count=0
for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        count+=1
print("Количество таких чисел:",count)
