#文件需求：读取工作簿中的一组工作表（部分）
#2，在这组工作表中筛选特定的行(1-2表中销售额大于$1900.0的行)
#method2 pandas语句
#!/usr/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
my_sheets = [0,1]
threshold = 1900.0
data_frame = pd.read_excel(input_file,sheet_name=my_sheets,index_col=None) #sheet_name=None一次性读取所有表
row_list = []
for worksheet_name,data in data_frame.items():
    row_list.append(data[data['Sale Amount'].astype(float)>threshold])
filterd_rows = pd.concat(row_list,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
filterd_rows.to_excel(writer,sheet_name='set_of_worksheets',index=False)
writer.save()