#conectarme a la API (coruña), cada 2 min y alamacenar los datos en mongodb
import requests 
import time
from pymongo import MongoClient


# URL de la API
url = "http://api.citybik.es/v2/networks/bicicorunha"
intervalo_minutos = 2 

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/') 
db = client['bicis_db']
collection = db['bicicorunha']  


# Función para hacer la solicitud a la API
def obtener_datos():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Almacenar datos en MongoDB
            collection.insert_one(data)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error al conectar a la API o a MongoDB: {e}")

        
# Bucle infinito para hacer la solicitud cada X minutos
while True:
    obtener_datos()
    time.sleep(intervalo_minutos * 60)  # Convertir minutos a segundos
