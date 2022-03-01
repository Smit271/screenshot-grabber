import requests

class Login():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.url = "http://testqaweb.com/screenshot/api/Auth/login"

    def login(self):
        payload={'username': self.username,'password': self.password}
        print(payload)
        files=[

        ]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
        response = requests.post(self.url, headers=headers, data=payload, files=files)
        print(response)
        # print(response.json())
        # print(response.text)
        return response.json()