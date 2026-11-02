# CPU Memory with tracemalloc
import tracemalloc

tracemalloc.start()

# your code here
model = build_model()
data = load_dataset()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
for stat in top_stats[:10]:
    print(stat)

# CPU Memory with memory_profiler
from memory_profiler import profile


@profile
def load_data():
    raw = read_csv("data.csv")
    processed = preprocess(raw)
    return processed


# GPU Memory with Pytorch
import torch

if torch.cuda.is_available():
    print(torch.cuda.memory_summary)
    print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
    print(f"Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")
