from bottie import Bottie
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    bot = Bottie()
    token = open('token').readline()
    bot.run(token)
