#当行中的值属于某个集合
#文件需求2：筛选出数据中日期属于{'1/20/14','1/30/14'}的行

#method2 pandas
#!/usr/bin/env python3
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
