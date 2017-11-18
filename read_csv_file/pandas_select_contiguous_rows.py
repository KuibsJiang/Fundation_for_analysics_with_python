#文件需求：选取连续的行
#method2 pandas语句，drop函数能根据行索引和列标题来丢弃行或列。
#iloc函数根据行索引选取一个单独行作为列索引。
#reindex函数为数据框重新生成索引

#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file,header=None)
data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))
data_frame.to_csv(output_file,index=False)