#文件需求：将包含相似数据的多个文件连接起来，实现数据连接至一张表中
#method1 基础python语句

#额外要注意的一点是：13行for语句中的'sale_*'而不是'*.csv'.避免输入输出文件在统一路径下导致出问题
#!/usr/bin/env python3
import sys
import csv
import os
import glob
input_path = sys.argv[1]
output_file = sys.argv[2]
first_file = True #引入是为了只保留一条列标题行
for input_file in glob.glob(os.path.join(input_path ,'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file,'r',newline='') as csv_in_file:
        with open(output_file,'a',newline='') as csv_out_file: #'a'以追加的方式打开输出文件，添加。若'w'写入的话会造成覆盖
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:  #if语句是将第一个文件的所有行添加的输出文件
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:  #else语句使用next方法将余下文件的标题行赋值给一个变量，但是并不添加到输出文件中
                header = next(filereader,None)
                for row in filereader:
                    filewriter.writerow(row)
