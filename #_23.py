# задание 23
def f(x, y):
    if x > y or x == 10:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x * 2, y)


print(f(1, 21))    # 32
