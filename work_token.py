
import requests
import json

client_id = 'c106a77ee4dda462f463'
client_secret = '3aa6adfa54057aa5c4341152482a97ee'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)  # разбираем ответ сервера
token = j["token"]  # достаем токен
headers = {"X-Xapp-Token": token}  # создаем заголовок, содержащий наш токен

f = open("text.txt", "r")  # открыть файл на чтение
lst = []
for line in f:
    line = line.rstrip()
    template = 'https://api.artsy.net/api/artists/{}'
    r = requests.get(template.format(line), headers=headers)  # инициируем запрос с заголовком
    r.encoding = 'utf-8'
    j = json.loads(r.text)  # разбираем ответ сервера
    lst.append(j)
f.close()

sorted_lst = sorted(lst, key=lambda person: (int(person['birthday']), person['sortable_name']))
for item in sorted_lst:
    print(item['sortable_name'])