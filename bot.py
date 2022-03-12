import requests


TOKEN = 'YOUR TOKEN'
href_getUpdates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
content = requests.get(href_getUpdates)
cnt_of_requests = len(content.json()['result'])

while True:
    href_getUpdates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    content = requests.get(href_getUpdates)

    check_requests = cnt_of_requests
    cnt_of_requests = len(content.json()['result'])

    if cnt_of_requests > check_requests:
        message_text = content.json()['result'][cnt_of_requests-1]['message']['text']
        user_id = content.json()['result'][cnt_of_requests-1]['message']['from']['id']
        parameters = {'chat_id': user_id,'text': message_text}

        href_sendMessage = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        content2 = requests.get(href_sendMessage, params=parameters)
        print(content2.json())
                
