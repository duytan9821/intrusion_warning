import telegram


def send_telegram(photo_path="alert.png"):
    try:
        my_token = "5974773326:AAE3W8a4EGAJ-dqoIt15r4fm0s258Vk-kKI"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="5092859384", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")
