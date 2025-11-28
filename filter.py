def func(x):
    return x % 2 == 0
nums = [1,2,3,4,5,6,7,8,9]
filtered = filter(func, nums)
print(list(filtered))