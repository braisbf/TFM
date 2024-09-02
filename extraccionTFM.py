import requests
import pymongo
import json
import datetime
#Conectarnos a la API de openweather


# firstCallSpain = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Spain&appid=ca36651aadc9aaa9652d0bec7184c909')

firstCallMadridHist = requests.get('https://history.openweathermap.org/data/2.5/history/city?q=Madrid&type=hour&start=1711839600&end=1712509489&appid=ca36651aadc9aaa9652d0bec7184c909')
client = pymongo.MongoClient("mongodb+srv://franciscoboccassi:1234567890@<cluster0.csyeqkh.mongodb.net/madrid?retryWrites=true&w=majority")
db = client.weather

# Formato deseado para la fecha y hora
formato_deseado = "%Y-%m-%d %H:%M:%S"
capitales_espana = [
    "Albacete",
    "Almeria",
    "Avila de los Caballeros",
    "Badajoz",
    "Barcelona",
    "Burgos",
    "Caceres",
    "Cadiz",
    "Castello de la Plana",
    "Ciudad Real",
    "Cordoba",
    "A Coruna",
    "Cuenca",
    "Girona",
    "Granada",
    "Guadalajara",
    "Huelva",
    "Huesca",
    "Jaen",
    "Leon",
    "Lleida",
    "Logrono",
    "Lugo",
    "Madrid",
    "Malaga",
    "Murcia",
    "Ourense",
    "Oviedo",
    "Palencia",
    "Las Palmas de Gran Canaria",
    "Pamplona",
    "Pontevedra",
    "Santander",
    "Segovia",
    "Sevilla",
    "Soria",
    "Tarragona",
    "Teruel",
    "Toledo",
    "Valencia",
    "Valladolid",
    "Vitoria-Gasteiz",
    "Zamora",
    "Zaragoza"
]






# Define el formato deseado para la fecha
formato_deseado = "%Y-%m-%d %H:%M:%S"

# Define el rango de fechas (1 de enero de 2024 a 14 de mayo de 2024)
start_date = datetime.datetime(2024, 6, 10)
end_date = datetime.datetime(2024, 8, 26)

# Define el intervalo de tiempo (una semana)
delta = datetime.timedelta(weeks=1)

# Itera sobre las ciudades
for city in capitales_espana:
    # Itera sobre las semanas
    current_date = start_date
    while current_date < end_date:
        # Define el rango de tiempo para esta semana
        start_unix = int(current_date.timestamp())
        end_unix = int((current_date + delta).timestamp())

        # Construye la URL de llamada a la API con los valores de inicio y fin actuales
        citycall = f'https://history.openweathermap.org/data/2.5/history/city?q={city},ES&type=hour&start={start_unix}&end={end_unix}&appid=ca36651aadc9aaa9652d0bec7184c909'
        
        # Realiza la llamada a la API
        result = requests.get(citycall)
        print(city)
        data = result.json()
        data_list = data['list']

        # Itera sobre los elementos del JSON
        for elemento in data_list:
            # Convertir el valor de tiempo Unix a objeto datetime
            tiempo_unix = elemento['dt']
            tiempo_datetime = datetime.datetime.fromtimestamp(tiempo_unix)
            
            # Formatear como string con el formato deseado
            tiempo_string = tiempo_datetime.strftime(formato_deseado)
            
            # Reemplazar el valor de tiempo en el JSON con el formato deseado
            elemento['datetime'] = tiempo_string
            elemento['city'] = city
            
        # Reemplaza '<nombre_de_tu_colección>' con el nombre de tu colección
        collection = db.data
        
        # Insertar datos en la colección
        # Suponiendo que tu JSON es un documento, puedes usar insert_one
        collection.insert_many(data_list)

        # Avanza a la siguiente semana
        current_date += delta


































for city in capitales_espana:
    citycall = 'https://history.openweathermap.org/data/2.5/history/city?q='+city+',ES&type=hour&start=1704067200&end=1715731200&appid=ca36651aadc9aaa9652d0bec7184c909'
    result = requests.get(citycall)
    print(city)
    data = result.json()
    data_list = data['list']

    # Iterar sobre los elementos del JSON
    for elemento in data_list:
        # Convertir el valor de tiempo Unix a objeto datetime
        tiempo_unix = elemento['dt']
        tiempo_datetime = datetime.datetime.fromtimestamp(tiempo_unix)
        
        # Formatear como string con el formato deseado
        tiempo_string = tiempo_datetime.strftime(formato_deseado)
        
        # Reemplazar el valor de tiempo en el JSON con el formato deseado
        elemento['datetime'] = tiempo_string
        elemento['city'] = city
        
    # Reemplaza '<nombre_de_tu_colección>' con el nombre de tu colección
    collection = db.data
    
    # Insertar datos en la colección
    # Suponiendo que tu JSON es un documento, puedes usar insert_one
    collection.insert_many(data_list)


#https://pro.openweathermap.org/data/2.5/forecast/climate?q={city name},{country code}&appid={API key}