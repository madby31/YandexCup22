while True:
    data = input("Введите время:\n")
    try:
        hours, minutes = data.split()
        if hours.isdigit() and hours.isdigit():
            hours = int(hours); minutes = int(minutes)
            if (11>=hours>=0) and (59>=minutes>=0):
                break
        # print('Время введено неправильно!')
    except:
        pass
    print('Время введено неправильно!')
if hours==0:
    hours_out = 0
else:
    hours_out = 12-hours
if minutes==0:
    minutes_out = 0
else:
    minutes_out = 60-minutes
print(hours_out,minutes_out)
