# задание 22
def f(n):
    i = 0
    while n > 0:
        i = i + n % 16
        n = n // 16
    return i % 15


for i in range(10, 100):
    if f(i) == 0:
        print(i)
        
'''
15
30
45
60
75
90
'''
