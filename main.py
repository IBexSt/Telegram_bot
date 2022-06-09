import telebot, time
from telebot import types, TeleBot

exstasy = 0
imlive = 0
secretfriends = 0
mydirtyhobbies = 0
islive = 0
camcontacts = 0
vxmodels = 0
xmodels = 0

bot: TeleBot = telebot.TeleBot('5319859431:AAH9lk9ibeuA8tWzcxFZ7A963hZXTA-ypSQ')

tconv = lambda x: time.strftime("%d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид (Переменная time_send выводит в формате 09.06.2022)

# При отправке "Указать заработок", начинается поочередный ввод данных пользователем, в переменные указанные в шапке
@bot.message_handler(func=lambda message: message.text == 'Указать заработок за день 💸')
def money(message):
    send_mess = "Хорошо, давай посчитаем exstasy ✏: "
    bot.send_message(message.chat.id, send_mess)
    bot.register_next_step_handler(message, vol1)


def vol1(message):
    global exstasy
    exstasy = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь ImLive: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol2)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol1)


def vol2(message):
    global imlive
    imlive = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь MyDirtyHobbies: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol3)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol2)


def vol3(message):
    global mydirtyhobbies
    mydirtyhobbies = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь IsLive €: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol4)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol3)


def vol4(message):
    global islive
    islive = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь CamContacts: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol5)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol4)


def vol5(message):
    global camcontacts
    camcontacts = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь VxModels: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol6)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol5)


def vol6(message):
    global vxmodels
    vxmodels = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь Xmodels: "
        bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, vol7)
    else:
        bot.send_message(message.chat.id, "Пожалуйста используй целые числа, например, если на сайте ты заработала 12,9. То округли до 12.")
        bot.register_next_step_handler(message, vol6)


def vol7(message):
    global xmodels
    xmodels = message.text
    if message.text.isdigit():
        send_mess = "Спасибо, теперь SecretFriends: "
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
        time_send = (tconv(message.date))
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
        send_mess = "Давай посчитаем exstasy ✏: "
        bot.send_message(call.message.chat.id, send_mess)
        bot.register_next_step_handler(call.message, vol1)


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
