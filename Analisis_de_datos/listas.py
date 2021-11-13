import pandas as pd
import numpy as np
import seaborn as sns #Libería para cargar conjuntos de datos

#Cargar bases de datos limpias utilizando seaborn
propinas=sns.load_dataset('tips')
print('Devuelve la información del conjunto de datos')
print(propinas.info())#Devuelve la información del conjunto de datos
print('uestra los primeros n registro')
print(propinas.head(10))# Muestra los primeros n registros
print('Estadistica descriptiva de variables numéricas')
print(propinas.describe())#Estadistica descriptiva de variables numéricas

propinas_cate=propinas[['sex','smoker','day','time']]#Selecciona solo un conjunto de datos
print('Describe la informacion de variables categoricas')
print(propinas_cate.describe())#Describe la informacion d evariables categoricas
print('Muestra los valores únicos de un campo')
print("sexo:",propinas_cate['sex'].unique())#Muestra los valores únicos de un campo
print("smoker: ",propinas_cate['smoker'].unique())
print("dia: ",propinas_cate['day'].unique())
print("time: ",propinas_cate['time'].unique())

#Estadistica descriptiva de un solo campo
print(propinas['size'].mean())
