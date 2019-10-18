import logging


def setup_custom_logger(name):

    # create logger
    logger_name = name
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create file handler
    log_path = "log/logger.log"
    fh = logging.FileHandler(filename=log_path, mode='a')

    # create formatter
    fmt = '''--------------------------------------------
%(asctime)s
$(levelname)s - file: %(filename)s
module: %(module)s - line: %(lineno)d - process: %(process)d
message: %(message)s
--------------------------------------------'''

    datefmt = '%Y/%m/%d %H:%M:%S'
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    # add handler and formatter to logger
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
