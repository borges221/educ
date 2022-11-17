from time import sleep
import main
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (ContextTypes)

from datetime import datetime as dt


reply_keyboard_start = [["Калькулятор"],\
                        ["Вывод логов"],\
                        ["Выход"]]

markup_start = ReplyKeyboardMarkup(reply_keyboard_start, one_time_keyboard=True) 



def universal_logger(data, data_description = "действие"):
    """Функция логинит любые данные
    при вызове функциив в data_description подставляется строковое описание
    действия(например, 'ввод значения а', 'ввод значения в'), который 
    сопровождает появление переменной data) 
    """  
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('log_calc.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data))
                    
async def print_log (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('log_calc.csv', 'r', encoding='utf-8') as file:
        text_for_print = ""
        for line in file:
            text_for_print+= line
    await update.message.reply_text (text_for_print)
    sleep(1)
    await update.message.reply_text('Продолжим работу?\n\
Калькулятор\nВывод логов на экран\nВыход', reply_markup=markup_start)
    return main.main_menu