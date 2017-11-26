#文件需求：筛选出客户姓名以大写字母J开头的行
#3种方法，行中的值满足某个条件，行中的值属于某个集合，行中的值满足某个正则表达式

#method2 pandas语句
#!/usr/bin/env python3  函数startswith/endswith/match/search
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'january_2013',index_col=None)
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith('J')]
writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer,'jan_2013_output',index=False)
writer.save()
