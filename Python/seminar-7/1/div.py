import input_n
import log
import excep


def float_div():
    div_float = input_n.x / input_n.y
    log.universal_logger(div_float, data_description = "Частное")
    return div_float


def floor_div():
    div_floor = input_n.x // input_n.y
    log.universal_logger(div_floor, data_description = "Целочисленное деление")
    return div_floor


def mod_div():
    div_mod = input_n.x % input_n.y
    log.universal_logger(div_mod, data_description = "Остаток от деления")
    return div_mod
