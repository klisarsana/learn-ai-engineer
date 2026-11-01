#!/usr/bin/env bash

for i in $(seq 1 100); do
    loss=$(echo "scale=4; 1/$i" | bc)

    echo "epoch $i loss: $loss"

    sleep 0.1
done > fake_train.log

# WSL at  klisarsana: 10-terminal-and-shell on  my-progress ❯ tail -5 fake_train.log
# epoch 96 loss: .0104
# epoch 97 loss: .0103
# epoch 98 loss: .0102
# epoch 99 loss: .0101
# epoch 100 loss: .0100

# WSL at  klisarsana: 10-terminal-and-shell on  my-progress ❯ grep "loss" fake_train.log
# menampilkan log dengat "loss" pada file log

# WSL at  klisarsana: 10-terminal-and-shell on  my-progress ❯ awk '{print $4}' fake_train.log
# menampilkan log dengan kolom keempat yang di pisahkan dengan spasi

# WSL at  klisarsana: 10-terminal-and-shell on  my-progress ❯ grep "loss" fake_train.log | tail -n 10 | awk '{print $4}'
# Mengambil 10 nilai loss terakhir

# WSL at  klisarsana: 10-terminal-and-shell on  my-progress ❯ grep "loss" fake_train.log | tail -n 10 | awk '{print "Epoch:", $2, "| Loss:", $4}'
# Epoch: 91 | Loss: .0109
# Epoch: 92 | Loss: .0108
# Epoch: 93 | Loss: .0107
# Epoch: 94 | Loss: .0106
# Epoch: 95 | Loss: .0105
# Epoch: 96 | Loss: .0104
# Epoch: 97 | Loss: .0103
# Epoch: 98 | Loss: .0102
# Epoch: 99 | Loss: .0101
# Epoch: 100 | Loss: .0100

