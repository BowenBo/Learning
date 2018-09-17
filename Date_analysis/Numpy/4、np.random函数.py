import numpy as np
#np.random函数的子库np.random.
'''
最基本的4个
.randn(do, d1, ```dn)        do到dn创建随机数数组，符合标准正态分布 
.rand(do, d1, ```dn)         do到dn创建随机数数组，[0,1)，均匀分布，浮点数
.randint(low, [,high,shape]) 按shape创建随机数或整数数组，范围[low,high)
.seed(s)        随机数的种子，s是给定的种子值
'''

'''
3个高级函数
.shuffle(a)根据数组a的第1轴进行乱序排列，改变数组
.permutation(a)根据数组a的第1轴产生一个新的乱序数组，不改变数组
.choice(a[,size,replace，p])从一维数组a中以概率p抽取元素，形成size形状新数组，replace表示是否可以重复选取同一元素，false不可重复
'''

'''
3个分布的随机数函数
.uniform(low,high,shape)，等概率选取，产生具有均匀分布的数组
.normal（loc,scale,shape),loc为均值，scale为标准差，具有正态分布的数组
.poisson(lam, shape),lam为随机事件发生率，产生具有柏松分布的数组
'''

'''
5个统计函数
sum（a, axis = none)
mean()
average()
std()
var()
'''
a = np.random.randint(1, 100)
print(a)
b = np.random.choice(a, size = (3, 4), replace = False)
print(b)