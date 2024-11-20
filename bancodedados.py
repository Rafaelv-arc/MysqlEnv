import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv("dot.env")

try:
    # Lê as variáveis de ambiente do arquivo .env
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        use_pure=True
    )
    
    if connection.is_connected():
        print("Conexão ao MySQL bem-sucedida!")
        # Exemplo de consulta
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()
        print(f"Conectado ao banco de dados: {db[0]}")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexão encerrada.")
