import ephem
print("Начало")
mars = ephem.Mars('2000/01/01')
print("Обращение")
constellation = ephem.constellation(mars)
print("Результат")
print(constellation)



