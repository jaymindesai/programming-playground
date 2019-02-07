from timeit import Timer

t1 = """
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
test1()
"""

t2 = """
def test2():
    l = []
    for i in range(1000):
        l.append(i)
test2()
"""

t3 = """
def test3():
    l = [i for i in range(1000)]
test3()
"""

t4 = """
def test4():
    l = list(range(1000))
"""

from timeit import timeit

print(round(timeit(t1, number=1000), 4))
print(round(timeit(t2, number=1000), 4))
print(round(timeit(t3, number=1000), 4))
print(round(timeit(t4, number=1000), 4))

# def empty():
#     pass
#
# t0 = Timer("empty()", "from __main__ import empty")
# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000) - t0.timeit(number=1000), "milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000) - t0.timeit(number=1000), "milliseconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000) - t0.timeit(number=1000), "milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000) - t0.timeit(number=1000), "milliseconds")
