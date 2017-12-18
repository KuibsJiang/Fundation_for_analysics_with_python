#文件需求：创建垂直条形图：
#!/usr/bin/env python3
import matplotlib.pyplot as plt
plt.style.use('ggplot') #使用R语言绘图包ggplot2的风格
customers = ['ABC','DEF','GHI','JKL','MNO']
customers_index = range(len(customers))
sale_amounts = [127,90,201,111,232]
fig = plt.figure() #使用matplotlib绘图时，需先创建一个基础图，然后再创建一个或多个子图。
ax1 = fig.add_subplot(1,1,1) #基础图中添加的一个子图，（1,1,1）表示ax1为1行1列的基础图中的第一个子图。
ax1.bar(customers_index,sale_amounts,align='center',color='darkblue') #括号中的4个分别表示设置条形左侧在X轴上的坐标，高度，条形与标签中间对齐，颜色
ax1.xaxis.set_ticks_position('bottom') #设置x轴的刻度线位置
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index,customers,rotation=0,fontsize='small')#刻度标签更改，rotation表示0倾斜度，水平，fontsize字体大小
plt.xlabel('Customer Name') #x轴的标签
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer') #图形的标题
plt.savefig('bar_plot.png',dpi=400,bbox_inches='tight') #保存图形，一些设置参数
plt.show()