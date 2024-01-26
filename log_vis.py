import os
import matplotlib.pyplot as plt

name = 'char_str_patch4_3_32_128-Seed226'
log_path = './save/{}/log_train.txt'.format(name)

f = open(log_path, 'r')
train_loss_list = []
valid_loss_list = []
valid_acc_list = []
while True:
    line = f.readline()
    if not line: break
    if 'loss' in line:
        split = line.split(',')
        train_loss = float(split[1][13:])
        valid_loss = float(split[2][13:])

        train_loss_list.append(train_loss)
        valid_loss_list.append(valid_loss)
    if 'char_accuracy' in line:
        split = line.split(',')
        valid_acc = float(split[0][19:])
        valid_acc_list.append(valid_acc) 
f.close()


plt.plot(range(1,len(train_loss_list)+1),train_loss_list,label = 'train loss')
plt.plot(range(1,len(valid_loss_list)+1),valid_loss_list,label = 'valid loss')
plt.legend()
plt.savefig('loss.png')
print("compliete")
