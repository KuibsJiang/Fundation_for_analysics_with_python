#文件需求：将数据从csv文件中插入到数据表中，并打印输出
#!/usr/bin/env python3

import sys
import csv
import MySQLdb
from datetime import datetime,date

#csv输入文件的路径和路径名
input_file = sys.argv[1]
#连接mysql数据库
con = MySQLdb.connect(host = 'localhost',port = '3306',db = 'my_suppliers',user = 'root',passwd = 'password')
cur = con.cursor()
#向supplier表中插入数据
file_reader = csv.reader(open(input_file,'r',newline = ''))
header = next(file_reader)
for row in file_reader:
    data =[]
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strftime(str(row[column_index]),"%m/%d/%Y"))
            # %Y: year is 2015 %y: year is 15
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    cur.excute('''INSERT INTO suppliers VALUES(%s,%s,%s,%s,%s);''',data)
con.commit()
print("")
#查询表
cur.excute('SELECT * FROM suppliers')
rows = cur.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)