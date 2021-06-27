import requests
import time

url_zapros = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url_zapros)
json_object = response.json()
print('json = ', json_object)
tkn = json_object['token']    # Выделяем значение поля "token" в объекте json
sec = json_object['seconds']    # Выделяем значение поля "seconds" в объекте json

print('tkn = ', tkn,'  sec = ', sec)

code = 400
while code != 200 or strtest != 'Job is ready':  # Это спасает от невзгод
    time.sleep(sec-4)
    response = requests.get(url_zapros, params={"token": tkn})
    json_object = response.json()
    print(response.status_code)
    code= response.status_code
    strtest = json_object['status']


if strtest != 'Job is ready':   # Или пишем strtest== 'Job is NOT ready'
    print(' fignua sluchilas')
else:
    str_res = json_object['result']
    print(' ')
    print('Result = ',str_res)