import input_n
import log

def summ():
    sum_num = input_n.x + input_n.y
    log.universal_logger(sum_num, data_description = "Сумма")  
    return sum_num