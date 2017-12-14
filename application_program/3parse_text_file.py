#文件需求：为文本文件中数据的任意数目分类计算统计量
#文本文件，也称平面文件，csv文件就是以逗号分隔的文本文件。通常活动日志，错误日志，交易记录等为文本文件
#!/usr/bin/env python3
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
messages = {} # 创建的空字典，是一个嵌套字典{错误日期:{错误信息:次数}}
notes = [] #存放所有错误信息
with open(input_file,'r',newline='') as txt_file:
    for row in txt_file:
        if '[Note]' in row:
            row_list = row.split(' ',4) #将该行按照空格拆分4次
            day = row_list[0].strip() #strip函数除去两端任何多余的空格、制表符和换行符
            note = row_list[4].strip('\n').strip()
            if note not in notes:
                notes.append(note)
            if day not in messages:
                messages[day] = {}
            if note not in messages[day]:
                messages[day][note] = 1
            else:
                messages[day][note] += 1
filewriter = open(output_file,'w',newline='')
header = ['Date']
header.extend(notes) #扩展，将notes中信息扩展到header行中
header = ','.join(map(str,header)) + '\n' #将header中内容在写入输出文件前转换成一个长字符串
print(header)
filewriter.write(header)
for day,day_value in messages.items():
    row_output = []
    row_output.append(day)
    for index in range(len(notes)):
        if notes[index] in day_value.keys():
            row_output.append(day_value[notes[index]])
        else:
            row_output.append(0)
    output = ','.join(map(str,row_output)) + '\n'
    print(output)
    filewriter.write(output)
filewriter.close()