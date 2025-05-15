## Proyecto #3 - Big Mac índice: Poder adquisitivo en Sudamérica (USD)

En este informe se analiza el poder adquisitivo de los países de Sudamérica (exceptuando Bolivia, Guyana y Surinam) tomando como referencia el salario mínimo y el precio de la Big Mac.

Se utilizó Python con varias librerías y APIs, para limpiar, construir pipelines, realizar transformaciones y presentar el dataset final.

La visualización se realizó en Looker Studio, acompañado de un informe en Google colab.

## librerías y tecnologías 

- Python: Lenguaje principal del proyecto.
- Pandas: Entrada, transformación y exportacion datasets.
- Request: Realizar solicitudes y obtener informacion.
- Time: Utilizado para agregar una pausa en cada solicitud.
- Datatime: Registrar fecha actual en el dataset.
- Apis: ExchangeRate API y Restcountries para obtener información de las monedas y tasas de cambio de cada pais con el par USD.
- Google colab: Presentar informe final.

## Visualización en Looker Studio

[LookerStudio](https://lookerstudio.google.com/s/rccHOEn4R-0)

## Presentacion del informe en Google Colab

[GoogleColab](https://colab.research.google.com/drive/1Zjd9Ua6E48vFH5-p_hgmECEo0ObhcABn?usp=sharing)

## Fuente de información - Big Mac

La información fue extraída generalmente de páginas oficiales de McDonald's. En algunos casos, se utilizó como segunda opcion la plataforma de delivery PedidosYa.
- [Argentina] (https://www.mcdonalds.com.ar/restaurantes/mendoza/colon-369-cmz/pedidos/pedi-y-retira/hamburguesas/big-mac)
- [Brasil] (https://www.mcdonalds.com.br/restaurantes/franca/franca-shopping-center-fra-fra/pedidos/peca-e-retire/sanduiches/big-mac)
- [Chile] (https://www.mcdonalds.cl/restaurantes/santiago/mall-arauco-maipu-patio-de-comida-ma1/pedidos/pickup/hamburguesas/big-mac)
- [Colombia] (https://www.mcdonalds.com.co/restaurantes/barranquilla/carrera-43-c43/pedidos/pickup/hamburguesas/big-mac)
- [Perú] (https://www.mcdonalds.com.pe/restaurantes/chiclayo/chiclayo-chi/pedidos/pide-y-retira/hamburguesas/big-mac)
- [Uruguay] (https://www.mcdonalds.com.uy/restaurantes/montevideo/18-de-julio-y-ejido-18e/pedidos/pickup/hamburguesas/big-mac)
- [Ecuador] (https://www.mcdonalds.com.ec/restaurantes/quito/mall-quicentro-sur-mqs/pedidos/pide-y-retira/hamburguesas/big-mac)
- [venezuela] (https://www.pedidosya.com.ve/restaurantes/caracas/mcdonalds-sabana-grande-0705dc41-b240-41db-ad82-9ddf8b946ce0-menu?p=128899332&menuSection=menu)
- [paraguay] (https://www.pedidosya.com.py/restaurantes/asuncion/mcdonalds-aviadores-fe2c57e6-f137-4165-8e86-8685d93391b0-menu?p=15598566&menuSection=menu)

## Fuente de información - Salario mínimo

La información fue extraída generalmente de páginas oficiales de los gobiernos. En algunos casos, se utilizó como segunda opcion algún diario local.
- [Argentina] (https://www.argentina.gob.ar/trabajo/consejodelsalario)
- [Brasil] (https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/04/presidente-sanciona-orcamento-de-2025-com-aumento-do-salario-minimo-para-r-1.518)
- [Chile] (https://www.mintrab.gob.cl/gobierno-y-la-cut-alcanzan-acuerdo-por-salario-minimo-529-000-a-partir-del-1-de-mayo-de-2025/)
- [Colombia] (https://www.presidencia.gov.co/prensa/Paginas/El-salario-minimo-para-2025-aumentara-el-9-54-porciento-y-queda-en-1423500-presidente-Gustavo-Petro-241224.aspx)
- [Perú] (https://www.gob.pe/institucion/presidencia/noticias/1082104-presidenta-boluarte-anuncia-aumento-de-la-remuneracion-minima-vital-a-1130-soles)
- [Uruguay] (https://www.gub.uy/ministerio-trabajo-seguridad-social/sites/ministerio-trabajo-seguridad-social/files/2025-01/SMN.pdf)
- [Ecuador] (https://ecuadorec.com/tabla-de-salarios-minimos-sectoriales-nuevos-valores/)
- [venezuela] (https://www.elcaribe.com.do/panorama/internacionales/salario-indexado-en-venezuela-2025-nuevo-monto-y-bonos/)
- [paraguay] (https://www.hoy.com.py/nacionales/2025/05/12/pena-confirma-que-subira-el-salario-minimo)











