import telegram

token = "5974773326:AAE3W8a4EGAJ-dqoIt15r4fm0s258Vk-kKI"

bot = telegram.Bot(token=token)

bot.sendMessage(chat_id="5092859384", text="Hello World!")
