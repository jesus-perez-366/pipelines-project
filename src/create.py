import pandas as pd
import re
import src.clean as cn
import src.json as jn
import numpy as np
import src.Grafico as gr


#crea el data set de weather_Kaggle
def creat_data_weather_kaggle(x):
    df_weather=pd.read_csv("input/weather_features.csv",encoding='cp1252')
    df_weather_CN = df_weather['city_name']
    df_indice = cn.indice(df_weather_CN)
    df_data = cn.div_in_set(df_weather,df_indice,"madrid")
    df_data2 = cn.delete_duplicate(df_data)
    df_data_weather = cn.arreglo(df_data2)
    df_data_weather = cn.redondear(df_data_weather)
    df_data_weather = cn.insert_month_year(df_data_weather)
    df_data_weather = cn.temp_C (df_data_weather)
    df_data_weather.insert(8, "prec", np.nan)
    df_data_weather.columns = ['Year', 'Month', 'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'Precip']
    df_data_weather.to_csv('output/weather_kaggle.csv')
    return df_data_weather

#crea el data set de weather_aemet inicial
def creat_data_weather_aemet(x):
    year= cn.fecha1()
    inf_wather = jn.Gen_url(x,year)
    inf_wather = jn.data_weather(inf_wather)
    inf_wather = cn.clean_json(inf_wather)
    inf_wather = inf_wather.replace(regex=r'\,', value=".")
    inf_wather = inf_wather.replace('Ip', value="0.1")
    inf_wather = inf_wather.astype(float)
    inf_wather = cn.Pres_m(inf_wather)
    inf_wather = cn.inte_nan(inf_wather)
    inf_wather = cn.day_a_Month (inf_wather,year)
    inf_wather = cn.redondear(inf_wather)
    inf_wather = inf_wather.reset_index(drop=True)
    inf_wather = cn.insert_month_year_2(inf_wather,year)
    inf_wather.insert(6, "humidity", np.nan)
    inf_wather.columns = ['Year', 'Month', 'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'Precip']
    data_final_weather = inf_wather.reset_index(drop=True)
    return data_final_weather

#crea el data set de weather_aemet completo
def creat_data_weather_aemet2(x, y):
    years= cn.fecha2()
    for year in years:
        inf_wather = jn.Gen_url(x,year)
        inf_wather = jn.data_weather(inf_wather)
        inf_wather = cn.clean_json(inf_wather)
        inf_wather = inf_wather.replace(regex=r'\,', value=".")
        inf_wather = inf_wather.replace('Ip', value="0.1")
        inf_wather = inf_wather.astype(float)
        inf_wather = cn.Pres_m(inf_wather)
        inf_wather = cn.inte_nan(inf_wather)
        inf_wather = cn.day_a_Month (inf_wather,year)
        inf_wather = cn.redondear(inf_wather)
        inf_wather = inf_wather.reset_index(drop=True)
        inf_wather = cn.insert_month_year_2(inf_wather,year)
        inf_wather.insert(6, "humidity", np.nan)
        inf_wather.columns = ['Year', 'Month', 'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'Precip']
        data_final_weather2 = inf_wather.reset_index(drop=True)
        y=pd.concat([y,data_final_weather2 ])
    y=y.reset_index(drop=True)
    y.to_csv('output/weather_aemet.csv')
    return y

# unifica los 2 dataset
def  union(x,y):
    dict1=cn.indice_year(x['Year'])
    data_final_2014 = x[:dict1[2015]].reset_index(drop=True)
    data_final_2018 = x[dict1[2015]:dict1[2019]].reset_index(drop=True)
    data_final_2019 = x[dict1[2019]:].reset_index(drop=True)
    data_final_2018 = cn.replace(data_final_2018, y)
    data_final=pd.concat([data_final_2014,data_final_2018,data_final_2019])
    data_final=data_final.reset_index(drop=True)
    data_final.to_csv('output/weather_final.csv')
    return data_final