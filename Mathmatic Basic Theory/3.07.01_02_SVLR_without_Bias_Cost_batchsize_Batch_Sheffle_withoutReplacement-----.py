# 3.03.01_SVLR_without_Bias_Cost.py와 비교해서 이제 Batch size에 대한 학습을 시킬것이다
# Batch Gradient Descent 에서 Shuffle을 적용하고 Replacement는 적용하지 않은 모델
# train data를 셔플하여 학습에 적용시킨다
# batch_size = data_size
# epochs 수가 곧 iterations 수이다

# import required modules
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

from dataset_generator import dataset_generator
import basic_nodes as nodes

np.random.seed(0)
plt.style.use('seaborn')

# dataset preparation
dataset_gen = dataset_generator()
dataset_gen.set_coefficient([5,0])
x_data, y_data = dataset_gen.make_dataset()
dataset_gen.dataset_visualizer()

# model part
node1 = nodes.mul_node()

# square error loss part
node2 = nodes.minus_node()
node3 = nodes.square_node()

# hyperparameter setting
epochs = 2 # total epoch setting
lr = 0.01 # learning rate setting

th = -1 # arbitary theta (=weight)
loss_list = []
th_list = []

for epoch in range(epochs):
    # train data를 랜덤으로 한번 shuffle 해주는 코드
    random_idx = np.arange(len(x_data))
    np.random.shuffle(random_idx)
    x_data = x_data[random_idx]
    y_data = y_data[random_idx]

    for data_idx in range(len(x_data)):
        x, y = x_data[data_idx], t_data[data_idx]

        z1 = node1.forward(th, x)
        z2 = node2.forward(y, z1)
        l = node3.forward(z2)

        dz2 = node3.backward(1)
        dy, dz1 = node2.backward(dz2)
        dth, dx = node1.backward(dz1)

        th = th - lr*dth

        th_list.append(th.item())
        loss_list.append(l.item())

fig, ax = plt.subplots(2, 1, figsize = (42,20))
ax[0].plot(th_list, linewidth = 5)
ax[1].plot(loss_list, linewidth = 5)
title_font = {'size':40, 'alpha':0.8, 'color':'navy'}
label_font = {'size':40, 'alpha':0.8}

ax[0].set_title(r'$\theta$', fontdict = title_font)
ax[1].set_title("Loss", fontdict = title_font)
ax[2].set_xlabel("Iteration", color = 'red', fontdict = label_font)
ax[0].tick_params(axis='both', which='major', labelsize=40)
ax[1].tick_params(axis='both', which='major', labelsize=40)