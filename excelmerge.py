import pandas as pd

file_paths = ['Descriptive_df110.csv', 'Descriptive_df111.csv', 'Descriptive_df112.csv']

df = [pd.read_csv(file) for file in file_paths]
combined_df = pd.concat(df, ignore_index=True)
combined_df.to_csv('finish.csv', index=False, encoding='utf-8-sig')