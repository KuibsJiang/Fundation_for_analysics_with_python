#文件需求：sqlite3模块1.创建内存数据库和数据表，2.在表中插入数据，3.获取输出数据，4.对sql查询输出的行进行计数。
#!/use/bin/env python3

import sqlite3 #轻量级的基于磁盘的数据库，无需独立的服务器进程

#创建SQLite3内存数据库
#创建带有4个属性的sales表
con = sqlite3.connect(':memory:') #创建连接对象con来代表数据库，是为了使用这个模块
query = '''CREATE TABLE sales       
             (customer VARCHAR(20),
             product VARCHAR(40),
             amount FLOAT,
             date DATE);''' #三引号创建多行字符串，赋值给变量query，varchar（变长字符型字段）
con.execute(query) #excute方法执行sql语句
con.commit() #commit方法将修改提交（保存）到数据库中，必须要提交，不提交则无法保存。

#在sales表中插入数据
data = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
statement = 'INSERT INTO sales VALUES(?,?,?,?)' #？占位符
con.executemany(statement,data) #执行多次所以用executemany
con.commit()

#查询sales表
cursor = con.execute('SELECT * FROM sales') #光标对象cursor的若干方法：execute()/executemany()/fetchone()/fetchmany()/fetchall()
rows = cursor.fetchall() #取出返回的所有值

#对查询结果计数
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows:%d' % (row_counter))
