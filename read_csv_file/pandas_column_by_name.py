#文件需求：只保留表中发票号码和购买日期这2列。
#使用列标题
#method1 pandas语句

#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:,['Invoice Number','Purchase Date']]
data_frame_column_by_name.to_csv(output_file,index=False)