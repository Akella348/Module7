import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        print(f"{self.name}, на нас напали!")
        days_gone = 0
        time_gone = 0
        enemy = 100
        while enemy > 0:
            step = 0.4 # шаг
            time.sleep(step)  # решил сделать шаг отличный от 1 секунды, а 1 секунде присвоить день
            time_gone += step  # счетчик времени дополняется шагом
            enemy -= self.power
            enemy = max(enemy, 0)  # ограничитель, чтобы меньше 0 не было
            if time_gone > 1:  # как только проходит день
                time_gone -= 1  # счетчик времени сбрасывается на день
                days_gone += 1  # счетчик дней дополняется днем
                print(f'{self.name} сражается {days_gone} день(дня), осталось {enemy} воинов')
        else:
            print(f'{self.name} одержал победу спустя {days_gone} день(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()