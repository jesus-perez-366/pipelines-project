import matplotlib.pyplot as plt
import seaborn as sns

#genera las etequitas de los graficos
def etiquetas(x,y,z,n):
    '''
    Pertime darle un formato a la graficas (Titulo y tamaño, etiqueta a los ejes, tamño del grafico)
    args:
    x (String) = Es el titulo del grafico
    y (String) = Es la etiqueta del eje x
    z (String) = Es la etiqueta del eje y
    n (int) = Tamaño de la letra del titulo
    Return:
    none
    '''
    plt.suptitle(x, size=n)
    plt.xlabel(y)
    plt.ylabel(z)

# crea todos los graficos
def graficos(x,y,k):
    grafico_total (x,'Comparativa de la Temp. por mes en todos los años', 'Meses', 'Temp ºC', '17', '1')
    grafico_area(x,'''Promedio de la Temp anual desde 
    el 2000 al 2019''', 'Años', 'Temp. ºC', '17', '2')
    grafico_plot(x,'''Comportamiento de la Temp. min y max 
    desde el 2000 al 2019''', 'Años', 'Temp. ºC', '17', ['1999', '2000', '2004', '2008', '2012', '2018', '2020'],'3')
    grafico_plot(y,'''Comportamiento de la Temp. min y max desde
    el 2000 al 2019 (data aemet)''', 'Años', 'Temp. ºC', '17', ['1999', '2000', '2004', '2008', '2012', '2018', '2020'], '4')
    grafico_plot(k,'''Comportamiento de la Temp. min y max desde
    el 2015 al 2018 (data Kaggle)''', 'Años', 'Temp. ºC', '17', [], '5')
    grafico_plot_2ejes(x, 'temp', 'Precip', '20', 'Relacion Temp vs Precip', '', 'mm', '17', [], '6', "Temp", "Precipitacion", 'Temp. ºC')
    grafico_plot_2ejes(x, 'Precip', 'wind_speed', '40', 'Relacion Precip vs Veloc. viento', '', 'm/s', '17', [], '7', "Precipitacion", "velocidad del viento", 'mm')


# funcion que crea un grafico tipo scatter
def grafico_total (x, t, eje_x, eje_y, size, i):
    sns.scatterplot(x="Month", y='temp', hue = 'Year',palette='colorblind', data=x)
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', title = 'Years')
    save(t, eje_x, eje_y, size, i)

# funcion que crea un grafico tipo line
def grafico_area(x,t,eje_x, eje_y, size, i):
    x.groupby('Year').temp.mean().plot()
    plt.xticks(rotation=45)
    save(t, eje_x, eje_y, size, i)
    return 

# funcion que crea un grafico tipo line
def grafico_plot(x,t,eje_x, eje_y, size, labels,i):
    x["temp_min"].plot(label="Temp. Min", legend=True).set_xticklabels(labels)
    x["temp_max"].plot(label="Temp. Max", legend=True)
    save(t, eje_x, eje_y, size, i)
    return 

# funcion que crea un grafico tipo line pero con dos variables en el eje Y
def grafico_plot_2ejes(x, param, param2, cant, t, eje_x, eje_y, size, labels, i, label1, label2, uni1):
    hight=x.sort_values(param, ascending=False)
    hight=hight.head(int(cant)).reset_index(drop=True)
    hight[param].plot(label=label1, legend=True).set_xticklabels(labels) 
    plt.ylabel(uni1)
    hight[param2].plot(secondary_y=True, label=label2, legend=True)
    save(t, eje_x, eje_y, size, i)
    return 

# guarda y cierra el plot
def save(t, eje_x, eje_y, size, i):
    etiquetas(t, eje_x, eje_y, size)
    plt.savefig(f'output/Grafico{i}.jpg', bbox_inches='tight')
    plt.clf()