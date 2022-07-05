import telebot
from telebot import types, TeleBot

exstasy = 0
imlive = 0
secretfriends = 0
mydirtyhobbies = 0
islive = 0
camcontacts = 0
vxmodels = 0
xmodels = 0

bot: TeleBot = telebot.TeleBot('Ключ изменен для демонстрации')


# При отправке "Указать заработок", начинается поочередный ввод данных пользователем, в переменные указанные в шапке
@bot.message_handler(func=lambda message: message.text == 'Сообщение изменено для демонстрации')
def money(message):
    send_mess = "Сообщение изменено для демонстрации "
    bot.send_message(message.chat.id, send_mess)
    bot.register_next_step_handler(message, vol1)


def vol1(message):
    global exstasy
# message.text.isdigit(): - Проверка на цифровой ввод целых чисел
    exstasy = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol2)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol1)


def vol2(message):
    global imlive
    imlive = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol3)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol2)


def vol3(message):
    global mydirtyhobbies
    mydirtyhobbies = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol4)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol3)


def vol4(message):
    global islive
    islive = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol5)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol4)


def vol5(message):
    global camcontacts
    camcontacts = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol6)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol5)


def vol6(message):
    global vxmodels
    vxmodels = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol7)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol6)


def vol7(message):
    global xmodels
    xmodels = message.text
    if message.text.isdigit():
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol8)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol7)


def vol8(message):
    global secretfriends
    secretfriends = message.text
    if message.text.isdigit():
        keyboard = types.InlineKeyboardMarkup()
        key_send = types.InlineKeyboardButton(text="Отправить", callback_data="send")
        keyboard.add(key_send)
        key_edit = types.InlineKeyboardButton(text="Редактировать", callback_data="edit")
        keyboard.add(key_edit)
        end_vol = "Все верно?\n" + "\nExstasy: " + str(exstasy) + "\nImLive: " + str(imlive) + "\nSecretFriends: " + str(secretfriends) + "\nIsLive (€): " + str(islive) + "\nMyDirtyHobbies: " + str(mydirtyhobbies) + "\nCamContacts: " + str(camcontacts) + "\nVxModels: " + str(vxmodels) + "\nXModels: " + str(xmodels)
        bot.send_message(message.from_user.id, text=end_vol, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol8)

# Обработчик функции callback_data после ответа (Отправить) или (Редактировать)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "send":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Статистика успешно отправлена")
    elif call.data == "edit":
# Ответ клиентскому приложению что информация получена
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Хорошо, заполним данные заново")
        send_mess = "Сообщение изменено для демонстрации"
        bot.send_message(call.message.chat.id, send_mess)
        bot.register_next_step_handler(call.message, vol1)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn2 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn3 = types.KeyboardButton('Сообщение изменено для демонстрации')
markup.add(btn1, btn2, btn3)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn2 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn3 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn4 = types.KeyboardButton('Сообщение изменено для демонстрации')
btn5 = types.KeyboardButton('Назад')
markup3.add(btn1, btn2, btn3, btn4, btn5)


# markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
# btn1 = types.KeyboardButton('Назад')
# markup4.add(btn1)


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


@bot.message_handler(func=lambda message: message.text == 'Сообщение изменено для демонстрации')
def foo2(message):
    final_message = "Сообщение изменено для демонстрации"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Сообщение изменено для демонстрации')
def foo3(message):
    final_message = "Сообщение изменено для демонстрации"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Сообщение изменено для демонстрации')
def foo4(message):
    final_message = "Сообщение изменено для демонстрации"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Сообщение изменено для демонстрации')
def foo5(message):
    final_message = "Сообщение изменено для демонстрации"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def foo6(message):
    final_message = "Главное меню"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Сообщение изменено для демонстрации")
def foo7(message):
    final_message = "Сообщение изменено для демонстрации"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
