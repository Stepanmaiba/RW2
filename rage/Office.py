import random
import numpy as np
from rage.Building import Building


class Office (Building):

    #Вывод даных
    def info_office(self):
        print  ("Данные по офису: ")
        return '\n'

    #Вывод периметра и площади
    def size_office(self):
        office_1 = 1
        length = np.empty(office_1)
        width = np.empty(office_1)
        for i in range(office_1):
            length[i] = random.randint(1, 15)
            width[i] = random.randint(1, 15)
            print("Длинна комнаты №1:", length[i], " ширина комнаты №1:", width[i])
            print('Периметр:', length[i] * length[i])

        office_2 = 1
        length = np.empty(office_2)
        width = np.empty(office_2)
        for i in range(office_2):
            length[i] = random.randint(1, 15)
            width[i] = random.randint(1, 15)
            print("Длинна комнаты №2:", length[i], " ширина комнаты №1:", width[i])
            print('Периметр:', length[i] * length[i])

        print('Общая площадь офисса:' + str(np.dot(length, width)))
        name = {1: 'Фролов Антон Степанович', 2: 'Фролов Степан Адольфович', 3: 'Фролова Лана Альбертовна'}
        for i in name:
            print(name[i])

        return '/n'

