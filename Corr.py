import pandas as pd
file_path = 'finish.csv'
data = pd.read_csv(file_path)

# 顯示數據的前幾行以了解其結構
data.head()
# print(data)

# 創建數據透視表以分析犯罪類型之間的關係
# 按 "type"（犯罪類型）和 "oc_region"（發生區域）分組，以識別重疊情況
crime_region_pivot = data.pivot_table(index='oc_region', columns='type', aggfunc='size', fill_value=0)

# 計算犯罪類型之間的相關性
crime_type_correlation = crime_region_pivot.corr()

# 顯示相關矩陣並將其可視化為熱圖
import matplotlib.pyplot as plt
import seaborn as sns

# 設定字體讓 plt 文字能正常顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 繪製熱圖
plt.figure(figsize=(12, 8))
sns.heatmap(crime_type_correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("犯罪類型之間的相關性", fontsize=14)

# 使用自定義標籤函數
plt.xticks(ticks=range(len(crime_type_correlation.columns)), 
           labels=[col[:7] for col in crime_type_correlation.columns],
           rotation=0, ha='right', fontsize=12)

plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
