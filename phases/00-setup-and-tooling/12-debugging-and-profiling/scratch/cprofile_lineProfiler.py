"""
When you need more than manual timers:
python -m cProfile -s cumtime train.py
"""

@profile
def train_step(model, data, target):
    output = model(data)
    loss = F.cross_entropy(output, target)
    loss.backward()
    return loss


# Run with: kernprof -l -v train.py
