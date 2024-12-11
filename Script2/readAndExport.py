import pymongo
import pandas as pd

# Conectar a MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')  # Ajusta la URI si es necesario
db = client['bicis_db']  # Nombre de tu base de datos
collection = db['bicicorunha']  # Nombre de tu colección

# Obtener los datos de MongoDB
data = list(collection.find())

# Extraer los datos relevantes de cada estación
stations_data = []
for doc in data:
    network = doc.get('network', {})
    stations = network.get('stations', [])
    
    for station in stations:
        # Extraer los datos de la estación
        extra_data = station.get('extra', {})
        
        # Crear el diccionario con los datos de la estación y su red
        station_data = {
            'station_id': station.get('id'),
            'station_name': station.get('name'),
            'timestamp': station.get('timestamp'),
            'free_bikes': station.get('free_bikes'),
            'empty_slots': station.get('empty_slots'),
            'extra_uid': extra_data.get('uid'),
            'extra_last_updated': extra_data.get('last_updated'),
            'extra_slots': extra_data.get('slots'),
            'extra_normal_bikes': extra_data.get('normal_bikes'),
            'extra_ebikes': extra_data.get('ebikes'),
        }
        stations_data.append(station_data)

# Crear el DataFrame
df = pd.DataFrame(stations_data)

# Exportar el DataFrame a un archivo CSV y parquet
df.to_csv('bicicorunha_stations.csv', index=False)
df.to_parquet('bicicorunha_stations.parquet', index=False)

# Mostrar el DataFrame
print(df)