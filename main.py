import src.create as cr
import src.Grafico as gr

print("Analisis de Clima desde el 2000 hasta 2019")
print("Introduce una de estas 5 localidades (Madrid, Valencia, Bilbao, Barcelona, Sevilla)")
x=input()
data_weather_kaggle = cr.creat_data_weather_kaggle(x)
data_weather_aemet = cr.creat_data_weather_aemet(x)
df_data_weather_aemet = cr.creat_data_weather_aemet2(x, data_weather_aemet )
df_data_weather_final = cr.union(df_data_weather_aemet, data_weather_kaggle)
gr.graficos(df_data_weather_final,df_data_weather_aemet,data_weather_kaggle)

