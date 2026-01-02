# Начало проекта Snake Intelligence
name = input("Введите имя змеи: ")
age = int(input("Введите возраст змеи (полных лет): "))
weight = float(input("Введите вес змеи в граммах: "))
is_heavy_enough = weight > 400

print(f"Змея {name}: возраст {age} лет, вес {weight}г. Данные приняты.")
print(f"Змея достаточно весит? {is_heavy_enough}")
print(f"Тип переменной: {type(is_heavy_enough)}")
print(type(1233))