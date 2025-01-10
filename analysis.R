# 讀取 CSV 文件
library(readr)
data <- read_csv("finish.csv")

# 建立列聯表
contingency_table <- table(data$oc_county, data$type)

# 顯示列聯表
print(contingency_table)

# 執行卡方檢定
chi_test <- chisq.test(contingency_table)

# 顯示檢定結果
print(chi_test)