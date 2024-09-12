import logging
import datetime
from os.path import exists
from os import mkdir

if not exists('logs'):
    mkdir('logs')

if not exists(f"logs/{datetime.date.today()}.log"):
    open(f"logs/{datetime.date.today()}.log", 'w').close()

logging.basicConfig(filename=f"logs/{datetime.date.today()}.log",
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    filemode='a')

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
