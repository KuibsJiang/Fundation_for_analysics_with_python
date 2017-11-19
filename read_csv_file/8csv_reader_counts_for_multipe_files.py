#文件需求：读取多个csv文件
#1，文件计数与文件中的行列计数

#!/usr/bin/env python3
import sys
import csv
import glob #定位找出匹配于某个特定模式的所有路径名
import os #包含解析路径名的函数
input_path = sys.argv[1]
file_counter = 0
for input_file in glob.glob(os.path.join(input_path ,'sales_*')): #sales_*表示搜索所有文件名以sales_开头且下划线后可为任意字符的文件
    row_counter = 1  #os.path.join将圆括号中两部分连接至一起 ，glob的glob函数将sales_*中的*转换为实际的文件名
    with open(input_file,'r',newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader,None)
        for row in filereader:
            row_counter += 1     #os.path.basename表示完整路径中抽取基本文件名
        print('{0!s}:\t{1:d} rows\t{2:d} columns'.format(os.path.basename(input_file),row_counter,len(header)))
        file_counter +=1 #打印输入文件的文件名、每个文件的行数和列数，\t是制表符，非必需，用于对齐。{}是占位符
print('Number of files: {0:d}'.format(file_counter))