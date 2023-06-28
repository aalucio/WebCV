library(dplyr)
library(corrplot)

df <- read.csv("COVID-19-2.csv",header = TRUE, sep=";")


df <- df %>% select(-Eli1,-Eli2,-Eli3,-Eli4,-Eli5,-Eli6,-Eli7.)
df <- df %>% mutate_all(~ifelse(. == "...", 0, .))

df$NRecuperados[is.na(df$NRecuperados)] <- 0
df$Proporcion <- gsub(",", ".", as.character(df$Proporcion))
dfSinFecha <- df %>% select(-Fecha)
dfSinFecha <- dfSinFecha %>% mutate_if(is.character, as.numeric)



df <- df$Fecha




dfSinFecha[is.na(dfSinFecha)]<-0

df <- cbind(df, dfSinFecha)

summary(df)


dfSinTra<- dfSinFecha %>% select(-NPTratados)
chisq.test(dfSinTra)






corr_matrix <- cor(dfSinFecha, method = "spearman")
corrplot(corr_matrix, method = "number")



plot(df$NMuertos, df$Edad70.79, xlab = "NMuertos", ylab = "Edad70.79")
plot(df$NMuertos, df$Edad0.9, xlab = "NMuertos", ylab = "Edad0.9")
##########################################################################
