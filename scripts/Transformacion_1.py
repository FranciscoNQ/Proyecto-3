#Librerias
import pandas as pd 
import datetime as dt
import requests
import time

#Variables con ubicacion y nombre de los datasets
Ubicacion = "C:/Users/nicol/Desktop/Proyecto #4/dataset/"
Ubicacion_guardar = "C:/Users/nicol/Desktop/Proyecto #4/dataset_limpio/"
dataset_salario_minimo = "Salario minimo.txt"
dataset_precio_big_mac = "Precio Big mac.txt"

#Variable con enlace para hacer la solicitud para sacar la moneda de cada pais
enlace = "https://restcountries.com/v3.1/name/"

#Convertimos los datasets en dataframe, agregamos unos parametros para avisarle a pandas que no tienen nombre las columnas y le agregamos los nombres
df_salario_minimo = pd.read_csv(Ubicacion+dataset_salario_minimo, header=None, names= ["Pais", "Salario minimo", "Fuente salario"], sep=";")
df_precio_big_mac = pd.read_csv(Ubicacion+dataset_precio_big_mac, header=None, names=["Pais", "Precio bigmac", "Fuente bigmac"], sep= ";")

##Limpieza
#Dividimos la columna precio bigmac para separarlo del signo
df_precio_big_mac[["eliminar", "Precio bigmac"]] = df_precio_big_mac["Precio bigmac"].str.split(n=1, expand=True) 
df_precio_big_mac.drop("eliminar", axis=1, inplace=True) #Eliminamos la columna 
df_precio_big_mac["Precio bigmac"] = df_precio_big_mac["Precio bigmac"].str.replace(".", "") #Reemplazamos "." por ","
df_precio_big_mac["Precio bigmac"] = df_precio_big_mac["Precio bigmac"].str.replace(",", ".") #Reemplazamos "," por "."
df_precio_big_mac["Fecha"] = dt.date.today() #Agregamos la fecha actual

#Repetimos limpieza
df_salario_minimo[["eliminar", "Salario minimo"]] = df_salario_minimo["Salario minimo"].str.split(n=1, expand=True)
df_salario_minimo.drop("eliminar", axis=1, inplace=True)
df_salario_minimo["Salario minimo"] = df_salario_minimo["Salario minimo"].str.replace(".", "")
df_salario_minimo["Salario minimo"] = df_salario_minimo["Salario minimo"].str.replace(",", ".")
df_salario_minimo = df_salario_minimo[["Salario minimo", "Fuente salario"]] #Filtramos las columnas que vamos a necesitar

#Union de los dataframes
df_final = pd.concat([df_precio_big_mac, df_salario_minimo], axis=1)


#Convertimos las columnas a numero flotante
df_final["Precio bigmac"] = df_final["Precio bigmac"].astype(float)
df_final["Salario minimo"] = df_final["Salario minimo"].astype(float)

##Creamos un bucle para agregar una columna con la moneda de cada pais
#Variables que se utilizaran en el bucle
cantidad_filas = df_final["Pais"].count() - 1
fila_inicial = 0 
df_final["Moneda"] = "No hay datos"

#Inicio del bucle
while fila_inicial <= cantidad_filas:
     nombre_pais = df_final["Pais"][fila_inicial] #Creamos una variable que obtendra el nombre de cada pais
     enlace_solicitud = enlace+nombre_pais #Sumamos el enlace con el nombre del pais
     solicitud = requests.get(enlace_solicitud) #Enviamos la solicitud     
     #Creamos una condicion para verificar si hay un error en la solicitud, caso contrario, sigue el proceso
     if solicitud == 404:
         print("Error, no se encontro la moneda del pais:", nombre_pais)
         fila_inicial += 1
     else:
         respuesta = solicitud.json()          
         #Lo convertimos en dataframe
         df  = pd.json_normalize(respuesta)
         moneda = df.columns[df.columns.str.startswith("currencies")] #Buscamos las columnas que comiencen con cierta palabra
         moneda = moneda[0] #Dejamos solo el primero
         moneda = moneda[11:] #Seleccionamos todas la palabra despues de las primeras 11 letras
         moneda = moneda[0:3] #seleccionamos las primeras 3 palabras
         df_final.loc[fila_inicial, "Moneda"] = moneda #Agregamos el nombre de la moneda
         time.sleep(2) #Agregamos un tiempo de espera de 3 segundos para continuar 
         fila_inicial += 1

#Cambiamos la moneda de venezuela a dolar porque los dataset tiene el salario y precio en esa moneda.        
df_final.loc[7, "Moneda"] = "USD"

#Ordenamos las columnas
columns = ["Pais", "Moneda", "Precio bigmac", "Salario minimo", "Fecha", "Fuente salario", "Fuente bigmac"]
df_final = df_final[columns]

#Lo guardamos en formato csv
df_final.to_csv(Ubicacion_guardar+"dataset_limpio", index=False)






















