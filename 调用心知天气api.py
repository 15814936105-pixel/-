import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.seniverse.com/v3/weather/now.json?key={API_KEY}&location={city}&language=zh-Hans&unit=c"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

print(API_KEY)
city = input("请输入您要查询的城市:")
while(city):
    data = get_weather(city)
    name = data["results"][0]["location"]["name"]
    timezone = data["results"][0]["location"]["timezone"]
    temperature = data["results"][0]["now"]["temperature"]
    weather = data["results"][0]["now"]["text"]
    print(data,name,timezone,temperature,weather, sep="\n")
    city = input("请输入您要查询的城市:")

#字典，列表 字典 字典
#{'results': [{'location': {'id': 'WX4FBXXFKE4F', 'name': '北京', 'country': 'CN', 'path': '北京,北京,中国', 'timezone': 'Asia/Shanghai', 'timezone_offset': '+08:00'}, 'now': {'text': '大雨', 'code': '15', 'temperature': '13'}, 'last_update': '2026-10-17T12:14:05+08:00'}]}