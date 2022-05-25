#FIXME не работает
def prost(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


spisok = set()
for i in range(412567, 473266):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            if prost(j) and prost(i/j):
                spisok.add(i)
print(spisok)
print(len(spisok))
