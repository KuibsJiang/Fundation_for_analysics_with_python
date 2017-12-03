#文件需求：使用csv文件向表中添加和更新数据。
#如何从csv格式的输入文件将数据批量的加载到数据库表中
#!/usr/bin/env python3

import sys
import csv
import sqlite3
#csv输入文件的路径和路径名
input_file = sys.argv[1]
#创建内存数据库和数据表
con = sqlite3.connect('Suppliers.db') #创建了一个本地数据库，代码运行后会在本地生成一个文件
cur = con.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS Suppliers
                (Supplier_Name VARCHAR(20),
                Invoice_Number VARCHAR(20),
                Part_Number VARCHAR(20),
                Cost FLOAT,
                Purchase_Date DATE);'''
cur.execute(create_table)
con.commit()
#读取csv文件
#向Suppliers表中插入数据
file_reader = csv.reader(open(input_file,'r'),delimiter= ',')
header = next(file_reader,None)
print(header)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    cur.execute('INSERT INTO Suppliers VALUES(?,?,?,?,?);',data)
con.commit()
print(" ") #这句是用来打印空格行，用于隔离两次打印的内容
#查询表中数据
output = cur.execute('SELECT * FROM Suppliers')
rows = output.fetchall() #取出所有返回值
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)