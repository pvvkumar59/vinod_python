import logging

Log_Filename = 'example.log'

logging.basicConfig(filename=Log_Filename, level=logging.DEBUG)

logging.debug("This is a debugging file, write this to example.log")