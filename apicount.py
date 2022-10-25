#!/usr/bin/python

#import re
import urllib.request
import json
from datetime import datetime
from time import sleep

# Есть три сервера "maria.ru", "rose.ru", "sina.ru", которые по GET-запросу отдают свою метрику. Напишите на вашем любимом скриптовом языке программирования (Ruby, Perl, PHP, Python, Groovy, . . .) программу, которая будет опрашивать три сервера каждую минуту и выводить в консоль эту метрику рядом с названием сервера.
#
# Формат запроса:
# GET http://servername/api/count
#
# Формат ответа:
# {"count": 42}
#
# Формат вывода:
# 2022-05-20 13:01:00 maria.ru 42
# 2022-05-20 13:01:00 rose.ru 43
# 2022-05-20 13:01:00 sina.ru 45
# 2022-05-20 13:02:00 maria.ru 32
# 2022-05-20 13:02:00 rose.ru 33
# 2022-05-20 13:02:00 sina.ru 34

servers = ('maria.ru', 'rose.ru', 'sina.ru')
apipath = '/api/count'

def doqueryapi():
    now = datetime.now()
    minute = now.strftime('%Y-%m-%d %H:%M:00')

    for site in servers:
        with urllib.request.urlopen('http://'+site+apipath) as response:
            html = response.read()
            json_response = json.loads(html.decode())
            count = json_response['count']
            print(minute, site, count)

if __name__ == '__main__':
    while True:
        doqueryapi()
        sleep(60)