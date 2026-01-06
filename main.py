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

print()

# словарные значения (билет 1)

snake_inventory = {
    "caninus_samka": {
        "name": "Василиса",
        "age": 2,
        "weight": 500,
        "is_venomous": False,
        "favorite_food": "крысы",
        "time_of_feeding": "ночь",
        "health_status": "Perfect",
        'days_since_last_meal': 12,
        'price': 0},
    "caninus_samets": {
        "name": "Вкусилий",
        "age": 2,
        "weight": 450,
        "is_venomous": False,
        "favorite_food": "крысы",
        "time_of_feeding": "ночь",
        "health_status": "Perfect",
        'days_since_last_meal': 16,
        'price': 240000}}

print(snake_inventory["caninus_samka"]["weight"])

total_weight = sum(
    snake_inventory[snake]["weight"] for snake in snake_inventory)
print(f"Общий вес змей: {total_weight}г")

print()

print(f"Цена змеи {snake_inventory['caninus_samets']['name']}: {snake_inventory['caninus_samets']['price']} руб.")


for key, data in snake_inventory.items():
    name = data["name"]

    # Если данных нет, ставим 0 (число!), чтобы сравнение > 14 сработало
    days = data.get("days_since_last_meal", 0)
    price = data.get("price", 0)

    # Теперь сравнение всегда идет: число > число
    if days > 14:
        print(f"{name} пора кормить!")

    if price > 200000:
        print(f"Цена змеи {name} высокая: {price} руб.")

    # А вот теперь проверяем на "самку" через ключ (key)
    if key.endswith("_samka"):
        print(f"Эта особь {name} — потенциальная мать.")

    for key, data in snake_inventory.items():
        key = 'udav_samka'
        data = {"name": "Абаддон",
        "age": 4,
        "weight": 8500,
        "is_venomous": False,
        "favorite_food": "крысы",
        "time_of_feeding": "Day",
        "health_status": "Perfect",
        'days_since_last_meal': 10,
        'price': 740000
        }
# альтернативный вариант вывода всех характеристик змей
for key, data in snake_inventory.items():
    print(f"--- Отчет по особи: {key} ---")

    # Внутренний цикл: идет по характеристикам внутри каждой змеи
    # sub_key - это "weight", "price" и т.д.
    # value - это конкретные значения (500, 240000...)
    for sub_key, value in data.items():
        print(f"Поле: {sub_key} | Значение: {value}")

    print()  # Просто пустая строка для красоты между змеями

# вариант обновления данных
updates = {
    "caninus_samka": {"weight": 550, "health_status": "Excellent"},
    "caninus_samets": {"weight": 480, "days_since_last_meal": 0}
}

# Вложенный цикл для ввода данных в snake_inventory
for zmeya, data in updates.items():
    # Проверяем, есть ли такая змея в нашей базе
    if zmeya in snake_inventory:
        # Внутренний цикл вводит каждое новое значение
        for characteristic, value in data.items():
            snake_inventory[zmeya][characteristic] = value
            print(f"Обновлено: {zmeya} -> {characteristic} теперь {value}")


# множества (билет 1)

# Создаем список видов змей (тут есть дубликаты)
species_list = ["caninus", "boa", "caninus", "python", "boa"]

# Превращаем в множество - дубликаты исчезают сами!
unique_species = set(species_list)
print(unique_species)  # Выведет: {'caninus', 'boa', 'python'}

print()

# Змеи, которые выставлены на продажу в США/Германию
on_sale = {"caninus_samka", "caninus_samets", "udav_samka"}

# Змеи, которые сейчас на лечении (их нельзя продавать)
medical_treatment = {"caninus_samka", "python_new"}

# 1. Кого мы МОЖЕМ продать прямо сейчас? (Разность)
ready_to_go = on_sale - medical_treatment
print(f"Готовы к продаже: {ready_to_go}")

# 2. Какие змеи одновременно и в продаже, и на лечении? (Пересечение)
# Это потенциальная проблема в базе!
problem_snakes = on_sale & medical_treatment
print(f"Внимание! Ошибочный статус у: {problem_snakes}")

high_price_snakes = {"caninus_samets", "udav_samka", "python_new"}
ready_for_breeding = {"caninus_samka", "udav_samka", 'setka_samka'}
high_price_and_breeding = high_price_snakes & ready_for_breeding
print(f"Змеи с высокой ценой и готовые к разведению: {high_price_and_breeding}")

# множества через словари 

# Автоматически создаем множество ID тех, кто дороже 500 000, используя данные из словаря
high_price_snakes = {
    key for key, data in snake_inventory.items() if data.get("price", 0) > 500000}

# Автоматически создаем множество самок
ready_for_breeding = {key for key in snake_inventory if key.endswith("_samka")}

# И теперь магия пересечения работает на АВТОМАТИЧЕСКИХ данных
high_price_and_breeding = high_price_snakes & ready_for_breeding
print(f"Змеи с высокой ценой и готовые к разведению: {high_price_and_breeding}")

# Автоматически создаем множество змей, которых нужно срочно кормить по характеристикам из словаря
urgent_feeding = {key for key, data in snake_inventory.items() if data.get("days_since_last_meal", 0) > 14}
print(f"Змеи, которых нужно срочно кормить: {urgent_feeding}")
