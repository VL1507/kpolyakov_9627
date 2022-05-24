# задание 2
print('y z x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x and (z and (not w) or y and (not w)\
                    or y and (not z))) == 1:
                    print(y, z, x, w)                   
'''
y z x w
0 1 1 0
1 0 1 0
1 0 1 1
1 1 1 0
'''
