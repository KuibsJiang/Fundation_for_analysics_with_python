#文件需求：筛选出购买日期在集合（01/24/2013和01/31/2013)中的行
#3种方法，行中的值满足某个条件，行中的值属于某个集合，行中的值满足某个正则表达式

#method1 基础python语句
#!/usr/bin/env python3
import sys
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
from datetime import date
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook
output_worksheet = output_workbook.add_sheet('jan_2013_output')
import_date = ['01/24/2013','01/31/2013']
purchase_date_column_index = 4
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index,purchase_date_column_index),workbook.datemode)
        purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/% Y')
        row_list = []
        if purchase_date in import_date:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,column_index)
                cell_type = worksheet.cell_type(row_index,column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                     row_list.append(cell_value)
    if row_list:
        data.append(row_list)
for list_index,output_list in enumerate(data):
    for element_index,element in enumerate(output_list):
        output_worksheet.write(list_index,element_index ,element)
output_workbook.save(output_file)