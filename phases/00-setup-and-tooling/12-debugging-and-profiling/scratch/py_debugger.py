import torch


def training_step(model, batch, criterion, optimizer):
    inputs, labels = batch
    outputs = model(input)
    loss = criterion(outputs, labels)

    if loss.item() > 100 or torch.isnan(loss):
        breakpoint()

    loss.backward()
    optimizer.step()


def demo_conditional_breakpoint():
    print("\n--- 10. Conditional Breakpoint Pattern ---")
    print("  In real code, use this pattern:")
    print()
    print("    for step in range(num_steps):")
    print("        loss = train_step(model, batch)")
    print("        if loss.item() > 10 or torch.isnan(loss):")
    print("            breakpoint()  # drops into pdb")
    print()
    print("  Useful pdb commands once inside:")
    print("    p tensor.shape       # print shape")
    print("    p tensor.device      # check device")
    print("    p tensor.grad        # inspect gradients")
    print("    p tensor.isnan().sum()  # count NaNs")
    print("    c                    # continue execution")
    print("    q                    # quit debugger")

demo_conditional_breakpoint()