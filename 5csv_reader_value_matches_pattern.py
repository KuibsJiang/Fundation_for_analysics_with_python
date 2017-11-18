#当行中的值匹配某个表达式（正则表达式）
#文件需求1：筛选出发票以001开头的行
#method1 python语句

#!/usr/bin/env python3
import sys
import csv
import re #导入正则表达式模块
input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)',re.I) #re的compile（编写）函数，r表示将单引号中间的数据按原始字符串处理，re.I是不区分大小写
with open(input_file,'r',newline='') as csv_in_file: #^001-.*中^表示只在开头搜索，句点.可以匹配除换行符外的任意字符，*表示重复任意次
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number): #在invoice_number的值中寻找模式
                filewriter.writerow(row_list)