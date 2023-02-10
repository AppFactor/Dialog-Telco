import requests

class LoginAPI:
    def __init__(self) -> None:
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/login"

        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "username": "saranga99",
                "password": "Saranga@1234"
        }
        return _body

    def make_login_request(self):
        response = self.session.post(self.BASE_URL, json=self.req_body)
        return response.json()

login = LoginAPI()
print(login.make_login_request())
