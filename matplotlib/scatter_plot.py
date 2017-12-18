#文件需求：创建散点图，并在各点间发一条回归曲线
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = np.arange(start=1.,stop=15.,step=1.)
y_linear = x + 5 * np.random.randn(14) #使数据和线性（直线）偏离
y_quadratic = x **2 + 10 * np.random.randn(14) #使数据和二次曲线偏离
fn_linear = np.poly1d(np.polyfit(x,y_linear,deg=1)) #根据拟合的线生成方程式
fn_quadratic = np.poly1d(np.polyfit(x,y_quadratic,deg=2))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x,y_linear,'bo',x,y_quadratic,'go',x,fn_linear(x),'b-',x,fn_quadratic(x),'g-',linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Scatter plots Regression Lines')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim((min(x)-1.,max(x)+1.)) #设置xy轴范围
plt.ylim((min(y_quadratic)-10.,max(y_quadratic)+10.))
plt.savefig('scatter_plot.png',dpi=400,bbox_inches='tight')
plt.show()