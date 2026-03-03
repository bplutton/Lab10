def sequential_search(a_list, target):
    for i in range(len(a_list)):
        if a_list[i] == target:
            return "Found"


def binary_search(a_list, target):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == target:
            return "Found"


def sequential_search_counted(a_list, target):
    count = 0
    for i in range(len(a_list)):
        count += 1
        if a_list[i] == target:
            return "Found", count


def binary_search_counted(a_list, target):
    low = 0
    high = len(a_list) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1
        if a_list[mid] == target:
            return "Found", count
