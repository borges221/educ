import input_n
import log

def mult():
    mult_num = input_n.x * input_n.y
    log.universal_logger(mult_num, data_description = "Произведение")
    return mult_num