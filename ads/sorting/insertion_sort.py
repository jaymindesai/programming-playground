
def insertion_sort(alist):
    for i in range(1, len(alist)):
        index = i
        value = alist[index]
        while index > 0 and value < alist[index-1]:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = value
    return alist

l = [5, 3, 4, 1, 100]

print(insertion_sort(l))

