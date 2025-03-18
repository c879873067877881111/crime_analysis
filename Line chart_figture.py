import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'finish.csv'
df = pd.read_csv(file_path)

year_counts = df['oc_year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 5))  # 單個圖時使用 ax，而不是 axes
sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", ax=ax, color="red")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.show()