import os.path

def func_even(letters,size):
    list_palindroms = []
    if size % 2 == 0:
        even_key = True
    else:
        even_key = False
    for ind in range(len(letters)-size):
        right = 0
        s_size = size
        for index in range(size//2):
            if even_key == True:
                if letters[ind+index] == letters[ind+index+s_size]:
                    right += 1
                s_size = size // 2
            else:
                if letters[ind + index] == letters[ind - index + size]:
                    right += 1
        if right == size // 2:
            list_palindroms.append([letters[vol] for vol in range(ind, ind+size+1)])
    return list_palindroms

def func_test_palindroms(out):
    best_choice = ['z' for i in range(len(out[0]))]
    for listof in out:
        if listof <= best_choice:
            best_choice = listof
    return ''.join(best_choice)

main_path = os.path.dirname(os.path.abspath(__file__))
with open(main_path+'\\string.txt', 'r') as file_name:
    letters = list(file_name.read().split())

size = 2
while True:
    out = func_even(letters,size)
    if not out:
        size += 1
    else:
        print(func_test_palindroms(out))
        break
    if len(letters)/2 < size:
        print(-1)
        break
