import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning.main_ana import read_data, process_data

# 獲取清理後的數據
df = read_data()
Descriptive_df = process_data(df)

# 設定中文字型
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

# 繪製「縣市犯罪占比」圓餅圖
sorted_df = Descriptive_df.sort_values(by='占比', ascending=False)
if len(sorted_df) > 10:
    top_10 = sorted_df.iloc[:10]
    other = pd.DataFrame({'縣市': ['其他'], '占比': [sorted_df.iloc[10:]['占比'].sum()]})
    pie_data = pd.concat([top_10, other])
else:
    pie_data = sorted_df

plt.figure(figsize=(10, 10))
colors = sns.color_palette("Set3", len(pie_data))
plt.pie(pie_data['占比'], labels=pie_data['縣市'], autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('各縣市犯罪占比')
plt.show()

# 繪製「各類犯罪案件數」圓餅圖
crime_type_columns = Descriptive_df.columns[1:9]
for crime_type in crime_type_columns:
    sorted_crime = Descriptive_df.sort_values(by=crime_type, ascending=False)
    if len(sorted_crime) > 10:
        top_10 = sorted_crime.iloc[:10]
        other = pd.DataFrame({'縣市': ['其他'], crime_type: [sorted_crime.iloc[10:][crime_type].sum()]})
        pie_crime_data = pd.concat([top_10, other])
    else:
        pie_crime_data = sorted_crime
    
    plt.figure(figsize=(10, 10))
    colors = sns.color_palette("Set3", len(pie_crime_data))
    plt.pie(pie_crime_data[crime_type], labels=pie_crime_data['縣市'], autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(crime_type)
    plt.show()