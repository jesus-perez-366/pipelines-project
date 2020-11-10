
import pandas as pd
import numpy as np
def indice(x):
    #esto lo paso como argumento x = df_weather['city_name']
    # esto como argumento y= df_weather['city_name']
    y=x.unique()
    count=0
    c=1
    indi=[]
    for i in x:
        count +=1
        if i == y[c]:
            indi.append(x.index[count-1])
            c+=1
            if c == 5:
                c=0
    return indi


def div_in_set(x, y, provincia):
    if provincia == "valencia":
        df_weather_valencia = x[:y[0]].reset_index()
        return pd.DataFrame(df_weather_valencia)
    elif provincia == "madrid":
        df_weather_madrid = x[y[0]:y[1]].reset_index()
        return pd.DataFrame(df_weather_madrid)
    elif provincia == "bilbao":
        df_weather_bilbao = x[y[1]:y[2]].reset_index()
        return pd.DataFrame(df_weather_bilbao)
    elif provincia == "barcelona":
        df_weather_barcelona = x[y[2]:y[3]].reset_index()
        return pd.DataFrame(df_weather_barcelona)
    else:
        df_weather_sevilla = x[y[3]:].reset_index()
        return pd.DataFrame(df_weather_sevilla)

def delete_duplicate(data):
    df_weather_2=data.drop_duplicates(subset=['dt_iso'], keep='last')
    return pd.DataFrame(df_weather_2)

def arreglo(data2):
    d=data2[['temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed']]
    columns=list(d)
    values=0
    x=0
    mes=['31', '28', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31']
    mes2= ['31', '29', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31']
    new2=[]
    c=0
    s=1
    u=0

    new_data=[]
    for y in columns:
        new=[]
        new2=[]
        m=0
        p=0
        for i in d[y]:
            values += i
            x += 1
            if x == 24:
                new.append(values/24)
                x=0
                values=0
        for i in new:
            if s!=2:
                m += i
                p +=1
                if str(p) == mes[c]:
            
                    f=mes[c]
                    f=int(f)
                    new2.append(m/f)
                    c+=1
                    p=0
                    m=0
                    if c > 11:
                        c=0           
                        u += 1
                        if u == 1:
                            s=2
            
            else:
                m += i
                p +=1
                if str(p) == mes2[c]:
                    f=mes2[c]
                    f=int(f)
                    new2.append(m/f)
                    c+=1
                    p=0
                    m=0
                    if c > 11:
                        c=0
                        s=3
                        u+=1
        new_data.append(new2)
                            
        
    p=np.array(new_data)
    g=pd.DataFrame(p)
    g=g.transpose()
    g.columns = ['temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed']
    return pd.DataFrame(g)

def insert_month_year(m):
    x=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']*4
    year=['2015']*12+['2016']*12+['2017']*12+['2018']*12
    m.insert(0,"Month",x,True)
    m.insert(0,"Year",year,True)
    return pd.DataFrame(m)



def insert_month_year_2(m,ye):
    x=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']*4
    year=[ye[0]]*12+[ye[1]]*12+[ye[2]]*12+[ye[3]]*12
    m.insert(0,"Month",x,True)
    m.insert(0,"Year",year,True)
    return pd.DataFrame(m)

def redondear (m):
    return m.apply(lambda x: round(x,2))

def temp_C (m):
    m[['temp', 'temp_min', 'temp_max']] = m[['temp', 'temp_min', 'temp_max']].apply(lambda x: x - 273)
    return m

def clean_json(data):
    x=data[['tmed','tmin','tmax', 'presMax', 'presMin', 'velmedia','prec']]
    return x

def Pres_m(p):
    p['pres'] = (p['presMax'] + p['presMin']).apply(lambda x: x/2)
    p.drop(['presMax', 'presMin'], axis=1)
    return p[['tmed','tmin','tmax', 'pres', 'velmedia','prec']]

def inte_nan(p):
    columns=list(p)
    for i in columns:
        p[i] = p[i].interpolate() 
    return (p)

def day_a_Month (p,years2):
    columns = list(p)
    mes=['31', '28', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31']
    mes_bis= ['31', '29', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31']
    new2=[]
    c=0
    s=0
    m=0
    new=[]
    for y in columns:
        new=[]
        for year2 in years2:
            year2=int(year2)
            c=0
            if year2 % 400 == 0 and year2 % 4 == 0 and year2 % 100 !=0:             
                for i in p[y]:
                    if c<12:
                        m += i
                        s +=1
                        if str(s) == mes_bis[c]:
                            new.append(m/s)
                            c+=1
                            s=0
                            m=0
                        


            else:
                
                for i in p[y]:
                    if c<12:
                        m += i
                        s +=1
                        if str(s) == mes[c]:
                            new.append(m/s)
                            c+=1
                            s=0
                            m=0
                
        new2.append(new)
    q=np.array(new2)
    g=pd.DataFrame(q)
    g=g.transpose()
    g.columns=columns
    return g

def insert_month_year_json(m):
    x=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    year=['2019']*12
    m.insert(0,"Month",x,True)
    m.insert(0,"Year",year,True)
    return pd.DataFrame(m)
# 

def indice_year(x):

    y=x.unique()
    count=0
    c=1
    dict1={}
    for i in x:
        count +=1
        if i == y[c]:
            dict1.update ({i:x.index[count-1]})
            c+=1
            if c == 20:
                c=0                
    return dict1


def replace(data_final_2018, m):
    titles = ['temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed']
    for i in titles:
        data_final_2018[i]=m[i]
    return data_final_2018

def fecha1():
    Inicio = 2000
    Fin = 2019
    list1=[]
    for i in range (Inicio,Inicio+4):
        list1.append(i)
    return list1

def fecha2 ():
    Inicio = 2000
    Fin = 2019
    list2=[]
    for i in range (Inicio+4,Fin+1):
        list2.append(i)
    list2
    lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    return lol(list2,4)