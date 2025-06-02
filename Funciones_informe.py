#Libreria
import pandas as pd

#Funciones
def iniciar_dataframe():
    ubiacion = "/content/drive/MyDrive/Proyecto #3/dataset/"
    dataset = "dataset_final"
    df = pd.read_csv(ubiacion + dataset)
    return df

def metrica_salario_minimo(df):
    df.sort_values(by="Salario minimo (USD)", ascending=False, inplace=True)
    salario_minimo_mas_alto = df.head(1)
    salario_minimo_mas_bajo = df.tail(2)
    print("Salario Minimo (USD):")
    print("* Mayor:", salario_minimo_mas_alto["Pais"].iloc[0]+ " - " + str(salario_minimo_mas_alto["Salario minimo (USD)"].iloc[0]), "USD")
    print("* Menor:", salario_minimo_mas_bajo["Pais"].iloc[0]+ " - " + str(salario_minimo_mas_bajo["Salario minimo (USD)"].iloc[0]), "USD")
    print("* Promedio:", df["Salario minimo (USD)"].mean().round(2), "USD")
    return

def metrica_big_mac(df):
  df.sort_values(by="Precio bigmac (USD)", ascending=False, inplace=True)
  precio_bigmac_mas_alto = df.head(1)
  precio_bigmac_mas_bajo = df.tail(1)
  print("Precio Big Mac (USD):")
  print("* Mayor:", precio_bigmac_mas_alto["Pais"].iloc[0]+" - "+str(precio_bigmac_mas_alto["Precio bigmac (USD)"].iloc[0]), "USD")
  print("* Menor:", precio_bigmac_mas_bajo["Pais"].iloc[0]+" - "+str(precio_bigmac_mas_bajo["Precio bigmac (USD)"].iloc[0]), "USD")
  print("* Promedio:", df["Precio bigmac (USD)"].mean().round(2), "USD")
  return 

def metrica_cantidad_bigmac_x_salario(df):
  df.sort_values(by="Cantidad_bigmac_con_salario", ascending=False, inplace=True)
  cantidad_bigmac_mayor_x_salario = df.head(1)
  cantidad_bigmac_menor_x_salario = df.tail(2)
  print("Poder Adquisitivo:")
  print("* Mayor:", cantidad_bigmac_mayor_x_salario["Pais"].iloc[0]+" - "+str(cantidad_bigmac_mayor_x_salario["Cantidad_bigmac_con_salario"].iloc[0]), "Big mac")
  print("* Menor:", cantidad_bigmac_menor_x_salario["Pais"].iloc[0]+" - "+str(cantidad_bigmac_menor_x_salario["Cantidad_bigmac_con_salario"].iloc[0]), "Big Mac")
  print("* Promedio:", df["Cantidad_bigmac_con_salario"].mean().round(2), "Big Mac")
  return