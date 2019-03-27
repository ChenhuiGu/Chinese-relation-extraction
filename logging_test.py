import logging

# logging.basicConfig(level=logging.INFO,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.debug('this is debug')

logging.info('this is info')

logging.warning('this is a warning')

logging.error('this is a error')


from loguru import logger

logger.add('info.log',level="DEBUG")
logger.debug('this is debug,{},get back','program')

@logger.catch
def add():
    return 3/0

add()