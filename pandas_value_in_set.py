#当行中的值属于某个集合
#文件需求2：筛选出数据中日期属于{'1/20/2014','1/30/2014'}的行

#method2 pandas
#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
important_data = ['1/30/2014','1/30/2014']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_data),:] #loc函数和isin函数
data_frame_value_in_set.to_csv(output_file,index = False)
