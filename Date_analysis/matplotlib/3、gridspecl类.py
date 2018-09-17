import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
gs = gridspec.GridSpec(3, 3)        #分区3*3
ax1 = plt.subplot(gs[0, : ])        #横向选中0行，纵向所有列
ax2 = plt.subplot(gs[1, : 2])       #第1行，从第0列到第1列
ax3 = plt.subplot(gs[1 :, -1])      #最后1列，第1行到最后一行
ax3 = plt.subplot(gs[2, 0])         #第2行，第0列
ax3 = plt.subplot(gs[2, 1])         #第2行，第1列