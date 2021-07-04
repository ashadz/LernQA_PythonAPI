import requests

class TestHeaders():
    def test_check_headers(self):
        response = requests.post("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        print(response.text)
        assert 'x-secret-homework-header' in response.headers
        tkn = response.headers['x-secret-homework-header']
        assert 'Some secret value' in tkn
