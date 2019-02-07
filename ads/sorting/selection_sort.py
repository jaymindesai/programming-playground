
def selection_sort(alist):
    length = len(alist)
    for slot in range(length - 1, 0, -1):
        index_max = 0
        for current_index in range(1, slot + 1):
            if alist[current_index] > alist[index_max]:
                index_max = current_index
        alist[slot], alist[index_max] = alist[index_max], alist[slot]
    return alist

l = [5, 3, 4, 1, 100]

print(selection_sort(l))