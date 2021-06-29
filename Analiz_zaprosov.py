import requests

parameters = ["POST", "PUT", "GET","HEAD","DELETE"]

print(' ')

for i in range(len(parameters)):
    url1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": parameters[i]})
    url2  = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": parameters[i]})
    url3  = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": parameters[i]})
    url4  = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": parameters[i]})
    url5  = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": parameters[i]})
    print(' i = ',i, '    param = ' ,parameters[i],' | ',url1.text,' | ',url2.text,' | ',url3.text,' | ',url4.text,' | ',url5.text,' |')

print(' ')