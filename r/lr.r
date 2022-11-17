insurance<-read.csv("insurance.csv",stringsAsFactors = TRUE)
str(insurance)
summary(insurance$expenses)
hist(insurance$expenses)
table(insurance$region)
cor(insurance[c("age","bmi","children","expenses")])
pairs(insurance[c("age","bmi","children","expenses")])
library(psych)
pairs.panels(insurance[c("age","bmi","children","expenses")])8
ins_model <- lm(expenses ~ age + children + bmi + sex + smoker + region, data = insurance)
ins_model
summary(ins_model)
insurance$age2 <- insurance$age^2
insurance$bmi30 <- ifelse(insurance$bmi >= 30,1,0)
expenses ~ bmi30*smoker
expenses ~ bmi30+smokeryes+bmi30:smokeryes
ins_model2 <- lm(expenses ~ age+age2+children+bmi+sex+bmi30*smoker+region,data=insurance)
summary(ins_model2)