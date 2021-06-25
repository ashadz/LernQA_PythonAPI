import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

first_response = response.history
second_response = response

print(len(response.history))    # Количество редиректов
print(response.url)     # Вывод последнего url


