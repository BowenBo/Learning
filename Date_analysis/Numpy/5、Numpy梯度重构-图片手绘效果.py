'''
depth = 10          预设深度值，范围0-100
grad = np.gradient（a）
grad_x, grad_y = grad   #提取x和y方向的梯度值
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100       根据深度调整x和y方向的梯度值

'''