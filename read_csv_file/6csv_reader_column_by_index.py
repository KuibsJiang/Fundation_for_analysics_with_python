#在csv文件中选取特定的列的2种通用方法
#使用列索引值 适用于索引值易识别，或者处理多个输入文件时，列位置不发生变化
#使用列标题   适用于列标题易识别，或者处理多个输入文件时，列位置发生变化，但标题不变

#文件需求：只保留表中供应商的姓名和成本这2列。
#使用列索引值
#method1 基础python语句

#!/usr/bin/env python3
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0,3] #创建一个列表变量，包含想要保留的列索引值
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index in my_columns:
                row_list_output.append(row_list[index])
                filewriter.writerow(row_list_output)
