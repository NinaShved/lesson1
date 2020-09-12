# создание цикла по списку
#sps=[2,3,4,12,17345,-1,-15]
#for nbr in sps:
#    a=nbr+1
#    print(a)

#    цикл на введенную с клавиатуры строку
#a=input("Введите строку :")
#print(a)
#for letter in a:
#    print(letter)

#Цикл по оценкам
#maz = [
#      {"kls":"2a", "marks":[4,4,5,4,5]},
#      {"kls":"3б", "marks":[3,5,5,4]},
#      {"kls":"10г", "marks": [5,5,3,4,4,4]}
#]
#    
#a = 0
#d = 0
#b = int(len(maz))
#for number in range(b):
#    c = int(len(maz[a]["marks"]))
#    smarks = 0
#    for num in range(c):
#        z = int(maz[a]["marks"][num])
#        smarks += z
#    kl = maz[a]["kls"]
#    d += (round(smarks/c,2))
#    print(f"В классе {kl} средняя оценка {round(smarks/c,2)}")
#    a += 1
#
#d1 = round(d/b,2)
#print(f"Средняя оценка в школе {d1}")   

# Цикл  While

def ask_user():
    while True:
        try:
            usay = input("Как дела?")
            if usay == "Хорошо":
                break
        except KeyboardInterrupt:
            print("Пока!")    
            break
#ask_user()        

# Работа со словарем
dic = {"Как дела?":"Хорошо!", 
       "Что делаешь?":"Программирую",
       "Когда перерыв?":"Скоро",
       "Пойдешь в кафе?":"С удовольствием!"}
def check(dic):
    while True:      
        a = input("Введите Ваш вопрос :")
        if a in dic and a != "Стоп":
            print(dic[a])
        else:    
            if a == "Стоп":
                print("Спасибо за работу со словарем")
                break
#check(dic)            
# Исключения
def discounted(price, discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        if discount >= 100:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        print(price_with_discount)     
    except(TypeError, ValueError, SyntaxError):   
        print("Неверные данные")        

discounted(2!0,5)
