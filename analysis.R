# 檢驗縣市與事件類型的相關性檢定
# 目標：檢驗不同縣市與事件類型之間是否存在顯著的相關性
data <- read.csv("finish.csv")

# 確保數據列名正確
colnames(data) <- trimws(colnames(data))

# 生成列聯表
county_type_table <- table(data$oc_county, data$type)

# 檢視列聯表
print("列聯表:")
print(county_type_table)

# 卡方檢定
chisq_test <- chisq.test(county_type_table)

# 檢視檢定結果
print("卡方檢定結果:")
print(chisq_test)