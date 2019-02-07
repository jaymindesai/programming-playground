
def _partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[first], alist[right] = alist[right], alist[first]
    return right

def _quick(alist, first, last):
    if first < last:
        split = _partition(alist, first, last)
        _quick(alist, first, split - 1)
        _quick(alist, split + 1, last)
    return alist

def quick_sort(alist):
    return _quick(alist, 0, len(alist) - 1)

l = [5, 3, 1, 4, 100]

print(quick_sort(l))