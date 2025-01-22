import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 文件
file_path = 'finish.csv'
data = pd.read_csv(file_path)

# 確保列名正確
data.columns = data.columns.str.strip()

# 簡單統計
# 1. 事件類型分佈
type_counts = data['type'].value_counts()

# 2. 年份分佈
year_counts = data['oc_year'].value_counts()

# 3. 月份分佈
data['month'] = data['oc_data'].astype(str).str.zfill(4).str[:2]  # 提取月份，補零
month_counts = data['month'].value_counts().sort_index()

# 繪圖
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# 事件類型分佈
axes[0].bar(type_counts.index, type_counts.values, color='skyblue')
axes[0].set_title('事件類型分佈', fontsize=16)
axes[0].set_xlabel('事件類型', fontsize=12)
axes[0].set_ylabel('事件數量', fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# 年份分佈
axes[1].bar(year_counts.index, year_counts.values, color='lightgreen')
axes[1].set_title('年份分佈', fontsize=16)
axes[1].set_xlabel('年份', fontsize=12)
axes[1].set_ylabel('事件數量', fontsize=12)

# 月份分佈
axes[2].bar(month_counts.index, month_counts.values, color='salmon')
axes[2].set_title('月份分佈', fontsize=16)
axes[2].set_xlabel('月份', fontsize=12)
axes[2].set_ylabel('事件數量', fontsize=12)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False
plt.tight_layout()
plt.show()
