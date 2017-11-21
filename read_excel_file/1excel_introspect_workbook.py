#文件需求：工作簿内省，获取工作簿的表数目、每张表的数据量和数据类型等
# #!/usr/bin/env python3

import sys
from xlrd import open_workbook

input_file = sys.argv[1]
workbook = open_workbook(input_file)
print('Number of Worksheets:',workbook.nsheets) #workbook.nsheets表示的是工作簿中表的数量
for worksheet in workbook.sheets(): #workbook.sheets()是捆绑的方法
    print('worksheet name:',worksheet.name,'\trows:',worksheet.nrows,'\tcolumns:',worksheet.ncols)