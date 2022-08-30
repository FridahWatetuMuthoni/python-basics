from cgitb import handler
import logging
# if the logger exists it will give it to you but if it does not it will be created
# __name__ is the name of the current module
logging.basicConfig(level=logging.DEBUG,
                    filename='logging/log.log', filemode='w', format="%(asctime)s  -  %(levelname)s - %(message)s")


# if you want the logging to go to a seperate file use handler
logger = logging.getLogger(__name__)

handler = logging.FileHandler('logging/test.log')
formatter = logging.Formatter(
    "%(asctime)s  - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('test the custom logger')
