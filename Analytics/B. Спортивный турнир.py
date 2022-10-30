import os.path
import math

main_path = os.path.dirname(os.path.abspath(__file__))
with open(main_path + '\\input.txt', 'r') as file_name:
    names = file_name.read().split()
num = int(math.log2(int(names.pop(0))+1)) # Получаем количество раундов
def func_champions(num, names):
    rate={}
    for name in set(names): # Создаем словарь с ключом-Фамилия, значением-количество сыграных игр
        rate[name] = names.count(name)
    for i in range(num): # Считаем по каждому раунду
        dict = {key: value for key, value in rate.items() if value >= (i+1)} # Получаем словарь игроков, учавствующих в раунде, по количеству сыграных игр. 
                                                                             # То есть, если игрок сыграл две игры, значит он учавствовал в первом и втором раунде, 
                                                                             # в третьем его не может быть
        if len(dict) != 2**(num-i): # Количество участников уменьшается в два раза после каждого раунда
            print('Round '+str(i+1)+' is not OK!') # Если количество участников не совпадает
            return 'NO SOLUTION'
    return ' '.join(dict.keys()) # Возвращаем последнее значение словаря последнего раунда

out = func_champions(num, names)

with open(main_path + '\\out.txt', "w") as file:
    file.write(out)
os.startfile(main_path + '\\out.txt')
