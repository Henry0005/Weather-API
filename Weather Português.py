import requests

API_KEY = "b7aedb8aa48fb59cf9f6c7eb405f0844"
cidade = "Sao Paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descrisao = requisicao_dic["weather"][0]['description']
temperatura = requisicao_dic['main']['temp']
cidade = requisicao_dic['name']
umidade = requisicao_dic['main']['humidity']
print (cidade ,descrisao, f"{temperatura}°C", f"Umidade relativa do ar {umidade}%")