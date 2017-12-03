#文件需求：从数据库中找出符合条件的数据，查询出来并保存至csv文件
##!/usr/bin/env python3

import sys
import csv
import MySQLdb
#csv输出文件的路径和路径名
output_file = sys.argv[1]
#连接MYSQL数据库
con = MySQLdb.connect(host = 'localhost',port = '3306',db = 'my_suppliers',user = 'root',passwd = 'password')
cur = con.cursor()
#创建写入文件的对象，并写入标题行
filewriter = csv.writer(open(output_file,'w',newline=''),delimiter = ',')
header = ['supplier name','invoice number','part number','cost','purchase date']
filewriter.writerow(header)
#查询表，并将结果写出到csv文件
cur.excute('''SELECT * FROM suppliers
            WHERE cost > 700.0;''')
rows = cur.fetchall()
for row in rows:
    filewriter.writerow(row)