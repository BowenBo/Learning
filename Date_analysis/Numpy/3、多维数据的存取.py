import numpy as np
a = np.arange(100).reshape((2, 5, 10))#三维，第一维2个元素，第2维5个元素，第3维10个元素
# print(a)

#1、 a.tofile(frame, sep = '', format ='%s')
a.tofile(r'/Users/bowen/PycharmProjects/数据分析/Numpy/a.dat', sep = ',',format = '%d')
'''
生成一个由，分割的数据文件，没有维度信息(元信息）
'''

#2、 a.fromfile(frame, dtype =float, count = -1, sep = '')
'''
dtype读取数据的类型
count读入元素的个数，-1表示整个文件
'''
b = np.fromfile(r'/Users/bowen/PycharmProjects/数据分析/Numpy/a.dat', sep = ',',dtype = int).reshape((2, 5, 10))
#取出时要知道原存入数据的维度，用reshape来还原，除非在tofile中存入元信息
# print(b)

#3、np.save(fname, array)或np.savez（fname, array）
'''
fname以npy为扩展名，压缩扩展名为npz
此类文件存储来数据的元信息，包括维度、类型等，在读取是会还原
'''
#4、np.load(fname)

np.save('a.npy', a)
c = np.load('a.npy')
print(c)