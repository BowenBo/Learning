import numpy as np
#.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ',
# encoding=None)
'''
fname:file name
X：需要存入的数组
fmt：存入文件的格式
delimiter：字符串分割符，默认空格
newline：默认换行
'''
#2、loadtxt
'''
.loadtxt(fname, dtype=float, comments='#', delimiter=None,converters=None, skiprows=0, usecols=None, unpack=False,ndmin=0, encoding='bytes')
'''

a = np.arange(100).reshape((10, 10))
# print(a, a.ndim)
np.savetxt(r'/Users/bowen/PycharmProjects/数据分析/Numpy/1.csv', a, delimiter = ',', fmt = '%d')

print(np.loadtxt(r'/Users/bowen/PycharmProjects/数据分析/Numpy/1.csv', delimiter = ',', dtype = int, unpack = False))
