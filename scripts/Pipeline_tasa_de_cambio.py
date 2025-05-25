#Librerias
import pandas as pd
import requests 

#Variables con enlace y apikey para hacer la solicitud
enlace_solicitud = "https://v6.exchangerate-api.com/v6/707b2206328205b99ea92a3b/latest/USD"

#Variables con ubicacion y nombre del dataset
ubicacion_carpeta = "C:/Users/nicol/Desktop/Proyecto #4/dataset_limpio/"

#Hacemos la solicitud para conseguir el tipo de cambio de usd de varios paises
solicitud = requests.get(enlace_solicitud)
respuesta = solicitud.json()

#Lo convertimos a dataframe
df_solicitudes = pd.json_normalize(respuesta["conversion_rates"]) 

#Convertimos todas las columnas y la primera fila a listas
lista = df_solicitudes.columns.tolist()
lista_2 = df_solicitudes.loc[0,:].tolist()

#Creamos un diccionario
diccionario = {"Simbolo": lista,
               "Numeros": lista_2}

#Lo convertimos en dataframe
df_datos_tipo_de_cambio = pd.DataFrame(diccionario)

#Lo guardamos en formato csv
df_datos_tipo_de_cambio.to_csv(ubicacion_carpeta+"dataset_tipo_de_cambio", index=False)


