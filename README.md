Project : crime_analysis

Ref textbook:
Pandas資料清理、重塑、過濾、視覺化: Python資料分析必備套件!/Matt Harrison/ Theodore Petrou
R錦囊妙計 (第2版)/J.D Long/ Paul Teetor
精通大數據! R語言資料分析與應用 (第2版)/Jared P. Lander
Ref websites:
https://medium.com/@jason8410271027/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E7%AC%AC%E4%B8%80%E6%AD%A5-%E8%B3%87%E6%96%99%E6%93%B7%E5%8F%96-%E6%95%B4%E7%90%86-%E5%8F%AF%E8%A6%96%E5%8C%96-efa30b4dde56

data classification:

data warehouse -> Output the original data of crime types and time in each county and city

110犯罪統計.py -> join all raw data into a dataframe for 110

111犯罪統計.py -> join all raw data into a dataframe for 111

112犯罪統計.py -> join all raw data into a dataframe for 112

Descriptive_df110 -> Export the cleaned data to a csv file for 110

Descriptive_df111 -> Export the cleaned data to a csv file for 111

Descriptive_df112 -> Export the cleaned data to a csv file for 112

excelmerge.py -> Descriptive_df110, Descriptive_df111, Descriptive_df112 merge finish.csv

finish.csv -> contains the total data files of Descriptive_df110, Descriptive_df111, and Descriptive_df112 

Plt.py -> Visualization of the correlation between various crime types

