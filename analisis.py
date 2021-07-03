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
# zona_norte = df[df['Comuna'] == ['Independencia'] # otra forma de extraer las comunas
# Agrupar información sobre las casas de la zona norte
zona_norte = df[df['Comuna'].isin(['Conchalí', 'Independencia', 'Huechuraba', 'Quilicura', 'Recoleta'])]
# %% [markdown]
#### Ordenar desde las casas mas caras a las más baratas del sector Norte 
zona_norte = zona_norte.sort_values('Valor_CLP', ascending=False)
# Mostrar las Casas mas caras del sector Norte
casas_caras = zona_norte[['Comuna', 'Valor_CLP']] 
casas_caras.head(10)
# %% [markdown]
#### Casas con terrenos más grandes del sector norte
cantidad_terreno = zona_norte[['Comuna', 'Total_Superficie_M2']]
cantidad_terreno = cantidad_terreno.sort_values('Total_Superficie_M2', ascending=False)
cantidad_terreno.head(10)
# %% [markdown]
#### Casas más grandes por comuna 
casas_grandes = zona_norte[['Comuna', 'Superficie_Construida_M2']]
casas_grandes = casas_grandes.sort_values('Superficie_Construida_M2', ascending=False)
casas_grandes.head(10)
# %% [markdown]
## Valor promedio casas Santiago Norte
valor_promedio_casas_cpl = zona_norte['Valor_CLP'].mean()
valor_promedio_casas_cpl = valor_promedio_casas_cpl.round(1)
print('El valor promedio de las casas del sector Norte de Santiago es', valor_promedio_casas_cpl, ' pesos chilenos')
## Valor Promedio U.F 
valor_promedio_casas_uf = zona_norte['Valor_UF'].mean()
valor_promedio_casas_uf = valor_promedio_casas_uf.round(1)
print('El valor promedio de las casas del sector Norte de Santiago es', valor_promedio_casas_uf, ' U.F')
## La Casa más cara es
casa_cara = zona_norte['Valor_CLP'].max()
print('La casa con mayor precio del Sector Norte de Santiago cuesta ', casa_cara, ' de pesos chilenos')
## La Casa más barata es
casa_barata = zona_norte['Valor_CLP'].min()
print('La casa con menor precio del Sector Norte de Santiago cuesta ', casa_barata, ' de pesos chilenos')
# %% [markdown]
## Valor promedio casas Santiago Norte desagregado por comuna
valor_promedio_comunas = zona_norte.pivot_table(values='Valor_CLP', index='Comuna')
valor_promedio_comunas = valor_promedio_comunas.round(1)
print(valor_promedio_comunas)
# %% [markdown]
#### Corredoras de Propiedades comunes en el Sector Norte 
corredoras_comunes = zona_norte.drop_duplicates(subset=['Corredor', 'Comuna'])
corredoras_comunes = corredoras_comunes['Corredor'].value_counts(sort=True)
print(corredoras_comunes)
#%% [markdown]
## Resumen, Características Casas Zona Norte
caracteristicas_casas = zona_norte.pivot_table(values=['Total_Superficie_M2', 'N_Habitaciones', 'N_Baños', 'N_Estacionamientos'], index='Comuna', margins=True)
caracteristicas_casas = caracteristicas_casas.round(1)
print(caracteristicas_casas)