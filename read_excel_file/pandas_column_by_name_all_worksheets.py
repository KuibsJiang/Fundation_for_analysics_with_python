#文件需求：读取工作簿中的所有工作表
#2，在工作簿中筛选特定的列(基于列标题选取Customer Name和Sale Amount列)
#method2 pandas语句
#!/usr/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheet_name=None,index_col=None) #sheet_name=None一次性读取所有表
column_output = []
for worksheet_name,data in data_frame.items():
    column_output.append(data.loc[:,['Customer Name','Sale Amount']])
selected_columns = pd.concat(column_output,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer,sheet_name='selected_columns_all_worksheets',index=False)
writer.save()