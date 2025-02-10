import pandas as pd

def read_data():
    df1 = pd.read_csv('data warehouse/11201-11203犯罪資料.csv', skipinitialspace=True)
    df2 = pd.read_csv('data warehouse/11204-11206犯罪資料.csv', skipinitialspace=True)
    df3 = pd.read_csv('data warehouse/11207-11209犯罪資料.csv', skipinitialspace=True)
    df4 = pd.read_csv('data warehouse/11210-11212犯罪資料.csv', skipinitialspace=True)
    df = pd.concat([df1,df2,df3,df4], axis=0).reset_index(drop = True)  #合併

    # 資料清理
    df = df[df.type != '案類']
    df = df[df.oc_year != '發生日期']
    df = df[df.oc_county != '發生地點']
    df = df[df.type != '說明 : 機車竊盜案件因發生地在路界、縣界等區域或報案']
    df = df[df.type != '人提供失竊地點不明確時，發生地僅顯示縣、市。']
    df.oc_county = df.oc_county.str.slice(0,3)
    df = df.dropna().reset_index(drop = True)

    return df

def process_data(df):
    crime_type_list = df.loc[:,['type']].groupby(df['type']).count()
    city_list = df.loc[:,['oc_county']].groupby(df['oc_county']).count()
    Descriptive_df = pd.DataFrame(columns=crime_type_list.index)  #Column為犯罪種類
    Descriptive_df.insert(0, '縣市', True) #新增Column
    Descriptive_df.insert(9, '案件總數',True) #新增Column
    Descriptive_df.insert(10, '占比', True) #新增Column
    for i in range(0, len(city_list)):
        Descriptive_df = Descriptive_df._append({
            '縣市':city_list.index[i],
            '住宅竊盜':len(df[(df['type'] == '住宅竊盜') & (df['oc_county'] == city_list.index[i])]),
            '強制性交':len(df[(df['type'] == '強制性交') & (df['oc_county'] == city_list.index[i])]),
            '強盜':len(df[(df['type'] == '強盜') & (df['oc_county'] == city_list.index[i])]),
            '搶奪':len(df[(df['type'] == '搶奪') & (df['oc_county'] == city_list.index[i])]),
            '機車竊盜':len(df[(df['type'] == '機車竊盜') & (df['oc_county'] == city_list.index[i])]),
            '毒品':len(df[(df['type'] == '毒品') & (df['oc_county'] == city_list.index[i])]),
            '汽車竊盜':len(df[(df['type'] == '汽車竊盜') & (df['oc_county'] == city_list.index[i])]),
            '組織犯罪防制條例':len(df[(df['type'] == '組織犯罪防制條例') & (df['oc_county'] == city_list.index[i])])
        }, ignore_index=True)
    

    #依據Descriptive_df，把每個Row的Column1到Column8全部加總
    Descriptive_df['案件總數'] = Descriptive_df.iloc[:,1:9].sum(axis = 1)
    #把每一筆的案件總數值除以22961，再乘以100，計算出該縣市的犯罪占比佔全台灣的幾%
    Descriptive_df['占比'] = (Descriptive_df['案件總數']/22961)*100

    return Descriptive_df

if __name__ == "__main__":
    df = read_data()
    Descriptive_df = process_data(df)
    Descriptive_df.to_csv('Descriptive_df112.csv', index=False)
    print("數據已儲存為: Descriptive_df112.csv")
    df.to_csv('Merge_df112.csv', index=False)