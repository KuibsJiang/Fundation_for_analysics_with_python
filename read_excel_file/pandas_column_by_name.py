#文件需求：选取特定的列(选取Customer ID，Purchase Date这两列)
#2种方法，使用列值索引和使用列标题
#method2 pandas语句
#!/usr/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'january_2013',index_col=None)
data_frame_column_by_name = data_frame.loc[:,['Customer ID','Purchase Date']]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer,'jan_2013_output',index=False)
writer.save()