import requests


class Message: 
    def __init__(self, token):
        self.__token = token 
        self.__telegram_api_url = "https://api.telegram.org/bot{token}/{method}".format(
            token=self.__token, method="getUpdates"
        )
        
        self.__const_method()

    def __const_method(self):
        response = requests.get(
            self.__telegram_api_url
        )       

        self.response_json = response.json()

        self.cnt_of_responses = len(
            self.response_json['result']
        )

    def user_id(self):
        user_id = self.response_json['result'][self.cnt_of_responses-1]['message']['from']['id']
        
        return user_id #returns the latest user id that texted 
        
    def text(self):
        text = self.response_json

        return text #returns the latest message from user

