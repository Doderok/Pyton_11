def bubble_sort(l):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l) - 1):
            if (l[i] > l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True


random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)