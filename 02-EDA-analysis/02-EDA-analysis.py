import pandas as pd
import numpy as np

# Lee el CSV en un DataFrame de Pandas
df = pd.read_csv("../01-data/2023-StatsPerGame.csv")

# Filtra las columnas que no sean numéricas
df = df.select_dtypes(include=[np.number])

df = df.drop('G', axis=1)

# Calcula la correlación de Pearson de cada par de columnas
correlations = df.corr(method="pearson")



# Visualiza los resultados de la correlación
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

matrix = ax.matshow(correlations, cmap = 'spring')

fig.colorbar(matrix)

ax.set_xticks(range(len(list(df.columns))))
ax.set_xticklabels(list(df.columns))

ax.set_yticks(range(len(list(df.columns))))
ax.set_yticklabels(list(df.columns))

fig.show()