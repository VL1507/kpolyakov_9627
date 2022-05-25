f = open('егэ_информатика\\17-1.txt')
l = f.readlines()
s = []
for i in range(len(l) - 1):  # исправляю кривой файл
    s.append(l[i][:-1])
s.append(l[-1])

pari = []
for i in range(1, len(s)):
    if (int(s[i - 1]) % 7 == 0 and int(s[i]) % 17 != 0) or\
                (int(s[i - 1]) % 17 != 0 and int(s[i]) % 7 == 0):
        pari.append(int(s[i - 1]) + int(s[i]))

print(len(pari))  # 2510
print(min(pari))  # -19677
