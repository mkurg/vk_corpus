import urllib3
import requests
import time

method_url = "https://api.vk.com/method/users.search"
pars = {"access_token":"ВАШ ТОКЕН ЗДЕСЬ",
"count":3,
"city":627,
"country":1,
"fields":"bdate,sex,occupation,education,universities",
"v":"5.89"}

otvet = requests.get(method_url, pars)
user_data = otvet.json()
# print(user_data)

wall_method = "https://api.vk.com/method/wall.get"
wall_pars = {"access_token":"ВАШ ТОКЕН ЗДЕСЬ", "filter": "owner", "count": 3,
"v":"5.89"}

for person in user_data["response"]["items"]:
    wall_pars["owner_id"] = person["id"]
    otvet_wall = requests.get(wall_method, wall_pars)
    otvet_data = otvet_wall.json()
    print(otvet_data)
    time.sleep(0.34)