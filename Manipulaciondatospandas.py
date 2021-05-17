import pandas as pd
#import numpy as np

artists_billboard = pd.read_csv("artists_billboard.csv")
#artists=np.asarray(artists_billboard )
#print(type(artists_billboard))
#print(type(artists))
#Ordenamos por columna
#print(artists_billboard.columns)
#print(artists_billboard.sort_values(["durationSeg"], ascending=False).to_string)
#Eliminar multiples columnas
artists_redux=artists_billboard.drop(["id","mood","tempo","artist_type","anioNacimiento"],axis=1)
#Eliminar una columna
print(artists_redux.columns)
artists_redux=artists_redux.drop(["durationSeg"],axis=1)
artists_redux=artists_redux.drop(["genre"],axis=1)
#print(artists_redux.to_string)
#Agregar una fila nueva al final
cantidad_filas = len(artists_redux)
artists_redux.loc[cantidad_filas] = ["Infinity","GURU JOSH","19900317",1]

#Actualizo una celda
artists_redux.at[635,"chart_date"] = 19900617

#Eliminar una fila
artists_redux=artists_redux.drop([0])
#Eliminar multiples filas
artists_redux=artists_redux.drop([1,3])
#Filtrar nos1
artists_redux1=artists_redux[(artists_redux["top"]==1)]
#Filtrar nos1 & despuẃs 2010
artists_redux12010=artists_redux[(artists_redux["top"]==1)&(artists_redux["chart_date"]>20100000)]
#print(artists_redux12010.to_string)
#Busco por un valor específico
artists_reduxLopez=artists_redux[artists_redux["artist"]=="JENNIFER LOPEZ"]
print(artists_reduxLopez.to_string)
artists_reduxUmbrella=artists_redux[artists_redux["title"]=="Umbrella"]
print(artists_reduxUmbrella.to_string)
artists_redux1981=artists_redux[artists_redux["chart_date"]==19900617]
print(artists_redux1981.to_string)
#transponer
print(artists_redux.T.to_string)