def my_range(start, stop):
    while True:
        if start > stop:
            raise StopIteration
        yield start
        start += 1

r = my_range(1, 8)
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
