#当行中的值匹配某个表达式（正则表达式）
#文件需求1：筛选出发票以001开头的行
#method2 pandas

#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startwith('001-'),:]
data_frame_value_matches_pattern.to_csv(output_file,index=False)