from urllib.request import urlopen
import json

def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + 
        city + "&appid=6f0bfb3232d4642285811d8fbe3fc9a8")
    result = sock.read()
    sock.close()

    weather = json.loads(result)

    return weather["main"]["temp"] -273.15

if __name__ == "__main__":
    user_city = input("Which city to check weather? ")
    degree = get_weather(user_city)    
    print(f"Weather in {user_city} is {degree:.2f}°C.")
