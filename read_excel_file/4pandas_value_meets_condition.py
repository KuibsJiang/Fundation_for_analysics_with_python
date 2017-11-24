#文件需求：筛选出特定行(选出sale amount大于1400的行)
#3种方法，行中的值满足某个条件，行中的值属于某个集合，行中的值满足某个正则表达式

#method2 pandas语句
#!/usr/bin/env python3

import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheetname='january_2013',index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float)>1400.0]
write = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(write,sheet_name='jan_13_output',index=False)
write.save()