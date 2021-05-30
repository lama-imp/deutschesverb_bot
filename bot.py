import telebot
from telebot import types
from SQLighter import SQLighter
from config import token
from verb_search import possible_answer, database_name


bot = telebot.TeleBot(token)

welcome_text = """
Приветствую, я бот для склонения немецких сильных глаголов.
Отправьте глагол, и я верну формы его склонения.
На данный момент в базе 197 сильных глаголов.
Если что-то непонятно, отправьте команду /help
"""
manual_text = """
Отправьте немецкий глагол в инфинитиве.
Если это сильный глагол, я выведу следующие его формы:
форму третьего лица единственного числа настоящего времени;
форму прошедшего времени (Präteritum);
второе причастие (Partizip II)
"""
return_variants_text = """
В моей базе данных нет такого глагола.
Возможно, вы имели в виду какой-то из этих глаголов:
"""
cannot_find_text = "В моей базе данных нет такого глагола"
wrong_content_text = "Это не текст. Отправьте текст."


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, welcome_text)


@bot.message_handler(commands=["help"])
def send_manual(message):
    bot.reply_to(message, manual_text)


@bot.message_handler(content_types=["text"])
def return_verb(message):
    db_worker = SQLighter(database_name)
    search_result = db_worker.find_verb(message.text.lower())
    if search_result is not None:
        markup = types.ReplyKeyboardRemove()
        answer = db_worker.give_answer(message.text.lower())
        print(answer)
        db_worker.close
        result = answer[1:]
        for i in result:
            bot.send_message(message.chat.id, i, reply_markup=markup)
    else:
        found_verbs = possible_answer(message)
        if len(found_verbs) > 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in found_verbs:
                markup.add(types.KeyboardButton(i))
            bot.send_message(
                message.chat.id,
                return_variants_text,
                reply_markup=markup)
        else:
            bot.send_message(
                message.chat.id, cannot_find_text)


@bot.message_handler(content_types=[
    "audio", "document", "photo", "sticker", "video"
])
def handle_wrong_content(message):
    bot.send_message(message.chat.id, wrong_content_text)
