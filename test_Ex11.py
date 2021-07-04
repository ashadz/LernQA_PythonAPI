import requests

class TestCookie():
    def test_check_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(' response cookies = ',response.cookies)
        print(response.cookies.get_dict())
        assert 'HomeWork' in response.cookies
        tkn = response.cookies['HomeWork']
        assert 'hw_value' in tkn

