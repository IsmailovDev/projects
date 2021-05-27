import telebot
import config
import json
import requests
bot = telebot.TeleBot(config.token)
def usertekshiruvi(id):
    try:
        bot.send_message(id,'Tekshiruv...')
        return 1
    except:
        return 0
def member(id):
    membernum = 0
    try:
        for channel in config.kanallar:
            print('http://api.telegram.org/bot'+str(config.token)+'/getChatMember?chat_id=@'+channel[1][12:]+'&user_id='+str(id))
            re=requests.get('http://api.telegram.org/bot'+str(config.token)+'/getChatMember?chat_id=@'+channel[1][13:]+'&user_id='+str(id))
            re = json.loads(re.text)
            if re["result"]["status"]=="left":
                pass
            else:
                membernum+=1
        if membernum == len(config.kanallar):
            return 1
        else:
            return 0
    except:
        print("Botda imkon yo`q")
