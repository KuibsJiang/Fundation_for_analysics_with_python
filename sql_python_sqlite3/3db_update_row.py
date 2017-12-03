#文件需求：使用csv输入文件更新数据表中已有的数据

#!/usr/bin/env python3

import sys
import csv
import sqlite3
#csv输入文件的文件路径和文件名
input_file = sys.argv[1]
#创建内存数据库和数据表
con = sqlite3.connect(':memory:')
create_table = '''CREATE TABLE IF NOT EXISTS sales
                (customer VARCHAR(20),
                product VARCHAR(20),
                amount FLOAT,
                date DATE);'''
con.execute(create_table)
con.commit()
#向表中插入数据
data = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
for tuple in data:
    print(tuple)
statement = 'INSERT INTO sales VALUES(?,?,?,?)'
con.executemany(statement,data)
con.commit()
#读取csv文件并更新特定行
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute('UPDATE sales SET amount=?,date=? WHERE customer=?;',data)
con.commit()
#查询数据表
cursor = con.execute('SELECT * FROM sales')
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)