import time
import threading
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for number in range(1,word_count+1):
            file.write(f"Какое-то слово №{number}\n")
            time.sleep(0.1)
        return f"Завершилась запись в файл {file_name}"
def thread_function(word_count, file_name):
    print(write_words(word_count, file_name))
param_1 = [(10, 'example1.txt'),(30, 'example2.txt'),(200, 'example3.txt'),(100, 'example4.txt')]
time_start1 = time.time()

for word_count, file_name in param_1:
    print(write_words(word_count, file_name))
time_end1 = time.time()
total_time1 = time_end1-time_start1
total_time1_str = (time.strftime("%H:%M:%S", time.gmtime(total_time1)) +
                   f".{int((total_time1 % 1) * 1000000):06}")
print(f"Работа потоков {total_time1_str} секунд")

param_2 = [(10, 'example5.txt'),(30, 'example6.txt'),(200, 'example7.txt'),(100, 'example8.txt')]
time_start2 = time.time()
threads = []
for word_count, file_name in param_2:
    thread = threading.Thread(target=thread_function, args=(word_count, file_name))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
time_end2 = time.time()
total_time2 = time_end2-time_start2
total_time2_str = (time.strftime("%H:%M:%S", time.gmtime(total_time2)) +
                   f".{int((total_time2 % 1) * 1000000):06}")
print(f"Работа потоков {total_time2_str} секунд")
