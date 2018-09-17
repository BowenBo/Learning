'''
pyplot：用于绘制各类可视化图形的命令子库
'''
'''
import matplotlib.pyplot as plt引入
命令：
1、plt.plot(x, y ,format_string, **kwargs)
	x:x轴数据，列表或数组，可选
	y：y轴数据，列表或数组
	format_string：控制曲线的格式字符串，可选
		1、颜色字符''
			b蓝色
			g绿色
			r红色
			c青绿色
			m洋红色
			y黄色
			k黑色
			w白色
			#008000     RGB某颜色
			0.8         灰度值字符串
		2、风格字符
			-           实线
			--          破折线
			-.          点划线
			:           虚线
			''          无线条
		3、标记字符
			.           点标记
			，
			o
			v
			>
			<
			1
			2
			3
			4
			s
			p
			*
			h
			H
			+
			x
			D
			d
			|
	**kw：第二组或更多（x,y,format_string）
		绘制1条曲线时可以省略x，只写一个列表代表y轴数据
		绘制多条曲线是不能省略
2、plt.show()显示图像
3、plt.savefig('text',dpi = )保存图片
4、plt.axis([x0, xn, y0, yn])坐标尺度，4个参数分别是x、y轴的起点和终点
5、plt,subplot(nrows,ncos,plot_number)绘图区分区命令，逗号可以去掉
	nrows:将绘图区分为的行数
	ncos:将绘图区分为的列数
	plot——number绘图所在的区域

'''

import matplotlib.pyplot as plt
import numpy as np
a = np.arange(10)
print(a)
# plt.subplot(324)
plt.plot(a, a * 1.5, '1', a, a * 2, a, a * 3.5, a, a * 4.5)
plt.show()

'''
6、matplotlib.rcParams(font.family, font.style, font.size) 默认不支持中文显示，需要次函数修改字体。
	family：字体名字
		Simhei黑体
	style：正常normal，斜体：italic
	size:大小
	例如：
	.rcParams['font.family'] = 'Simhei'
	.rcParams['font.size'] = 20
'''