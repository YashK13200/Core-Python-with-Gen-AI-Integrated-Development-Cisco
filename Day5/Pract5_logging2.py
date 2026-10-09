import logging

logging.basicConfig(level=logging.ERROR)


try:
    result = 10 / 0
except Exception as e:
    logging.error("An error occurred: %s", e)
    
    
