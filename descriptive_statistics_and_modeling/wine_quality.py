#文件需求：葡萄酒质量的描述性统计
#计算出每列的总体描述性统计量、质量列中的唯一值以及这个唯一值对应的观测数量。
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as smf
from statsmodels.formula.api import ols,glm
#将数据集读取到pandas数据框中
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)#sep表示域分割符号为‘逗号’，head=0表示第一行为列标题
wine.columns = wine.columns.str.replace('','_')
print(wine.head())
#显示所有变量的描述性统计量
print(wine.describe())
#找出唯一值
print(sorted(wine.quality.unique()))
#计算值的频率
print(wine.quality.value_counts())