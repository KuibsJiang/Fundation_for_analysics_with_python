#文件需求：读取工作簿中的所有工作表
#1，在工作簿中筛选特定的行(销售额大于$2000.00的所有行)
#method2 pandas语句,数据框字典用于存储读取的所有工作表，键为工作表名称，值为包含工作表数据的数据框
#!/usr/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheet_name=None,index_col=None) #sheet_name=None一次性读取所有表
row_output = []
for worksheet_name,data in data_frame.items():
    row_output.append(data[data['Sale Amount'].astype(float)>2000.0])
filtered_rows = pd.concat(row_output,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer,sheet_name='sale_amount_gt2000',index=False)
writer.save()



