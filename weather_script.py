import requests

def obtener_clima(ciudad, api_key):
    """
    Devuelve datos del clima desde OpenWeatherMap para la ciudad especificada.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def main():
    ciudad = input("Ingresa el nombre de la ciudad: ")
    api_key = "ea7c20257f0887baafef3b6970588e44"  # Reemplaza con tu API Key de OpenWeatherMap
    datos_clima = obtener_clima(ciudad, api_key)
    if datos_clima:
        print(f"Ciudad: {datos_clima['name']}")
        print(f"Temperatura: {datos_clima['main']['temp']}°C")
        print(f"Descripción: {datos_clima['weather'][0]['description']}")
    else:
        print("No fue posible obtener datos del clima.")

if __name__ == "__main__":
    main()