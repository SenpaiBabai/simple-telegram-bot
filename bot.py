import requests
import time
from loguru import logger

from type import Event


class Bot:
    def __init__(self, token):
        self.__token = token 
        self.__telegram_api_url = "https://api.telegram.org/bot{token}/{method}".format(
            token=self.__token, method="{method}"
        )  

        logger.info("Верификация токена")
        self.__verify_token()
        logger.info("Верефикация токена успешна")

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
            logger.error("Верефикация токена не успешна")
            raise Exception("Токен бота не верен")

    def start_pooling(self):
        logger.info("Бот запускается")
        method_url = self.__telegram_api_url.format(
            method="getUpdates"
        )  
        while True:
            response = requests.get(
                method_url
            ) 
            events = response.json()["result"]

            for event in events:
                yield Event(**event)

