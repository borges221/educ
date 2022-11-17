import log
import main


from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)


x = 0
y = 0


reply_keyboard_action = [["Сложение"],\
                        ["Вычитание"],\
                        ["Умножение"],\
                        ["Деление"],\
                        ["Целочисленное деление"],\
                        ["Остаток от деления"],\
                        ["Главное меню"],\
                        ["Выход"]]

markup_action = ReplyKeyboardMarkup(reply_keyboard_action, one_time_keyboard=True)

async def int_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global x
    # context.user_data.clear()
    # a = update.message.text
    # context.user_data["choice"] = a
    # x = int(a)
    x = int(update.message.text)
    context.user_data["choice"] = x
    await update.message.reply_text('Введите число 2:')
    return main.int_num_two

async def int_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global y
    # context.user_data.clear()
    # b = update.message.text
    # context.user_data["choice"] = b
    # y = int(b)
    y = int(update.message.text)
    context.user_data["choice"] = y
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\\nВыход', reply_markup=markup_action)
    return main.action_menu


async def float_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите число 1:')
    global x
    a = update.message.text
    x = float(a)
    await update.message.reply_text('Введите число 2:')
    return float_num_2

async def float_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:    
    global y
    b = update.message.text
    y = float(b)
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return main.action_menu


async def complex_num_1 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global d_1
    d_1 = update.message.text
    d_1 = float(d_1)
    await update.message.reply_text('Введите мнимую часть числа 1:')
    return complex_num_2

async def complex_num_2 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global x
    m_1 = update.message.text
    m_1 = float(m_1)
    x = complex(d_1, m_1)
    await update.message.reply_text('Введите действительную часть числа 2:')
    return complex_num_3


async def complex_num_3 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global d_2
    d_2 = update.message.text
    d_2 = float(d_2)
    await update.message.reply_text('Введите мнимую часть числа 2:')
    return complex_num_4

async def complex_num_4 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global y
    m_2 = update.message.text
    m_2 = float(m_2)
    y = complex(d_2, m_2)
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return main.action_menu