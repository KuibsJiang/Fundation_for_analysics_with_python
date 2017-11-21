#文件需求：读取工作簿中的一张表
#method1 基础python语句
#!/usr/bin/env python3

import sys
from xlrd import open_workbook #导入的是方法
from xlwt import Workbook #导入的是对象

input_file = sys.argv[1]
output_file = sys.argv[2]
out_workbook = Workbook() #在with语句后会发现需要输出，所以先创建一个输出文件对象
out_worksheet = out_workbook.add_sheet('jan_2013') #创建输出文件的表
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013') #该方法引用工作表
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            out_worksheet.write(row_index,col_index,worksheet.cell_value(row_index,col_index))
out_workbook.save(output_file) #记得保存



