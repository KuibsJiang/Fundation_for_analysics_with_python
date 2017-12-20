#文件需求：创建seaborn各种统计图
#!/usr/bin/env python3
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
sns.set(color_codes=True)
#直方图
x = np.random.normal(size=100)
sns.distplot(x,bins=20,kde=False,rug=True,label='Histogram w/o Density')
sns.axlabel('Value','Frequency')
plt.title('Histogram of a Random Sample from a Normal Distribution')
plt.legend()
#带有回归直线的散点图和单变量直方图
mean,cov = [5,10],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
data_frame = pd.DataFrame(data,columns=['x','y'])
sns.jointplot(x='x',y='y',data=data_frame,kind='reg').set_axis_labels('x','y')
plt.suptitle('Joint Plot of Two Variables with Bivariabte and Graphs')
#成对变量之间的散点图与单变量直方图
iris = sns.load_dataset('iris')
sns.pairplot(iris)
#按照某几个变量生成的箱线图
tips = sns.load_dataset('tips')
sns.factorplot(x='time',y='total_bill',hue='smoker',col='day',data=tips,kind='box',size=4,aspect=.5)
#带有bootstrap置信区间的线性回归模型
sns.lmplot(x='total_bill',y='tip',data=tips)
#带有bootstrap置信区间的逻辑斯蒂回归模型
tips['big_tip'] = (tips.tip/tips.total_bill)>.15
sns.lmplot(x='total_bill',y='big_tip',data=tips,logistic=True,y_jitter=.03).set_axis_labels('Total Bill','Big Tip')
plt.title('Logistic Regression of Big Tip vs. Total Bill')
plt.show()
savefig('seaborn_plots.png')