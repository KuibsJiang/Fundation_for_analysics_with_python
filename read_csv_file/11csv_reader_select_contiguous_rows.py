#文件需求：选取连续的行
#method1 基础python语句

#!/usr/bin/env python3
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
row_counter = 0 #引入变量跟踪行编号
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >=3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1
                
