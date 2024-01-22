import telebot
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

token = '6723346366:AAHW2w9ZkAt8DPnNwVWBJMecyCXAMzgkW9U'
bot = telebot.TeleBot(token=token)

markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup.add(KeyboardButton('1'))
markup.add(KeyboardButton('2'))
markup.add(KeyboardButton('3'))

## Сценарий:
## Главный герой попал в странный мир, где он мог пойти в Лес, Деревню или Подземелье, в зависимости от его выбора, будут дальнейшии приключения!😨
def load_data():
    try:
        with open('players.json', "r") as f:
            data = json.load(f)
    except:
        data = {}
    return data


def save_data(data):
    with open('players.json', 'w') as f:
        json.dump(data, f)


@bot.message_handler(commands=['start'])
def wellcome(message):
    bot.send_message(message.chat.id, text='Добро пожаловать, ознакомьтесь с нашёй игров в /help')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Добро пожаловать в RPG игру в телеграмм боте, чтобы начать игру , напишите /game')


@bot.message_handler(commands=['game'])
def wellcome_game(message):
    user_id = message.chat.id
    mesg = bot.send_message(user_id, 'Придумайте никнейм')
    bot.register_next_step_handler(mesg, verify)


def verify(message):
    user_id = message.chat.id
    choice = message.text.lower()
    if choice == "/game":
        bot.send_message(user_id, text='не используйте / в вашем нике')
        wellcome_game(message)
    elif choice == "/start":
        bot.send_message(user_id, text='не используйте / в вашем нике')
        wellcome_game(message)
    elif choice == "/help":
        bot.send_message(user_id, text='не используйте / в вашем нике')
        wellcome_game(message)
    else:
        start_location(message)


