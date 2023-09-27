
print("Калькулятор приветствует Вас!!!")
print("Выберите действие")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Факториал")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")

from math import *
komanda = int(input("Какое хотите сделать действие? "))
match komanda:
    case 1:
         while True:
            try:
                print(int( input("введите первое число: ")) + int(input("введите второе число:  "))) 
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
        
    case 2:
         while True:
            try:
                print(int(input("введите первое число:  ")) - int(input("введите второе число: ")))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
    case 3:
        while True:
            try:
                print(int(input("введите первое число:  ")) * int(input("введите второе число: "))) 
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
    case 4:
        while True:
            try:
                num_1 = int(input("введите первое число:  "))
                num_2 = int(input("введите второе число: "))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
       
        if num_2 == 0 :
            print(int(input("ERROR") ))
        else:
            print (num_1/num_2)
    case 5:
        while True:
            try:
                print( int( input("введите первое число: ")) ** int(input("введите второе число:  ")))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
    case 6:
        while True:
            try:
                print( int( input("введите число: ")) **0.5)
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
        
    case 7:
       while True:
            try:
                print(factorial (int( input("введите число: "))))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
            
    case 8:
          while True:
            try:
                print(sin(int(input("введите число: "))))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
            
        
    case 9:
        while True:
            try:
                print(cos(int(input("введите число: ")) ))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
       
    case 10:
        while True:
            try:
                print(tan(int("введите число: ")))
                break
            except ValueError:
                print("Ой, вы ввели что-то не то")
       
        