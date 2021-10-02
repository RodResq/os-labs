import logging

logging.basicConfig(filename='my_program_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging modulo is working')
logging.warning('An error message is baout to be logged.')
logging.error('An error has occurred')
logging.critical('The program is unable to recover')
