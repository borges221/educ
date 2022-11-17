import input_n
import log
import main
from time import sleep


from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)

result = 0

reply_keyboard_next_action = [["Продожить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]

markup_next_action = ReplyKeyboardMarkup(reply_keyboard_next_action, one_time_keyboard=True)


def float_div():
    global result
    result = input_n.x / input_n.y
    log.universal_logger(result, data_description = "Частное")
    return main.res_action


def floor_div():
    global result
    result = input_n.x // input_n.y
    log.universal_logger(result, data_description = "Целочисленное деление")
    return main.res_action


def mod_div():
    global result
    result = input_n.x % input_n.y
    log.universal_logger(result, data_description = "Остаток от деления")
    return main.res_action


def sub():
    global result
    result = input_n.x - input_n.y
    log.universal_logger(result, data_description = "Разность")    
    return main.res_action


def mult():
    global result
    result = input_n.x * input_n.y
    log.universal_logger(result, data_description = "Произведение")
    return main.res_action


async def summ (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global result
    result = input_n.x + input_n.y
    log.universal_logger(result, data_description = "Сумма")
    await update.message.reply_text(f'Сумма чисел {input_n.x} и {input_n.y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{input_n.x}" и "{input_n.y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return main.next_action

