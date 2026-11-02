import torch


def debug_print(name, tensor):
    print(
        f"  {name}: shape={tensor.shape}, dtype={tensor.dtype}, "
        f"device={tensor.device}, "
        f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}, "
        f"mean={tensor.mean().item():.4f}, "
        f"has_nan={tensor.isnan().any().item()}"
    )


def demo_debug_print():
    print("=== Print Debuggin for Tensors ===")
    x = torch.randn(32, 784)
    debug_print("input batch", x)

    w = torch.randn(784, 128)
    out = x @ w
    debug_print("after matmul", out)

    with_nan = out.clone()
    with_nan[0, 0] = float("nan")
    debug_print("with injected Nan", with_nan)

demo_debug_print()