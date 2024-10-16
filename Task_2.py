def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0  
    upper_bound = None  
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Якщо знайшли елемент, повертаємо кількість ітерацій і значення
            return (iterations, arr[mid])
        
        elif arr[mid] < target:
            left = mid + 1 
        else:
            upper_bound = arr[mid] 
            right = mid - 1  
    
    # Якщо елемент не знайдений, повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)
