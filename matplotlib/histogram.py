#文件需求：创建频率分布直方图
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
mu1,mu2,sigma = 100,130,15
x1 = mu1 + sigma*np.random.randn(10000) #随机生成器穿件正态分布变量，均值为100
x2 = mu2 + sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
n,bins,patches = ax1.hist(x1,bins= 50,normed=False,color='darkgreen') #bin=50表示每个变量被分成50份，normed=False表示是频率分布不是概率密度
n,bins,patches = ax1.hist(x2,bins=50,normed=False,color='orange',alpha= 0.5) #alpha表示透明
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Value in Bin')
fig.suptitle('Histograms',fontsize=14,fontweight='bold')
ax1.set_title('Two Frequency Distributions')
plt.savefig('histogram.png',dpi=400,bbox_inches='tight')
plt.show()