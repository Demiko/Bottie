from bottie import Bottie
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='%s.log'%(time.strftime("%Y.%m.%d_%H.%M.%S")), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

if __name__ == '__main__':
    bot = Bottie(logger=logger)
    token = open('token').readline()
    bot.run(token)
