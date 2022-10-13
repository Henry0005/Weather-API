import requests

API_KEY = "b7aedb8aa48fb59cf9f6c7eb405f0844"
city = "Sao Paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
description = requisicao_dic["weather"][0]['description']
temperature = requisicao_dic['main']['temp']
city = requisicao_dic['name']
humidity = requisicao_dic['main']['humidity']
print (city ,description, f"{temperature}°C", f"Relative humidity {humidity}%")