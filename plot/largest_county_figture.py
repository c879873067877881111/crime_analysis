import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'finish.csv'
df = pd.read_csv(file_path)

fig, axes = plt.subplots(figsize=(12, 18))

county_counts = df['oc_county'].value_counts()
sns.barplot(x=county_counts.index, y=county_counts.values, palette="Blues_r")
axes.set_title("各縣市事件數量分佈")
axes.set_xlabel("縣市")
axes.set_ylabel("事件數量")
axes.tick_params(axis='x', rotation=45)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.show()