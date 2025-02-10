# 月份與事件數量的季節性變化檢定
# 目標：檢驗事件數量是否具有明顯的季節性特徵。
# 方法：
# 使用 單因素方差分析 (ANOVA) 檢驗不同月份之間的事件數量是否存在顯著差異。
# 假設 H0：不同月份的事件數量無顯著差異。
# 若檢定顯著，進行事後檢定（Tukey HSD）找出具體不同的月份

# 準備數據：從 oc_data 取出月份
# 做ONE WAY ANOVA 檢定：
# 檢驗不同月份之間的事件數量是否存在顯著差異
# 假設 H0：不同月份的事件數量無顯著差異

data <- read.csv("finish.csv")
# 取出月份
data$month <- as.numeric(substr(data$oc_data, 1, nchar(data$oc_data) - 2))
# 確認每個月份的事件數量是否為 0
table(data$month)
# 單因素 ANOVA 檢定
anova_result <- aov(as.numeric(oc_data) ~ factor(month), data = data)

# 檢視 ANOVA 結果
summary(anova_result)


