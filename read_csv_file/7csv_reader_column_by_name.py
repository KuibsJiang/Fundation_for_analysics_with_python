#文件需求：只保留表中发票号码和购买日期这2列。
#使用列标题
#method1 基础python语句

#!/usr/bin/env python3
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = ['Invoice Number','Purchase Date'] #创建列表变量，要保留的2列
my_columns_index = [] #创建空列表变量，填充保留列的索引值
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader,None)
        for index in range(len(header)):
            if header[index] in my_columns:
                my_columns_index.append(index) #for循环是为了获取保留列的索引值
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = [] #创建空值列表变量用于存放for循环后返回的‘有用’数据
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
                filewriter.writerow(row_list_output)
