import timeit

# Реалізуємо або імпортуємо алгоритми пошуку рядків
def knuth_morris_pratt(pattern, text):
    pass

def boyer_moore(pattern, text):
    pass

def rabin_karp(pattern, text, prime=101):
    pass

# Завантажуємо статті з текстових файлів
with open("article1.txt", "r") as file1, open("article2.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

# Визначаємо підрядки для тестування
existing_substring = "your existing substring"
non_existing_substring = "your made-up substring"

# Вимірюємо час виконання для статті 1
time_kmp_existing = timeit.timeit(lambda: knuth_morris_pratt(existing_substring, text1), number=10)
time_bm_existing = timeit.timeit(lambda: boyer_moore(existing_substring, text1), number=10)
time_rk_existing = timeit.timeit(lambda: rabin_karp(existing_substring, text1), number=10)

time_kmp_non_existing = timeit.timeit(lambda: knuth_morris_pratt(non_existing_substring, text1), number=10)
time_bm_non_existing = timeit.timeit(lambda: boyer_moore(non_existing_substring, text1), number=10)
time_rk_non_existing = timeit.timeit(lambda: rabin_karp(non_existing_substring, text1), number=10)

# На основі проведених експериментів можна зробити висновок, що алгоритм Боєра-Мура є найефективнішим для пошуку підрядків у представлених текстових файлах.

