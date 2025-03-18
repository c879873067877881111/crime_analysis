import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('finish.csv')
df.columns = df.columns.str.strip()
print(df.columns.tolist())  # 檢查欄位名稱是否正確

# 過濾 110、111、112 年的一月份數據（0101-131）
df_january = df[(df["oc_year"].isin([110, 111, 112])) & (df["oc_data"].between(101, 131))]

# 計算總體犯罪數量
total_crimes_january = len(df_january)
print("1 月總犯罪數量：", total_crimes_january)

target_regions = ["大園區", "松山區", "小港區", "沙鹿區"]
df_filtered = df_january[df_january["oc_region"].isin(target_regions)]
crime_counts = df_filtered.groupby(["oc_region", "type"]).size().reset_index(name="count") # 統計各區域不同犯罪類型


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.figure(figsize=(12, 6))
sns.barplot(data=crime_counts, x="oc_region", y="count", hue="type")
plt.xlabel("區域")
plt.ylabel("犯罪數量")
plt.title("各區域犯罪類型分佈")
plt.xticks(rotation=30)
plt.legend(title="犯罪類型")
plt.show()
