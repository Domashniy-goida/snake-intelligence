# Данные
name = "Василиса"
weight = float(input("Текущий вес (г): "))
temp = float(input("Температура в террариуме (°C): "))
is_active = input("Змея активна? (да/нет): ").lower() == "да"

print(f"\n--- Отчет системы для {name} ---")

print()

# 1. Проверка веса (Билет 5)
if weight > 2000:
    status = "Избыточный вес"
elif 500 <= weight <= 2000:
    status = "Норма"
else:
    status = "Недовес / Молодая особь"

print()

# 2. Сложное условие (Вложенность)
if temp < 22 or temp > 32:
    alert = "КРИТИЧЕСКИЙ УРОВЕНЬ ТЕМПЕРАТУРЫ!"
    if is_active:
        action = "Срочно проверить термостат, змея в стрессе."
    else:
        action = "Змея в анабиозе, риск гибели."
else:
    alert = "Температура в норме"
    action = "Вмешательство не требуется."

print(f"Статус веса: {status}")
print(f"Климат: {alert}")
print(f"Рекомендация: {action}")

print()

# Расчет корма 
food_weight_min = weight * 0.08
food_weight_max = weight * 0.10

print(f"\n--- Рекомендации по кормлению ---")
print(
    f"Оптимальный вес корма: {food_weight_min:.1f}г - {food_weight_max:.1f}г")

if weight < 100:
    print("Тип корма: Живые или размороженные 'голыши'.")
elif 100 <= weight < 500:
    print("Тип корма: Опушата или мелкие мыши.")
else:
    print("Тип корма: Взрослые мыши или крысы среднего размера.")

print()

# История веса (Списки)
weight_history = []
for i in range(1, 7):
    weight *= 1.05
    weight_history.append(round(weight, 1))
    print(f"в месяце {i} вес змеии будет примерно: {weight:.1f}г")

print()
print(f"Минимальный вес в истории: {min(weight_history)}г")
print(f"Максимальный вес в истории: {max(weight_history)}г")
print(f"Всего записей: {len(weight_history)}")
print(f"Средний вес за период: {sum(weight_history)/len(weight_history):.1f}г")

weight_list = []
weight = 100
for i in range(1, 7):
    weight *= 1.1
    weight_list.append(round(weight, 1))
print(weight_list)
