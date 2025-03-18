import pandas as pd
import numpy as np

file_path = 'finish.csv'
df = pd.read_csv(file_path)
print(np.all(pd.notnull(df))) # np.all()返回是否有缺失值

print(df['type'].value_counts().to_frame().T)
print(df['oc_year'].value_counts().to_frame().T)

def read_data():
    return df

def process_data(df):
    """根據清理後的 df 產生 Descriptive_df"""
    crime_type_list = df.loc[:,['type']].groupby(df['type']).count()
    city_list = df.loc[:,['oc_county']].groupby(df['oc_county']).count()

    Descriptive_df = pd.DataFrame(columns=crime_type_list.index)  # Column 為犯罪種類
    Descriptive_df.insert(0, '縣市', True)  # 新增 Column
    Descriptive_df.insert(9, '案件總數', True)  # 新增 Column
    Descriptive_df.insert(10, '占比', True)  # 新增 Column

    for i in range(len(city_list)):
        Descriptive_df = Descriptive_df._append({
            '縣市': city_list.index[i],
            '住宅竊盜': len(df[(df['type'] == '住宅竊盜') & (df['oc_county'] == city_list.index[i])]),
            '強制性交': len(df[(df['type'] == '強制性交') & (df['oc_county'] == city_list.index[i])]),
            '強盜': len(df[(df['type'] == '強盜') & (df['oc_county'] == city_list.index[i])]),
            '搶奪': len(df[(df['type'] == '搶奪') & (df['oc_county'] == city_list.index[i])]),
            '機車竊盜': len(df[(df['type'] == '機車竊盜') & (df['oc_county'] == city_list.index[i])]),
            '毒品': len(df[(df['type'] == '毒品') & (df['oc_county'] == city_list.index[i])]),
            '汽車竊盜': len(df[(df['type'] == '汽車竊盜') & (df['oc_county'] == city_list.index[i])]),
            '組織犯罪防制條例': len(df[(df['type'] == '組織犯罪防制條例') & (df['oc_county'] == city_list.index[i])])
        }, ignore_index=True)

    Descriptive_df['案件總數'] = Descriptive_df.iloc[:, 1:9].sum(axis=1)
    Descriptive_df['占比'] = (Descriptive_df['案件總數'] / 73176) * 100

    return Descriptive_df

if __name__ == "__main__":
    df = read_data()
    Descriptive_df = process_data(df)
    Descriptive_df.to_csv('Descriptive_df_total.csv', index=False)
    print("數據已儲存為: Descriptive_df_total.csv")
    # 將同年不同月份的csv合併
    df.to_csv('Merge_df_total.csv', index=False)