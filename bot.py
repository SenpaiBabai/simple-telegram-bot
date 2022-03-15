import requests
import time


class Bot:
    def __init__(self, token): 
        self.__token = token 
        self.__telegram_api_url = "https://api.telegram.org/bot{token}/{method}".format(
            token=self.__token, method="{method}"
        )  

        self.__verify_token()

    def get_me(self):
        method_url = self.__telegram_api_url.format(method="getMe")

        response = requests.get(
            method_url
        )  

        response_json = response.json()

        return response_json

    def __verify_token(self):
        token_status = self.get_me()["ok"]
        if not token_status:
            raise Exception("Токен бота не верен")

    def start_pooling(self):
        method_url = self.__telegram_api_url.format(
            method="getUpdates"
        )  
        while True:
            response = requests.get(
                method_url
            ) 
            response_json = response.json()
            yield response_json
            time.sleep(3)

