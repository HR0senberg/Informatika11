import telebot

bot = telebot.TeleBot("5600261398:AAG7GOLasGlGtG5Js9D-ViwftQ2W8shcF7c")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Здравствуйте! Я Гостевой бот. Вам нужна помощь? Я вышел на связь, чтобы ответить на любые вопросы и проблемы.')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
