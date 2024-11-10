import random, threading, time
from random import randint
class Bank(threading.Thread):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count = 100
        while count > 0:
            if self.lock.locked():
                count -= 1
                some_number = random.randint(50, 500)
                self.balance += some_number
                print(f"Пополнение: {some_number}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            else:
                count -= 1
            time.sleep(0.001)




    def take(self):
        count = 100
        while count > 0:
            if not self.lock.locked():
                count -= 1
                some_number = random.randint(50, 500)
                print(f"Запрос на {some_number}")
                if some_number <= self.balance:
                    self.balance -= some_number
                    print(f"Снятие: {some_number}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()
            else:
                count -= 1
            time.sleep(0.001)


bank = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bank,))
th2 = threading.Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')