import logging

# logging configuration

# Determing which level to start your logging(debug,info,warning, error, critical)
# filename = where you want your logging to go to
# filemode= the mode in which you want to operate your file.we use 'w' so that we can overwrite the file everytime
# The normal logging output: INFO:root:info  which is [logging_level,name_of_logger,message]
# We can change the logging output using the format arguement asctime=human readable time
logging.basicConfig(level=logging.DEBUG,
                    filename='logging/log.log', filemode='w', format="%(asctime)s  -  %(levelname)s - %(message)s")

# including a varialible in a logging
num = 2
logging.debug(f"The value of num is {num}")

# including a stuck trace
try:
    1/0
except ZeroDivisionError as e:
    logging.exception('Zero Division Error')


logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
