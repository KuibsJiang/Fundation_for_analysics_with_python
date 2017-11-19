#文件需求：计算多个文件中每个文件某一列的总和与均值
#method1 基础python语句

#!/usr/bin/env python
import sys
import csv
import os
import glob

input_path = sys.argv [1]
output_file = sys.argv[2]
output_file_header_list = ['file_name','total_sales','average_sales']
csv_out_file = open(output_file,'a',newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_file_header_list) #先将手动创建的列标题行添加到输出文件
for input_file in glob.glob(os.path.join(input_path ,'sales_*')):
    with open(input_file ,'r',newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader) #将每个输入文件的第一行除去
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',',''))
            number_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()
