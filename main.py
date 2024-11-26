# подключение библиотеки и создание бота
import telebot

bot = telebot.TeleBot('7291996150:AAF8eB2MdSBNE4HYXuNu90MTLguQ5zBTuw8')


# обработка команды старт3
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Если Вы не можете определиться со вкусом и дизайном торта, то данный бот поможет Вам!*', parse_mode = 'MarkDown')

@bot.message_handler(commands=['type'])
def main_1(message):
    bot.send_message(message.chat.id, 'Можете ознакомиться с прайсом и выбором начинки в социальной сети ниже поссылке [Перейти в каталог](https://www.instagram.com/novikova_av76?igsh=MXA0YjRrNnhvMzdvdQ==)', parse_mode = 'MarkDown')
    # проверка новых сообщений

bot.infinity_polling()