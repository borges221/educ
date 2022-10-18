import input_n
import log

def sub():
    sub_num = input_n.x - input_n.y
    log.universal_logger(sub_num, data_description = "Разность")    
    return sub_num