import logging
from logging import Logger
import sys

def set_log(name: str) -> Logger:
    log = logging.getLogger(name)
    log.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log