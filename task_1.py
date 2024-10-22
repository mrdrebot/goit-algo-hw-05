from typing import Callable

def caching_fibonacci() -> Callable[[int], int]: 
    cache: dict = {} 

    def fibonacci(n: int) -> int:
        nonlocal cache

        if n in cache:
            return cache[n]

        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci 

# Отримуємо функцію fibonacci 
fib = caching_fibonacci() 

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі 
print(fib(10)) # Виведе 55 
print(fib(15)) # Виведе 610
