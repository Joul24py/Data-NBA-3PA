import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web a la que queremos acceder
url = "https://www.basketball-reference.com/leagues/NBA_2023.html"

# Realizamos la petición HTTP a la URL
response = requests.get(url)

# Creamos un objeto BeautifulSoup a partir de la respuesta HTTP
soup = BeautifulSoup(response.content, "html.parser")

# Buscamos la tabla a partir de la etiqueta id
table = soup.find("table", {"id": "per_game-team"})

df = pd.read_html(str(table))[0]

df.to_csv('2023-StatsPerGame.csv')

# Buscamos la tabla a partir de la etiqueta id
table = soup.find("table", {"id": "per_game-team"})

df = pd.read_html(str(table))[0]

df.to_csv('2023-StatsPerGame.csv')