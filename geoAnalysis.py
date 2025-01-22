import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 讀取 CSV 文件
file_path = 'finish.csv'
data = pd.read_csv(file_path)
# 縣市分佈
county_counts = data['oc_county'].value_counts()

# 地區分佈
region_counts = data['oc_region'].value_counts()

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False
# 繪製縣市分佈柱狀圖
plt.figure(figsize=(12, 6))
sns.barplot(x=county_counts.index, y=county_counts.values, palette="viridis")
plt.title('縣市事件分佈', fontsize=16)
plt.xlabel('縣市', fontsize=12)
plt.ylabel('事件數量', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 繪製地區分佈柱狀圖
plt.figure(figsize=(12, 6))
top_regions = region_counts[:20]  # 只顯示前 20 大地區
sns.barplot(x=top_regions.index, y=top_regions.values, palette="coolwarm")
plt.title('地區事件分佈（前 20 大地區）', fontsize=16)
plt.xlabel('地區', fontsize=12)
plt.ylabel('事件數量', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
