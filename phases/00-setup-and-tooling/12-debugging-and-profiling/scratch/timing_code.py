import time

import torch


class Timer:
    def __init__(self, name=""):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] {elapsed:.4f}s")


def demo_timing():
    with Timer("Matrix multiply 1000x1000"):
        a = torch.randn(1000, 1000)
        b = torch.randn(1000, 1000)
        _ = a @ b

    with Timer("Matrix multiply 5000x5000"):
        a = torch.randn(5000, 5000)
        b = torch.randn(5000, 5000)
        _ = a @ b


demo_timing()
