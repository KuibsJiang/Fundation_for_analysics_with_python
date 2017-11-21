#文件需求：读取工作簿中的一张表
#method2 pandas语句
#!/usr/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheetname='january_2013')
write = pd.ExcelWriter(output_file)
data_frame.to_excel(write,sheet_name='jan_2013',index=False)
write.save()