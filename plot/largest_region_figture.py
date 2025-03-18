import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'finish.csv'
df = pd.read_csv(file_path)

# 各區域 (oc_region) 的事件數量分佈
region_counts = df['oc_region'].value_counts()

fig, axes = plt.subplots(figsize=(15, 8))  # 加大宽度
sns.barplot(x=region_counts.index, y=region_counts.values, palette="Greens_r")

axes.set_title("各區域事件數量分佈")
axes.set_xlabel("區域")
axes.set_ylabel("事件數量")

# 因為x-label太多導致顯示錯誤，採取每10個count顯示
step = max(1, len(region_counts) // 10)  

plt.xticks(region_counts.index[::step], rotation=45, ha="right")
plt.xticks(rotation=45, ha="right")  
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.tight_layout()  
plt.show()
