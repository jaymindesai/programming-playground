
def bubble_sort(alist):
    passes = len(alist) - 1
    exchanges = True
    while passes > 0 and exchanges:
        exchanges = False
        for i in range(passes):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passes -= 1
    return alist

l = [5, 3, 4, 1, 100]

print(bubble_sort(l))