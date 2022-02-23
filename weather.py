import re
import requests

apiKey = "8775bf099e83fd6c1987f58bc9b257a8"
baseUrl = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
requestUrl = f"{baseUrl}?appid={apiKey}&q={city}"

responce = requests.get(requestUrl)

if responce.status_code == 200:
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    print(f"The weather is: {weather}")
    print(f"The temperature is: {tempC} in Celcius and {tempF} in Fahrenheit")    
else:
    print("An error occured")

