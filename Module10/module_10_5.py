import time, multiprocessing

def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()
    return all_data
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # # Линейный вызов
    # start_time = time.perf_counter()
    # for filename in filenames:
    #     read_info(filename)
    # linear_time = time.perf_counter() - start_time
    # print(f"Линейный: {linear_time}")

    # Многопроцессный вывод
    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.perf_counter() - start_time
    print(f"Многопроцессный: {multiprocessing_time}")
