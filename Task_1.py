class HashTable:
    def __init__(self):
        self.size = 10 
        self.table = [[] for _ in range(self.size)]  

    def hash_function(self, key):
        return hash(key) % self.size  

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]
        
        # Перевіряємо, чи існує вже ключ в хеш-таблиці
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket[i] = (key, value)  
                return
        
        # Якщо ключ не знайдено, додаємо новий ключ-значення
        bucket.append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        
        # Шукаємо значення за ключем
        for k, v in bucket:
            if k == key:
                return v
        
        # Якщо ключ не знайдений, повертаємо None
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        
        # Шукаємо ключ у відповідному "відрі" (списку)
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                del bucket[i] 
                print(f"Ключ '{key}' успішно видалений.")
                return
        
        # Якщо ключ не знайдений
        print(f"Ключ '{key}' не знайдено.")
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


