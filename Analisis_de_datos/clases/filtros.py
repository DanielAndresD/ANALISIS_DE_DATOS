import pandas as pd
import numpy as np
import seaborn as sns #Libería para cargar conjuntos de datos

#Cargar bases de datos limpias utilizando seaborn
propinas=sns.load_dataset('tips')

mujeres_propinas=propinas[(propinas['sex']=='Female')and (propinas['tip']>=2)]
print(mujeres_propinas.shape)
print(mujeres_propinas)
