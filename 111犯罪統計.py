import pandas as pd
df1 = pd.read_csv('11101-11103犯罪資料.csv', skipinitialspace=True)
df2 = pd.read_csv('11104-11106犯罪資料.csv', skipinitialspace=True)
df3 = pd.read_csv('11107-11109犯罪資料.csv', skipinitialspace=True)
df4 = pd.read_csv('11110-11112犯罪資料.csv', skipinitialspace=True)
df = pd.concat([df1,df2,df3,df4], axis=0).reset_index(drop = True)  #合併

#資料清理
df = df[df.type != '案類']
df = df[df.oc_year != '發生日期']
df = df[df.oc_county != '發生地點']
df = df[df.type != '說明 : 機車竊盜案件因發生地在路界、縣界等區域或報案']
df = df[df.type != '人提供失竊地點不明確時，發生地僅顯示縣、市。']
df.oc_county = df.oc_county.str.slice(0,3)
df = df.dropna().reset_index(drop = True)


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
#把每一筆的案件總數值除以23808，再乘以100，計算出該縣市的犯罪占比佔全台灣的幾%
Descriptive_df['占比'] = (Descriptive_df['案件總數']/23808)*100
print(Descriptive_df)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'  #讓圖表能夠正常顯示中文
listx = Descriptive_df['縣市'] #X軸資料
listy = Descriptive_df['占比'] #Y軸資料
plt.figure(figsize=(15,8)) #繪製圖表大小
plt.bar(listx, listy, width=0.5) #長條圖
plt.ylabel('占比(%)') #Y軸標題
plt.ylim(0,20) #Y軸顯示範圍
plt.xticks(rotation = 45)  #X軸旋轉45度
plt.grid(ls = ':', lw = 1) #設定格線
plt.show()

for i in range(0, len(crime_type_list.index)):
    listx = Descriptive_df['縣市'] #X軸資料
    listy = Descriptive_df[crime_type_list.index[i]] #Y軸資料
    plt.figure(figsize=(15,8)) #圖表大小
    plt.bar(listx, listy, width=0.5) #繪製長條圖
    plt.ylabel('案件數') #Y軸標題
    plt.xticks(rotation = 45) #X軸旋轉45度
    plt.grid(ls = ':', lw = 1) #繪製格線
    plt.title(crime_type_list.index[i]) #圖表標題
    plt.show()
df.to_csv('Descriptive_df111.csv', index=False)