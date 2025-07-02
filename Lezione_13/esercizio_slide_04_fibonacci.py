def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return int(fibonacci(n-1) + fibonacci(n-2))
    
print(fibonacci(6))

print(fibonacci(50))
    
