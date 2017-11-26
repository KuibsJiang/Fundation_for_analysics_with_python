#文件需求：筛选出购买日期在集合（01/24/2013和01/31/2013)中的行
#3种方法，行中的值满足某个条件，行中的值属于某个集合，行中的值满足某个正则表达式

#method2 pandas语句  isin函数
#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'january_2013',index_col=None)
important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['PurchaseDate'].isin(important_dates)]
write = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(write,'janu_2013_output',index=False)
write.save()