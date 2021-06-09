# %%
import pandas as pd
# %%
df = pd.read_excel('casa.xlsx', engine='openpyxl')
# %% [markdown]
### Exploración General
df.head()
# %%
df.info()  # Nombre de las columnas y tipos de datos 
#%%
df.shape   # Para saber el número de filas y columnas
#%%
df.describe()  # Para saber estadísticas generales del DataFrame
#%%
df.values  # arroja los datos en forma de matriz de numpy
#%%
df.columns  # Arroja los títulos de las columnas
# %%
df.index  # contiene los números de filas o los nombres de estas
# %% [markdown]
### Limpieza de datos
df.drop(columns=['Link', 'Tipo_Vivienda'], inplace=True)  # Borra la columna link y tipo vivienda
# Inplace=True sirve para que reemplaze los cambios en el df original
# %% [markdown]
### Analísis Casas Sector Norte Santiago 
#### Comunas: Conchalí, Huechuraba, Independencia, Recoleta y Quilicura
casas_conchali = df.iloc[78:98]
# %%
casas_huechuraba = df.loc[133:159]
casas_independencia = df.loc[160:182]
casas_recoleta = df.loc[903:927]
casas_quilicura = df.loc[842:891]
# %% [markdown]
### Extracción de la Información:
#### Número de habitaciones, superficie y valor en cada comuna del Sector Norte
casas_independencia.iloc[:,[0, 3, 6, 9]]  # extrae las habitaciones, superficie y valor
# %%
casas_huechuraba.iloc[:,[0, 3, 6, 9]]  # extrae las habitaciones, superficie y valor
# %%
casas_conchali.iloc[:,[0, 3, 6, 9]]  # extrae las habitaciones, superficie y valor
# %%
# ideas sacar el valor promedio de casas por comuna
# sacar las habitaciones promedio y la superficie promedio
# limpiar los datos que no usaré como u.f
# comparar el los promedios de las casas del sector norte de la capital
# Conchalí, Huechuraba, Independencia, Recoleta, Quilicura
# Probar fucion dataframe.groupby('nombre columna) para seleccionar valores especificos
# Probar casas_conchali.groupby('Valor_CLP') no funcionó xd


# %%
# Juntar todos los datos de las comunas de la zona norte de Santiago y 
# Ordenar las columnas para saber las casas mas caras, las con más habitaciones, etc.
# Eso se debería poder hacer con el método  .sort_values('nombre columa')


# %%
# zona_norte = df[df['Comuna'] == ['Independencia'] # otra forma de extraer las comunas
# Buscar la forma de juntar en un dataframe todas las comunas del sector norte
zona_norte = df[df['Comuna'].isin(['Conchalí', 'Independencia', 'Huechuraba', 'Quilicura', 'Recoleta'])]
# %%
# Ordenar las desde las casas mas caras a las mas baratas del sector Norte 
zona_norte = zona_norte.sort_values('Valor_CLP', ascending=False)
# Mostrar las Casas mas caras del sector Norte
casas_caras = zona_norte[['Comuna', 'Valor_CLP']] 
casas_caras.head(10)
# %%
# Casas con terrenos grandes
cantidad_terreno = zona_norte[['Comuna', 'Total_Superficie_M2']]
cantidad_terreno = cantidad_terreno.sort_values('Total_Superficie_M2', ascending=False)
cantidad_terreno.head(10)
# %%
# Casas mas grandes por comuna 
casas_grandes = zona_norte[['Comuna', 'Superficie_Construida_M2']]
casas_grandes = casas_grandes.sort_values('Superficie_Construida_M2', ascending=False)
casas_grandes.head(10)

# %%
# Idea saber cuantas corredoras de propiedades hay en el sector norte o en las comunas
# Para esto tendriamos que eliminar los duplicados con .drop_duplicates(subset='nombre_corredora')

# %%
# Otra Idea: aplicar estadisticas en el dataframe .mean() , . median(), mode(), etc