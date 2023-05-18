# Importamos el módulo urllib.parse para realizar la codificación de URL
import urllib.parse  
# Importamos el módulo requests para hacer solicitudes HTTP
import requests  
# Importamos el módulo json para trabajar con datos JSON
import json  

# URL base de la API de MapQuest
main_api = "https://www.mapquestapi.com/directions/v2/route?"  
# Aquí ponemos nuestra key de mapquest
key = "xU9S841b4HVI8tUjysuIyNX9asCV8YUU"  

# Solicitamos al usuario la ciudad de origen y destino
orig = input("Ingresa la ciudad de origen: ")
dest = input("Ingresa la ciudad de destino: ")

# Construimos la URL completa de la solicitud de ruta utilizando la URL base y codificando los parámetros necesarios como por ejemplo que arroje la narrativa del viaje en español
url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "locale": "es_ES", "unit": "k"})

# Realizamos la solicitud GET a la API de MapQuest y obtiene los datos de respuesta en formato JSON
jsondata = requests.get(url).json()

# Extraemos la distancia en kilómetros de los datos JSON
distancia_km = jsondata['route']['distance']

# Aquí se obtiene el tiempo de viaje en segundos de los datos JSON
tiempo_viaje_segundos = jsondata['route']['time']

# Esta cadena convierte el tiempo de viaje de segundos a horas, minutos y segundos
tiempo_viaje_horas = tiempo_viaje_segundos // 3600
tiempo_viaje_minutos = (tiempo_viaje_segundos % 3600) // 60
tiempo_viaje_segundos = tiempo_viaje_segundos % 60

# Aquí se convierten los datos JSON en una cadena con formato JSON
json_formateado = json.dumps(jsondata, indent=2)

# Imprimimos la distancia, origen, destino y duración del viaje
print(f"Distancia: {distancia_km} kilómetros")
print(f"Origen: {orig}")
print(f"Destino: {dest}")
print(f"Duración del viaje: {tiempo_viaje_horas} horas, {tiempo_viaje_minutos} minutos, {tiempo_viaje_segundos} segundos")

# Para concluir imprimimos la narrativa del viaje
print("\nNarrativa de la ruta:")
for leg in jsondata['route']['legs']:
    print(f"\nSalida: {leg['origNarrative']}.")
    for man in leg['maneuvers']:
        print(f"- {man['narrative']}.")
    print(f"Llegada: {leg['destNarrative']}.")