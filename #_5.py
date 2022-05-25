# задание 5
def f(n):
    new_n = bin(n)[2:]
    new_n += new_n[-2]
    new_n += new_n[1]
    return int(new_n, 2)


for i in range(2, 1000):
    if f(i) > 210:
        print(i)
        break

# 53
