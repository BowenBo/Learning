#NumPy库
'''
提供一个强大的N维数组对象ndarray
提供一个广播功能的函数
整合C、C++、Fortran代码的工具
提供线性代数、傅立叶变换、随机数生成等功能
轴表示数据的维度
秩表示轴的数量，也就是这个数组类型有多少个维度
'''
#引入库
'''import numpy as np'''
#生成
'''
1、从列表或元组等类型创建ndarray数组
	numpy.array(object, dtype = None, copy = True, order = 'K', subok = False, ndmin = 0)
	elements:
		object:任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列
		dtype 数组的所需数据类型，可选
		copy 可选，默认为true，对象是否被复制
		order C（按行）、F（按列）或A（任意，默认）
		subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类
		ndmin 指定返回数组的最小维数
 
2、函数创建
	.arange(x, y ,j)：创建由x到y，以j为步长的数组
	.ones((m,n),dtype)：创建m行n列的全1数组，dtype是数据类型
	.zeros((m,n),dtype)：创建m行n列的全0数组，dtype是数据类型
	.empty((m,n),dtpye):数组
	.full(shape,val)，每个元素值都是value
	.eye(n):n*n单位矩阵，对角线为1，其余为0的数组
	.ones_like(a)
	.zeros_like(a)
	.full_like(a):根据a的形状生成一个全是value元素的数组
3、使用其它函数创建
	np.linspace(起，止，数据数量)根据起止值等间距第填充数据，形成数组
	np.concatenate(a,b)将两个或多个数组合并成一个新的数组
'''
#5个ndarray对象属性
'''
.ndim：秩，即轴的数量
.shape：对象的尺度
.size：对象元素的个数
.dtype：对象元素类型
.itemsize：对象中每个元素的大小，以字节为单位
'''
#ndarray元素类型
'''
bool
inte
intp
int8
int12
int32
int64
uint8
uint16
uint32
uint64
float16
float32
float64
complex64
complex128
'''
#ndarray数组的维度变换
'''
.reshape(shape)不改变数组元素，返回一个shape形状的数组，原数组不变
.resize(shape)与上一个功能一样，但修改来原来数组
.swapases(ax1,ax2)将数组中的两个维度进行调换
.flatten()对数组进行降维，返回一个一维数组，原数组不变
'''
import numpy
a = numpy.zeros((3, 4))
b = numpy.array([[12,33],[22,44]])
print(b)
