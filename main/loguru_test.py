from loguru import logger

logger.add('debug.log',
           format='{time} {level} {message}',
           level='DEBUG', rotation='1 week', compression='zip')

logger.debug('Test')
logger.info('Test')
logger.error('Test')
