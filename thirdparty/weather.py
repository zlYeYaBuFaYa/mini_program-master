# coding=utf-8
from mini_program.settings import weather_api_url, weather_key

import os, sys, requests, json

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_program.settings")

def weather(cityname):
    """ 
        请求接口，查询天气
     """
    request_url = "{0}?cityname={1}&dtype=&format=&key={2}".format(
        weather_api_url, cityname, weather_key
    )
    response = requests.get(url=request_url)
    content_dic = json.loads(response.content.decode())
    result = content_dic["resultcode"]
    response = {}
    if result in ["200", 200]:
        today_content = content_dic["result"]["today"]
        response["city"] = today_content["city"]
        response["temperature"] = today_content["temperature"]
        response["weather"] = today_content["weather"]
        response["wind"] = today_content["wind"]
        response["week"] = today_content["week"]
        response["date_y"] = today_content["date_y"]
        response["dressing_advice"] = today_content["dressing_advice"]
    return response


if __name__ == "__main__":
    result = weather("郑州")
    print(result)