def start_location(message):
    user_id = message.chat.id
    question = {
        "question": "Добро пожаловать в нашу RPG игру, сейчас вы находитесь на спавне\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}'
                                                  f'Куда вы хотите пойти?\n'
                                                  f'1. Подземелье\n'
                                                  f'2. В лес\n'
                                                  f'3. В деревню\n', reply_markup=markup)
    with open('start_location.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, location_handler)


def location_handler(message):
    user_id = message.chat.id
    choice = message.text.lower()

    if choice == "1":
        location1(message)
    elif choice == "2":
        location2(message)
    elif choice == "3":
        location3(message)
    else:
        bot.send_message(user_id, text="Данной локации не существует, попробуйте ещё раз.")
        start_location(message)


def location1(message):
    user_id = message.chat.id
    question = {
        "question": "Вы попали в огромное подземелье, кишащее кучей монстров\n"
                    " ваши действия:\n"
                    " 1. Взять в руки меч и идти сражаться\n"
                    " 2. Осторожно исследовать всё подземелье\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, location1_handler)


def location1_handler(message):
    user_id = message.chat.id
    choice = message.text.lower()

    if choice == "1":
        location1_1(message)
    elif choice == "2":
        location1_2(message)
    else:
        bot.send_message(user_id, text="Данного ответа не существует, попробуйте ещё раз")
        location1(message)


def location1_1(message):
    user_id = message.chat.id
    question = {
        "question": "Вы использовали меч, но на вас напал очень сильный монстр, и вы магическим образом переместились куда-то. Оказалось, что вас переместил к себе очень сильный маг, который научил вас колдовать. Вы быстро освоились и стали сильнейшим.\n"
                    "Вы победили😎"
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}')

    with open('location_1_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location1_2(message):
    user_id = message.chat.id
    question = {
        "question": "Вы осторожно исследовали всё подземелье, но вы заблудились. Вы продолжили бродить по всему подземелью, но выхода нигде не было. Но вдруг, вы нашли какую-то тайную комнату, в ней была куча сокровищь. Вы решили открыть сундук, но... Это была ловушка!!! Двери закрылись и вы остались в заточении на веки вечные.\n"
                    "Вы проиграли😭"
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}')

    with open('location_1_2.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)



def location2(message):
    user_id = message.chat.id
    question = {
        "question": "Вы попали в лес, в нём было очень темно и страшно😨, но вдруг, вы нашли какую-то хижину\n"
                    "Ваши действия:\n"
                    "1. Зайти в неё\n"
                    "2. Пройти мимо\n"
                    "3. Выйти из леса\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_2.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, location2_handler)


def location2_handler(message):
    user_id = message.chat.id
    choice = message.text.lower()

    if choice == "1":
        location2_1(message)
    elif choice == "2":
        location2_2(message)
    elif choice == "3":
        start_location(message)
    else:
        bot.send_message(user_id, text="Данного ответа не существует, попробуйте ещё раз")
        location2(message)


def location2_1(message):
    user_id = message.chat.id
    question = {
        "question": "В хижине было много вещей, вы очень разбогатели\n"
                    "Вы победили💰",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_2_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location2_2(message):
    user_id = message.chat.id
    question = {
        "question": "Вы решили продолжить свой путь, вдруг вы наткнулись на стаю волков, вы решили спрятоться, но вам это не помогло,\n"
                    "Вы проиграли🐺\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_2_2.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location3(message):
    user_id = message.chat.id
    question = {
        "question": "Вы пошли в деревню, там было много всего!\n"
                    "Ваши действия:\n"
                    "1. Пойти в торговую лавку\n"
                    "2. Пойти погулять по переулкам\n"
                    "3. Пойти в замок короля\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, location3_handler)


def location3_handler(message):
    user_id = message.chat.id
    choice = message.text.lower()

    if choice == "1":
        location3_1(message)
    elif choice == "2":
        location3_2(message)
    elif choice == "3":
        location3_3(message)
    else:
        bot.send_message(user_id, text="Данного ответа не существует, попробуйте ещё раз")
        location3(message)


def location3_1(message):
    user_id = message.chat.id
    question = {
        "question": "Вы пришли в торговую лавку\n"
                    "Ваши действия:\n"
                    "1. Продать всё не нужное\n"
                    "2. Купить вещей\n"
                    "3. Выйти из торговой лавки\n",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, location3_1_handler)


def location3_1_handler(message):
    user_id = message.chat.id
    choice = message.text.lower()

    if choice == "1":
        location3_1_1(message)
    elif choice == "2":
        location3_1_2(message)
    elif choice == "3":
        location3(message)
    else:
        bot.send_message(user_id, text="Данного ответа не существует, попробуйте ещё раз")
        location3_1(message)


def location3_1_1(message):
    user_id = message.chat.id
    question = {
        "question": "Вы продали все свои вещи и остались не счем, вы обеднели\n"
                    "Вы проиграли💸",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location3_1_2(message):
    user_id = message.chat.id
    question = {
        "question": "Вас очень сильно обобрали на деньги и вам не удалось купить ничего ценного\n"
                    "Вы проиграли💸",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3_1.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location3_2(message):
    user_id = message.chat.id
    question = {
        "question": "Вы бродили по тёмным переулкам, но вдруг, на вас напали грабители в чёрных масках, вам удалось сбежать, но вдруг, вы заметили, что они сняли маски и оказалось... Что это ваши друзья!!! Вы обрадывались и пошли гулять\n"
                    "Вы победили😎",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3_2.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def location3_3(message):
    user_id = message.chat.id
    question = {
        "question": "Вас не пустили стражи, но король решил впустить вас, оказалось, что король был знаком с тобой ещё со школы, вы весело болтали и развлекались!\n"
                    "Вы победили👑",
    }
    mesg = bot.send_message(user_id, text=f'{question["question"]}', reply_markup=markup)

    with open('location_3_3.jpg', 'rb') as photo_file:
        bot.send_photo(user_id, photo=photo_file)

    bot.register_next_step_handler(mesg, finally1)


def finally1(message):
    bot.send_message(message.chat.id, text="Спасибо что прошли данный RPG формат в боте телеграмм!😎")
    bot.send_message(message.chat.id, text="Игра завершена. Для начала новой игры, напишите команду /game")


bot.polling()
