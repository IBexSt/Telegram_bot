import telebot
from telebot import types

exstasy = 0
imlive = 0
secretfriends = 0

bot = telebot.TeleBot('5319859431:AAH9lk9ibeuA8tWzcxFZ7A963hZXTA-ypSQ')

@bot.message_handler(func=lambda message: message.text == 'Указать заработок за день 💸')
def money(message):
    send_mess = "Хорошо, давай посчитаем exstasy ✏: "
    bot.send_message(message.chat.id, send_mess)
    bot.register_next_step_handler(message, vol1)

def vol1(message):
    global exstasy
    exstasy = str(message.text)
    send_mess = "Спасибо, теперь imLive: "
    bot.send_message(message.chat.id, send_mess)
    bot.register_next_step_handler(message, vol2)


def vol2(message):
    global imlive
    imlive = str(message.text)
    send_mess = "Спасибо, теперь SecretFriends: "
    bot.send_message(message.chat.id, send_mess)
    bot.register_next_step_handler(message, vol3)

def vol3(message):
    global secretfriends
    secretfriends = str(message.text)
    end_vol = "У тебя: " + str(exstasy) + str(imlive) + str(secretfriends) + " ?"
    bot.send_message(message.from_user.id, end_vol)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Указать заработок за день 💸')
btn2 = types.KeyboardButton('Узнать о бонусах 💰')
btn3 = types.KeyboardButton('FAQ ❓')
markup.add(btn1, btn2, btn3)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Можно ли курить перед камерой?')
btn2 = types.KeyboardButton('Я плохо знаю английский, что делать?')
btn3 = types.KeyboardButton('Хочу уйти на удаленную работу')
btn4 = types.KeyboardButton('Штрафы')
btn5 = types.KeyboardButton('Назад')
markup3.add(btn1, btn2, btn3, btn4, btn5)

#markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#btn1 = types.KeyboardButton('Назад')
#markup4.add(btn1)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    username = message.from_user.username
    bot.send_message(message.chat.id, "Давай начнем!", reply_markup=markup)
    send_mess = f"Привет, {username}! Я твой личный помощник!"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'FAQ ❓')
def foo(message):
    send_mess = "Что тебя интересует?"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Можно ли курить перед камерой?')
def foo2(message):
    final_message = "К сожалению не все сайты одобряют курение моделей перед камерой, а так как наша работа заключена на нескольких сайтах одновременно, то курить перед камерой становится строго запрещено!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Я плохо знаю английский, что делать?')
def foo3(message):
    final_message = "Не переживай если тебе приходится много отвлекаться на переводчик, в скором времени у нас в штате будет преподаватель Английского языка, он будет заниматься и обучать нас основам, чтоб бы тебе было комфортно отвечать на банальные вопросы и общаться с несколькими мемберами сразу!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Хочу уйти на удаленную работу')
def foo4(message):
    final_message = "Мы с радостью поддерживаем моделей, которые хотят уйти на удаленную работу и не тратить время на поездки в студию. Но чтобы уйти работать удаленно, тебе необходимо выполнить несколько обязательных пунктов: \n 1. Опыт работы на студии Muskad от 1 года и более \n 2. Дома есть оборудованное место (Хотя бы хороший свет и яркая привлекательная комната, ноутбук и камеру мы можем дать в аренду)"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Штрафы')
def foo5(message):
    final_message = "Прогул рабочего дня наказывается штрафом, как бы сурово это не было, выгоду теряете не только вы. Штраф расчитывается индивидуально и составляет от 3 000р до 6 000р в сутки. Прогул по уважительной причине (есть справка), штрафом не облагается."
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def foo6(message):
    final_message = "Главное меню"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Узнать о бонусах 💰")
def foo7(message):
    final_message = "У нас действует предложение, если твоя подруга хочет вступить к нам в команду, то мы с радостью рассмотрим ее кандидатуру, а тебе будет положен бонус 5 000₽. Но есть одно условие, твоя подруга должна пройти испытательный срок равный 1 месяцу. "
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
