# -*- coding:utf-8 -*-
from city import city
import requests

#cityname = raw_input('请输入你要查询的城市名（中文）')
cityname  = '武汉'
citycode = city.get(cityname)
if citycode:
    url = 'http://www.weather.com.cn/data/cityinfo/%s.html' %(citycode)
    r = requests.get(url)
    result_dict = r.json()['weatherinfo']
    str_temp = ("%s\n%s - %s") %(result_dict['weather'],result_dict['temp2'],result_dict['temp1'])
    print str_temp
