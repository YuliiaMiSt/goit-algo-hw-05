class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)] 

    def _hash_function(self, key):
        """Хеш-функція, яка визначає індекс ключа"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка пари ключ-значення у таблицю"""
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:  
                kvp[1] = value
                return
        self.table[index].append([key, value]) 

    def get(self, key):
        """Отримання значення за ключем"""
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1] 
        return None  

    def delete(self, key):
        """Видалення пари ключ-значення за ключем"""
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                self.table[index].remove(kvp) 
                print(f"Ключ '{key}' було успішно видалено.")
                return
        print(f"Ключ '{key}' не знайдено.")

    def display(self):
        """Виведення всієї таблиці"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Індекс {i}: {bucket}")
            else:
                print(f"Індекс {i}: порожньо")

# Приклад використання

# Створюємо таблицю хешування
hash_table = HashTable(size=10)

# Вставляємо ключі та значення
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)
hash_table.insert("grape", 40)

# Виводимо таблицю до видалення
print("Таблиця хешування до видалення:")
hash_table.display()

# Видаляємо ключ 'banana'
hash_table.delete("banana")

# Виводимо таблицю після видалення
print("\nТаблиця хешування після видалення ключа 'banana':")
hash_table.display()

# Видаляємо ключ, якого немає
hash_table.delete("pear")



