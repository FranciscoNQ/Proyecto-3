#Libreria
import pandas as pd


#Variables con ubicacion y nombres del dataset
ubicacion_entrada = "C:/Users/nicol/Desktop/Proyecto #4/dataset_limpio/"
ubicacion_salida = "C:/Users/nicol/Desktop/Proyecto #4/dataset_final/"
dataset_tipo_de_cambio = "dataset_tipo_de_cambio"
dataset_principal = "dataset_limpio"

#Abrimos y convertimos a dataframes
df_cambio = pd.read_csv(ubicacion_entrada+dataset_tipo_de_cambio)
df_principal = pd.read_csv(ubicacion_entrada+dataset_principal)

#Creamos columnas 
df_principal["Precio bigmac (USD)"] = 0.00
df_principal["Salario minimo (USD)"] = 0.00

#Convertimos la columna simbolo en indice
df_cambio.set_index("Simbolo", inplace=True)


#Creamos variables para iniciar bucle que convertira los salarios y precios en usd
cantidad_filas = df_principal["Pais"].count() - 1
fila_inicial = 0 

#Iniciamos el bucle y ponemos como condicion cantidad_filas para terminar. 
while fila_inicial <= cantidad_filas:
    moneda = df_principal["Moneda"][fila_inicial]
    consulta = df_cambio[df_cambio.index.str.contains(moneda)]
    
    #Creamos una condicion donde se va consultar si encontro la moneda en df_cambio
    #Si no la encuentra, se le sumara uno a la variable de fila_inicial, caso contrario, seguira con el proceso
    if consulta.empty:
        print("No se encontro la moneda", moneda)
        fila_inicial += 1
    else: 
        df_principal.loc[fila_inicial, "Precio bigmac (USD)"] = df_principal.loc[fila_inicial, "Precio bigmac"] / consulta.loc[moneda, "Numeros"]
        df_principal.loc[fila_inicial, "Salario minimo (USD)"] = df_principal.loc[fila_inicial, "Salario minimo"] / consulta.loc[moneda, "Numeros"]
        fila_inicial += 1
        
#Calculamos la cantidad de bigmac que podes comprar con el salario minimo
df_principal["Cantidad_bigmac_con_salario"] = df_principal["Salario minimo (USD)"] / df_principal["Precio bigmac (USD)"] 
        
#Redondeamos y dejamos los primeros 2 decimales
df_principal["Precio bigmac (USD)"] = df_principal["Precio bigmac (USD)"].round(2)
df_principal["Salario minimo (USD)"] = df_principal["Salario minimo (USD)"].round(2)
df_principal["Cantidad_bigmac_con_salario"] = df_principal["Cantidad_bigmac_con_salario"].round(2)
    
#Borramos la columnas de precio y salario minimo en la moneda local
df_principal.drop(["Precio bigmac", "Salario minimo"], axis=1, inplace=True)

#Ordenamos el dataframe
columns = ["Pais", "Moneda", "Precio bigmac (USD)", "Salario minimo (USD)", "Cantidad_bigmac_con_salario", "Fecha", "Fuente salario", "Fuente bigmac"]
df_principal = df_principal[columns]

#Guardamos 
df_principal.to_csv(ubicacion_salida+"dataset_final", index=False)
