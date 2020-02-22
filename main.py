def playGame_MyVersion(rangeNumber, number, count):
    rangeNumber //= 2
    workNumber = rangeNumber
    while rangeNumber != number:
        print(rangeNumber);
        if (workNumber > 2):
            workNumber //= 2
        else:
            workNumber = 1;
        print("               ", workNumber);
        if (rangeNumber > number):
            rangeNumber -= workNumber
        else:
            rangeNumber += workNumber
        count+=1;
    return (count)

import numpy as np
count = 0                                     # счетчик попыток
rangeNumber = 100                             # задали диапазон
number = np.random.randint(1, rangeNumber)    # загадали число
print ("Загадано число от 1 до 99: ", number)
# запускаем
count = playGame_MyVersion(rangeNumber, number, count)
print("Алгоритм прошёл игру за количество попыток: ", count);