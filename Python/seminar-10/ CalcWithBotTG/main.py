import input_n
import log
import excep
import actions_mod

from time import sleep
import logging
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
 
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(f"This example is not compatible with your current PTB version {TG_VER}. To view the "\
        f"{TG_VER} version of this bot, "\
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)



reply_keyboard_start = [["Калькулятор"],\
                        ["Вывод логов"],\
                        ["Выход"]]

reply_keyboard_choice_num = [["Целые"],\
                            ["Вещественные"],\
                            ["Комплексные"],\
                            ["Главное меню"],\
                            ["Выход"]]

reply_keyboard_action = [["Сложение"],\
                        ["Вычитание"],\
                        ["Умножение"],\
                        ["Деление"],\
                        ["Целочисленное деление"],\
                        ["Остаток от деления"],\
                        ["Главное меню"],\
                        ["Выход"]]

reply_keyboard_next_action = [["Продолжить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]

markup_start = ReplyKeyboardMarkup(reply_keyboard_start, one_time_keyboard=True)
markup_choice_num = ReplyKeyboardMarkup(reply_keyboard_choice_num, one_time_keyboard=True)
markup_action = ReplyKeyboardMarkup(reply_keyboard_action, one_time_keyboard=True)
markup_next_action = ReplyKeyboardMarkup(reply_keyboard_next_action, one_time_keyboard=True)


main_menu, numbers_menu, action_menu, end_prog,\
int_num_one, int_num_two, next_action, result_action,\
float_num_one, float_num_two, complex_num_one, complex_num_two,\
complex_num_three, complex_num_four = range(14)


type_menu_1 = ""
type_menu_2 = ""
type_menu_3 = ""
type_menu_4 = ""
answer = ""

result = 0
x = 0
y = 0

#### Интерфейс ####

async def main_m (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    clear_data()
    await update.message.reply_text('Выбери пункт меню или введите команду\nКалькулятор\nВывод логов\nВыход', reply_markup=markup_start)
    global type_menu_1
    type_menu_1 = update.message.text
    context.user_data["choice"] = type_menu_1
    return main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.universal_logger("Вход в программу", data_description = "Запуск")
    await update.message.reply_text('Добро пожаловать в программу-калькулятор🔥')
    sleep(1)
    await update.message.reply_text('Для начала работы выбери пункт меню или введите команду\nКалькулятор\nВывод логов\nВыход', reply_markup=markup_start)
    return main_menu
    

async def choice_num (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    clear_data()
    await update.message.reply_text ('С какими числами будем работать?\n\
Целые\nВещественные\nКомплексные\nГлавное меню\nВыход',reply_markup=markup_choice_num)
    global type_menu_2
    type_menu_2 = update.message.text
    return numbers_menu


async def number_menu_choice_complex (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Введите действительную часть числа 1:')
    return complex_num_one

async def number_menu_choice_int (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Введите число 1:')
    return int_num_one

async def number_menu_choice_float (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Введите число 1:')
    return float_num_one


async def res_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global type_menu_4
    type_menu_4 = update.message.text
    context.user_data["choice"] = type_menu_4
    return next_action


async def choice_action (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global type_menu_3
    type_menu_3 = update.message.text
    context.user_data["choice"] = type_menu_3
    if type_menu_3 == "Сложение" or type_menu_3 == "Вычитание" or type_menu_3 == "Умножение" or excep.excep_check_zero() is True:
        return action_menu
    else:
        return excep.excep_check_zero


async def repeat_same_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return action_menu


async def ending (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    log.universal_logger("по команде пользователя", data_description = "Выход") 
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]
    await update.message.reply_text(f"Выполнение программы завершено! Спасибо!", reply_markup=ReplyKeyboardRemove())
    clear_data()
    user_data.clear()
    return ConversationHandler.END


def clear_data():
    global type_menu_1
    type_menu_1 = ""
    global type_menu_2
    type_menu_2 = ""
    global type_menu_3
    type_menu_3 = ""
    global type_menu_4
    type_menu_4 = ""
    global answer
    answer = ""


#### Ввод чисел #####


async def int_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global x
    x = int(update.message.text)
    context.user_data["choice"] = x
    await update.message.reply_text('Введите число 2:')
    return int_num_two

async def int_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global y
    y = int(update.message.text)
    context.user_data["choice"] = y
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return action_menu

async def float_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global x
    x = float(update.message.text)
    context.user_data["choice"] = x
    await update.message.reply_text('Введите число 2:')
    return float_num_two

async def float_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global y
    y = float(update.message.text)
    context.user_data["choice"] = y
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return action_menu


async def complex_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global x_1
    x_1 = float(update.message.text)
    context.user_data["choice"] = x_1
    await update.message.reply_text('Введите мннимую часть числа 1:')
    return complex_num_two

async def complex_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global x
    x_2 = float(update.message.text)
    context.user_data["choice"] = x_2
    x = complex(x_1, x_2)
    await update.message.reply_text('Введите действительную часть числа 2:')
    return complex_num_three

async def complex_num_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global y_1
    y_1 = float(update.message.text)
    context.user_data["choice"] = y_1
    await update.message.reply_text('Введите мннимую часть числа 2:')
    return complex_num_four

async def complex_num_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    global y
    y_2 = float(update.message.text)
    context.user_data["choice"] = y_2
    y = complex(y_1, y_2)
    log.universal_logger((x,y), data_description = "Ввод данных")
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{x}" и "{y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nВыход', reply_markup=markup_action)
    return action_menu







#### Арифметические действия ####


async def summ (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x + y
    log.universal_logger(result, data_description = "Сумма")
    await update.message.reply_text(f'Сумма чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action


async def float_div(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x / y
    log.universal_logger(result, data_description = "Частное")
    await update.message.reply_text(f'Частное чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action


async def floor_div (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x // y
    log.universal_logger(result, data_description = "Целочисленное деление")
    await update.message.reply_text(f'Частное от целочисленного деления чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action


async def mod_div (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x % y
    log.universal_logger(result, data_description = "Остаток от деления")
    await update.message.reply_text(f'Остаток от деления чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action


async def sub (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x - y
    log.universal_logger(result, data_description = "Разность")    
    await update.message.reply_text(f'Разность чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action


async def mult (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global result
    result = x * y
    log.universal_logger(result, data_description = "Произведение")
    await update.message.reply_text(f'Произведение чисел {x} и {y} составляет {result}')
    sleep(1)
    await update.message.reply_text(f'Продолжить вычисления с числами "{x}" и "{y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    return next_action






    




def main() -> None:
    application = Application.builder().token("5700119796:AAGgdI8yBQOzkBCRKkAhz4DpxBH6FNxMRFU").build()
    conv_handler = ConversationHandler\
        \
        (entry_points=[CommandHandler("start", start)],\
        \
        states={main_menu: [MessageHandler(filters.Regex("^Калькулятор$"), choice_num),\
                            MessageHandler(filters.Regex("^Вывод логов$"), log.print_log),\
                            MessageHandler(filters.Regex("^Выход$"), ending)],\
                numbers_menu: [MessageHandler(filters.Regex("^Целые$"), number_menu_choice_int),
                               MessageHandler(filters.Regex("^Вещественные$"), number_menu_choice_float),\
                               MessageHandler(filters.Regex("^Комплексные$"), number_menu_choice_complex),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],\
                int_num_one: [MessageHandler(filters.TEXT & ~(filters.COMMAND), int_num_1)],\
                int_num_two: [MessageHandler(filters.TEXT & ~(filters.COMMAND), int_num_2)],\
                float_num_one: [MessageHandler(filters.TEXT & ~(filters.COMMAND), float_num_1)],\
                float_num_two: [MessageHandler(filters.TEXT & ~(filters.COMMAND), float_num_2)],\
                complex_num_one: [MessageHandler(filters.TEXT & ~(filters.COMMAND), complex_num_1)],\
                complex_num_two: [MessageHandler(filters.TEXT & ~(filters.COMMAND), complex_num_2)],\
                complex_num_three: [MessageHandler(filters.TEXT & ~(filters.COMMAND), complex_num_3)],\
                complex_num_four: [MessageHandler(filters.TEXT & ~(filters.COMMAND), complex_num_4)],\
                action_menu: [MessageHandler(filters.Regex("^Сложение$"), summ),\
                               MessageHandler(filters.Regex("^Вычитание$"), sub),\
                               MessageHandler(filters.Regex("^Умножение$"), mult),\
                               MessageHandler(filters.Regex("^Деление$"), float_div),\
                               MessageHandler(filters.Regex("^Целочисленное деление$"), floor_div),\
                               MessageHandler(filters.Regex("^Остаток от деления$"), mod_div),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],\
                next_action: [MessageHandler(filters.Regex("^Продолжить$"), repeat_same_num),\
                               MessageHandler(filters.Regex("^Новый ввод$"), choice_num),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)]},
                
        fallbacks=[MessageHandler(filters.Regex("^Выход$"), ending)])
 
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
