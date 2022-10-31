while True:
    data = input("Введите число:\n")
    try:
        if data.isdigit():
            n = int(data)
            if (10**13>=n>=1):
                break
    except:
        pass
    print('Число введено неправильно!')
line = [1,1]
ind = 1
new_line = []
while ind <= n:
    new_line = []
    for i in range(len(line)-1):
        new_line.extend([line[i], line[i]+line[i+1]])
    new_line.append(1)
    ind += 1
    line = new_line
print('Линейный расчет: '+str(line.count(n)))

# Code from: https://stackoverflow.com/a/18114286/20377539
from math import gcd
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount
print('Расчет по функции Эйлера: '+str(phi(n)))
