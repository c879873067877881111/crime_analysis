import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 引入封裝的函式
from crime_stat_110 import read_data, process_data 
from crime_stat_111 import read_data, process_data 
from crime_stat_112 import read_data, process_data  

# 獲取清理後的數據
df = read_data()
Descriptive_df = process_data(df)

# 設定中文字型
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

# 繪製「縣市犯罪占比」圖表
plt.figure(figsize=(15,8))
plt.bar(Descriptive_df['縣市'], Descriptive_df['占比'], width=0.5)
plt.ylabel('占比(%)')
plt.ylim(0,20)
plt.xticks(rotation=45)
plt.grid(ls=':', lw=1)
plt.title('各縣市犯罪占比')
plt.show()

# 繪製「各類犯罪案件數」圖表
crime_type_columns = Descriptive_df.columns[1:9]

for crime_type in crime_type_columns:
    plt.figure(figsize=(15,8))
    plt.bar(Descriptive_df['縣市'], Descriptive_df[crime_type], width=0.5)
    plt.ylabel('案件數')
    plt.xticks(rotation=45)
    plt.grid(ls=':', lw=1)
    plt.title(crime_type)
    plt.show()