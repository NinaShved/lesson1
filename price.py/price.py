#age=input("Введите Ваш возраст ")
#a=abs(int(age)) 
#print(a)           
#def var(a):
#    if a <= 6:
#        print(f"Тебе {a} лет и ты ходшь в садик")
#    elif 6 < a <= 18:    
#        print(f"Тебе {a} лет и ты учишься в школе")#
#    else: 
#        print(f"Вам {a} лет и Вы учитесь в ВУЗе или работаете")    
#var(a)


#Проверяем является переданная переменная строкой или это текст.
a="j"
b="Learn"
#c=tol(a,b)
def tol(a,b):
    if type(a) == int or type(b) == int or type(a) == float or type(b) == float:
        print("Это не строки")
        return "0"
    else:
        print("Это строки")  
        if a != b and len(a) > len(b):
            print("Первая строка длиннее второй")
            return "2"
        if a != b and b == "Learn":
                print("Строки разные и вторая Learn")
                return "3"        
        else:        
            print("Строки одинаковые")
            return "1"
    
print(tol(a,b))  
     