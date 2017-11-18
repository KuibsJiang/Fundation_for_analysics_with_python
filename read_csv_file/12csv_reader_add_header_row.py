#为表格中的所有列添加列标题行
#method1 基础python语句

#!/usr/bin/env python3
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file,'r',newline='') as csv_in_data:
    with open(output_file,'w',newline='') as csv_out_data:
        filereader = csv.reader(csv_in_data)
        filewriter = csv.reader(csv_out_data)
        header = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date'] #手动将需要的列属性添加至标题行
        filewriter.writerow(header)
        for row in filereader:
            filewriter.writerow(row)