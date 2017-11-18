#为表格中的所有列添加列标题行
#method2 pandas语句

#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
header_list= ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
data_frame = pd.read_csv(input_file,header=None,names= header_list) #pd的read_csv函数可直接指定输入文件不包含标题行，并且可直接提供标题行列表
data_frame.to_csv(output_file,index=False)