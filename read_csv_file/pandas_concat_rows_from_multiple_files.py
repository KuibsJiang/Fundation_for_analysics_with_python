#文件需求：将包含相似数据的多个文件连接起来，实现数据连接至一张表中
#method2 pandas语句
#使用pandas将多个输入文件的数据垂直连接成一个输出文件 axis = 0
#pandas方法主要是将输入文件读取到数据框中，再将数据框追加到一个数据列表，然后concat方法将所有数据框连接成一个数据框

#额外要注意的一点是：13行for语句中的'sale_*'而不是'*.csv'.避免输入输出文件在统一路径下导致出问题

#!/usr/bin/env python3
import sys
import os
import glob
import pandas as pd
input_path = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frames = []

for file in all_files:
    data_frame = pd.read_csv(file,index_col= None)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames,axis=0,ignore_index=True) #axis=0 垂直堆叠数据框，axis=1 平行连接
data_frame_concat.to_csv(output_file,index= False)

