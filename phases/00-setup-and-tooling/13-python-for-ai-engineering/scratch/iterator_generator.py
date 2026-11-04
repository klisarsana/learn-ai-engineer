numbers = [10, 20, 30]
it = iter(numbers)
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("no more items")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(type(gen).__name__)
print(list(gen))
print(list(gen))

import os
import tempfile

def read_rows(path):
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split(",")
        for line in fh:
            yield dict(zip(header, line.rstrip("\n").split(",")))

with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "rows.csv")
    with open(path, "w", encoding="utf=8") as fh:
        fh.write("x,label\n")
        fh.writelines(f"{i*0.5}, {i % 2}\n" for i in range(5))
    rows = read_rows(path)
    print(next(rows))
    print(sum(1 for _ in rows))

import sys

as_list = [i*i for i in range(1_000_000)]
as_generator = (i*i for i in range(1_000_000))
print(sys.getsizeof(as_list), sys.getsizeof(as_generator))
print(sum(as_list) == sum(as_generator))