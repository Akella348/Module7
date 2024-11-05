def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results
# def __min__(int_list): Эти функции я зачем-то расписал, а потом понял, что они и так сработают, без переопределения
#     minimum = int_list[0]
#     for item in int_list:
#         if item < minimum:
#             minimum = item
#     return minimum
# def __max__(int_list):
#     maximum = int_list[0]
#     for item in int_list:
#         if item > maximum:
#             maximum = item
#     return maximum
# def __len__(int_list):
#     count = 0
#     for item in int_list:
#         count += 1
#     return count
# def __sum__(int_list):
#     summary = 0
#     for item in int_list:
#         summary += item
#     return summary
# def __sorted__(int_list):
#     return sorted(int_list)
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))