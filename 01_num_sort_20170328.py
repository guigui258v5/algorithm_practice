import time
import random

l = []
num = int(input('数据范围为:'))
# 生成随机列表
time0 = time.time()

for i in range(int(num*0.6)):
    a = random.randint(0,num-1)
    if a not in l:
        l.append(a)

time1 = time.time()

# 位图排序
time4 = time.time()
l2 = [0 for x in range(num)]
l3 = []

for item in l:
    l2[item] = 1

for i,item in enumerate(l2):
    if item == 1:
       l3.append(i)
time5 = time.time()

# 系统排序
time2 = time.time()
l.sort()
time3 = time.time()

print('-'*100)
print('生成随机数耗时%.2f秒'%(time1-time0))
print('系统排序耗时%f秒'%(time3-time2))
print('位图排序耗时%f秒'%(time5-time4))
print('-'*100)
