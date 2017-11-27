#文件需求：处理多个工作簿，工作表计数，每个表的行列计数
#method1，基础python语句
#!/usr/bin/env python3

import sys
import glob
import os
from xlrd import open_workbook
input_directory = sys.argv[1]
workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory,'*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook:%s' % os.path.basename(input_file))
    print('Number of worksheets:%d' % workbook.nsheets)
    for worksheet in workbook.sheets():
        print('Workshseet name:',worksheet.name,'\tRows',worksheet.nrows,'\tColumns',worksheet.ncols)
    workbook_counter += 1
print('Number of Excel workbooks: %d' % (workbook_counter) )