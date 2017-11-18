#文件需求：只保留表中供应商的姓名和成本这2列。
#使用列索引值
#method2 pandas语句

#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:,[0,3]] #iloc函数根据索引位置选取列
data_frame_column_by_index.to_csv(output_file,index = False)