class HashTable:
    def _get_hash_index(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._get_hash_index(key)
        # Получаем список (цепочку) по вычисленному индексу
        bucket = self.table[index]

        # Проверяем, существует ли ключ уже в этом "ведре" (списке)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Если ключ найден, обновляем значение и выходим
                bucket[i] = [key, v]
                print(f"Ключ '{key}' обновлен. Новое значение: '{v}'.")
                return
        # Если ключ не найден, добавляем новую пару [ключ, значение]
        bucket.append([key, v])
        print(f"Ключ '{key}' со значением '{v}' добавлен.")

    def get(self, key):
        """
        Возвращает значение, связанное с данным ключом.
        Если ключ не найден, возвращает None.
        """
        index = self._get_hash_index(key)
        bucket = self.table[index]

        # Ищем ключ в соответствующем "ведре"
        for k, v in bucket:
            if k == key:
                print(f"Найден ключ '{key}'. Значение: '{v}'.")
                return v # Возвращаем найденное значение
        print(f"Ключ '{key}' не найден в хеш-таблице.")
        return None # Ключ не найден

    def remove(self, key):
        """
        Удаляет пару ключ-значение из хеш-таблицы по заданному ключу.
        """
        index = self._get_hash_index(key)
        bucket = self.table[index]

        # Ищем ключ в соответствующем "ведре" для удаления
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] # Удаляем элемент по индексу
                print(f"Ключ '{key}' успешно удален.")
                return
        print(f"Ошибка: Ключ '{key}' не найден для удаления.")

    def display_all(self):
        """
        Отображает все содержимое хеш-таблицы (для отладки).
        """
        print("\n--- Содержимое хеш-таблицы ---")
        for i, bucket in enumerate(self.table):
            print(f"Индекс {i}: {bucket}")
        print("----------------------------")
    
    def __init__(self, capacity=10):
        """
        Инициализирует хеш-таблицу.
        Capacity (емкость) - это размер базового массива.
        """
        self.capacity = capacity
        # Создаем массив списков. Каждый внутренний список будет хранить пары [ключ, значение]
        # для разрешения коллизий (метод цепочек).
        self.table = [[] for _ in range(self.capacity)]
        print(f"Хеш-таблица инициализирована с емкостью {self.capacity}.")