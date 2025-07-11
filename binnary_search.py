def binary_search(sorted_list, target):
    left = 0  # Инициализируем левый указатель на начало списка
    right = len(sorted_list) - 1  # Инициализируем правый указатель на конец списка

    # Продолжаем поиск, пока левый указатель не превысит правый
    while left <= right:
        mid = (left + right) // 2  # Вычисляем средний индекс (используем целочисленное деление)
        mid_value = sorted_list[mid] # Получаем значение по среднему индексу

        if mid_value == target:
            # Если элемент по среднему индексу равен целевому, мы нашли его
            print(f"'{target}' найден по индексу {mid}.")
            return mid
        elif mid_value < target:
            # Если элемент по среднему индексу меньше целевого,
            # значит, целевой элемент находится в правой половине.
            # Сдвигаем левый указатель вправо от среднего.
            left = mid + 1
        else: # mid_value > target
            # Если элемент по среднему индексу больше целевого,
            # значит, целевой элемент находится в левой половине.
            # Сдвигаем правый указатель влево от среднего.
            right = mid - 1
        print(mid_value)

    # Если цикл завершился, значит, целевой элемент не был найден
    print(f"'{target}' не найден в списке.")
    return -1

# Пример 1: Список товаров и целевой идентификатор
product_ids = [10, 25, 30, 45, 60, 70, 85, 90, 100]
print(f"Список товаров: {product_ids}")

print("\n--- Поиск существующих товаров ---")
# Поиск существующего товара
target_id_1 = 45
index_1 = binary_search(product_ids, target_id_1)
print(f"Индекс товара '{target_id_1}': {index_1}")

target_id_2 = 10
index_2 = binary_search(product_ids, target_id_2)
print(f"Индекс товара '{target_id_2}': {index_2}")

target_id_3 = 100
index_3 = binary_search(product_ids, target_id_3)
print(f"Индекс товара '{target_id_3}': {index_3}")

print("\n--- Поиск отсутствующих товаров ---")
# Поиск отсутствующего товара
target_id_4 = 55
index_4 = binary_search(product_ids, target_id_4)
print(f"Индекс товара '{target_id_4}': {index_4}")

target_id_5 = 5
index_5 = binary_search(product_ids, target_id_5)
print(f"Индекс товара '{target_id_5}': {index_5}")

target_id_6 = 110
index_6 = binary_search(product_ids, target_id_6)
print(f"Индекс товара '{target_id_6}': {index_6}")

print("\n--- Поиск в списке с одним элементом ---")
single_item_list = [77]
print(f"Список: {single_item_list}")
binary_search(single_item_list, 77)
binary_search(single_item_list, 99)

print("\n--- Поиск в пустом списке ---")
empty_list = []
print(f"Список: {empty_list}")
binary_search(empty_list, 42)