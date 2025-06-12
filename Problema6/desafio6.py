import requests
import mysql.connector
from datetime import datetime

# Coordenadas do Rio de Janeiro
latitude = -22.9068
longitude = -43.1729

# URL da API Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=surface_pressure&timezone=America%2FSao_Paulo"
)

# Requisição à API
response = requests.get(url)
data = response.json()

horarios = data["hourly"]["time"]
pressoes = data["hourly"]["surface_pressure"]

# Conexão com MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="your password",  
    database="clima"
)
cursor = conn.cursor()

# Comando SQL de inserção
sql = "INSERT INTO previsao_pressao_atm (momento, valor) VALUES (%s, %s)"

# Insere todos os registros
for momento, valor in zip(horarios, pressoes):
    momento_ts = datetime.fromisoformat(momento)
    cursor.execute(sql, (momento_ts, valor))

# Finaliza a transação
conn.commit()
cursor.close()
conn.close()

print("Dados inseridos com sucesso.")
