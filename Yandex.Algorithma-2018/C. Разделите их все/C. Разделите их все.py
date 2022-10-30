import os.path

main_path = os.path.dirname(os.path.abspath(__file__))
with open(main_path + '\\target.txt', 'r') as file_name:
    target = file_name.read().splitlines() # Получаем список

def func_split_targes(target):
    target_num = int(target.pop(0))+1
    if target_num <= 2:
        return 'Yes'
    x = []
    y = []
    for i in range(target_num-1):
        target_list = list(map(int, target[i].split()))
        if target_list[0] == 0:
            x.append(target_list[2])
            y.append(target_list[3])
        if target_list[0] == 1:
            x.append(target_list[1] + (target_list[5] - target_list[1])/2)
            y.append(target_list[2] + (target_list[6] - target_list[2])/2)
    for i in range(target_num-3):
        if (x[i+1]-x[i])*(y[i+2]-y[i])-(x[i+2]-x[i])*(y[i+1]-y[i]) != 0:
            return 'No'
    return 'Yes'

print(func_split_targes(target))
