# <img src=imagen/clima-gif-5.gif width="1000"> 
# El Clima

## Proyecto
Consiste en elaborar un codigo con el cual se pueda obtener la informacion en la web y unificarla con otra informacion para su posterior analisis.

### Tema para el analisis
Clima en Madrid y otras provincia.

### Informacion
Un Data_set extraido de la web de Kaggle
Extracion por medio de la API de la Agencia Estatal de Meteorologia.


## Procesos
### A) Data de Kaggle
1.- Se analizo la informacion y se planteo una nueva estructura de la data.
2.- Se realizaron filtros como eliminacion de informacion no necesaria para el proyecto.
3.- Se crearon funciones para agruprar la informacion ya que la data esta registrada por hora.
nota: Cuando se trata de agrupar de manera mensual una informacion de una data historica, hay que tener encuenta los años bisciesto.

Condicion empleada para determinar si el año es biciesto
```
if year2 % 400 == 0 and year2 % 4 == 0 and year2 % 100 !=0:
```

4.- crear el nuevo data_set

### B) API de la AEMET
1.- Se realizo el estudio para el uso del AEMET OpenData el cual es una API REST (no tienen documentacion para su uso)
2.- Se determinaron cuales eran los parametros necesarios para poder extraer la informacion requerida.

```
    token=open("./input/key.txt").readlines()[0]
    token = token.strip()
    response = requests.get(url, headers={"api_key": token})

```

3.- Se elaboraron la secuencia de codigos necesarios para extraer la informacion.
4.- Se filtro, limpio y estructuro la informacion necesaria.

### C) Union
1.- Se realizo la union de toda la informacion en un Data Set

EJEMPLO

```
    data_final=pd.concat([data_final_2014,data_final_2018,data_final_2019])
```

### D) Analisis
1.- Elaboracion de 3 graficas sobre temperatura
2.- Elaboracion de un grafico con los datos de kaggel y otro con los datos de AEMET para dar explicacion a un comportamiento observado en la primeras graficas.
3.- Elaboracion de dos graficas para observar si habia una correlacion entre la Temperatura y la precipitaciones, asi como las precipitaciones con la velocidad del viento.

Codigo (Graficos con dos distribuciones distintas en el eje Y)

```
def grafico_plot(x,t,eje_x, eje_y, size, labels,i):
    x["temp_min"].plot(label="Temp. Min", legend=True).set_xticklabels(labels)
    x["temp_max"].plot(label="Temp. Max", legend=True)
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    save(t, eje_x, eje_y, size, i)
```


## Resultados
Los Datos reflejan en el transcurso del 20 años el clima presenta una tendencia de crecimiento en su temperatura media, llegando a ser un aumento del 10% aproximadamente, esto son datos que se deben analizar a mayor detalle, sin embargo estos resultados primarios, indican un alto aumento en la temperatura.

Se pudo observar que al comparar el cambio de temperatura en un mes particular en los 20 años existe una variacion de entre 4 grados Celsius hasta casi 10 grados Celsius, estas variaciones pueden deberse a eventos o fenomenos ocurrido en ese año (olas de calor, sequías, inundaciones, derretimiento extensivo del hielo polar, entre otras).

Se constato que la temperatura no tiene una relacion directa con las precipitacion y de igual manera sucede con las precipitacion con respecto a la velocidad del tiempo.


<img src=output/Grafico1.jpg width="700"> 



<img src=output/Grafico2.jpg width="700"> 

