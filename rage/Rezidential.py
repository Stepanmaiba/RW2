import random
import numpy as np
from rage.Building import Building


class Rezidential (Building):

    # Вывод даных
    def info_rezidential_(self):
        print ("Данные по квартире: ")
        return '\n'

    # Вывод периметра и площади
    def size_residential(self):
        residential_1 = 1
        length = np.empty(residential_1)
        width = np.empty(residential_1)
        for i in range(residential_1):
            length[i] = random.randint(1, 10)
            width[i] = random.randint(1, 10)
            print("Длинна кухни: ", length[i], " ширина кухни: ", width[i])
            print('Периметр:', length[i] * length[i])

        residential_2 = 1
        length = np.empty(residential_2)
        width = np.empty(residential_2)
        for i in range(residential_2):
            length[i] = random.randint(1, 10)
            width[i] = random.randint(1, 10)
            print("длинна гостинной: ", length[i], " ширина гостинной: ", width[i])
            print('Периметр:', length[i] * length[i])

        print('Общая площадь квартры: ' + str(np.dot(length, width)))
        name = {1: 'Дорофеев Клим Авксентьевич', 2: 'Шестаков Илья Дмитриевич', 3: 'Григорьева Ира Лукьяновна'}
        for i in name:
            print(name[i])

        return '/n'
