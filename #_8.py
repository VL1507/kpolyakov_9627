# задание 8
perv = 'МАРИ'
posl = 'ИНА'
spisok = []
for a in perv:
    for b in perv:
        for c in perv:
            for d in perv:
                nach = a + b + c + d
                if nach.count('М') == nach.count('А') ==\
                    nach.count('Р') == nach.count('И') == 1:
                    for i in posl:
                        for f in posl:
                            for g in posl:
                                for h in posl:
                                    spisok.append(nach + i + f + g + h)
s = sorted(spisok)
print(s.index('МАРИАННА') + 1)  # 1078
