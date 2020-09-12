# print("Привет мир!")
# print("Привет,программист!")
# print(2+2)

#print(int(1/3)) 
#print(10**2)
# print(10//2)
# a=2
# print(a+7)
# name="Нина"
# print(name)
# print(len(name[:-1]))
# print(name[:-1])
# a=2
# b=0.5
# print(a+b)
# d="Привет {name}!".format(name=name)
# print(d)
# v=input("Введите число от 1 до 10 ")
# b=float(v)
# c=b+10
# print(c)
# name=input("Введите Ваше имя: ")
# print(f"Привет, {name}! Как дела?")
#print(float('1'))
#print(int('2.5'))
#print(bool(1))
#print(bool(''))
#print(bool(0))
#name="Нина"
#print(len(name[:-2]))
#print(name[:-2])
#numbers=[3,5,7,9,10.5]
#print(numbers)
#print(len(numbers))
#numbers.append('Python')
#print(len(numbers))
#print(numbers[0:1])
#print(numbers[-1])
#print(numbers[1:4])
#del numbers[5]
#print(numbers)
#print(type(numbers))
#dic={"city":"Москва","temperature":"20"}
#print(dic["city"])
#a=float(dic["temperature"])
#b=a-5
#print(b)
#dic["temperature"] = int(dic["temperature"]) - 5
#print(dic)
#print(dic.get("country"))
#print(dic.get("country","Россия"))
#dic["date"] = "23.08.2019"
#print(dic)
#print(len(dic))
#a=len("Вася и Маша")
#print(a)
#a=2.395
#b=3
#print(round(a, 2))
#list = ['A', "S","R","D","e"]
#print(list[-1])
one="Learn"
two="python"
def get_summ(one, two, delimiter="&"):
    a=f"{one}{delimiter}{two}"
    print(a)
    a1=a.upper()
    print(a1)
get_summ(one, two, delimiter='&')    