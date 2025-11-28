def log_call(func):
    def decorated(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула: {result}")
        return result
    return decorated

@log_call
def sum(a, b):
    return a + b
print(sum(5, 1))