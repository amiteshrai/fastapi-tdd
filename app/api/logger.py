"""
    Logger Module

    This module is responsible for defining logging into application.
    The module exposes a function 'get_logger' which accepts inputs for
    configuring the logger instance.
    The inputs to the 'get_logger' function are:
        - name: The name of the logger
        - debug: A boolean flag to indicate if debug mode is enabled or not.
        - filepath: The path of the log file where the logger output will be
          appended.
"""

import logging


def get_logger(
        name='uvicorn',
        log_path='uvicorn.log',
        err_path='uvicorn.err.log',
        debug=False
):
    """
    Creates and logger instance and configures it with log format and the file
    names for different log levels

    Arguments:
        name {string} -- The name of the module which is instantiating the
        logger instance
        filepath {string}: The log filepath where the log output will be
        appended. Default to a file in current directory
        debug {bool}: Boolean flag to indicate if the the log output will be
        printed to the terminal or not

    Returns:
        [logging.logger] -- The logger instance
    """

    # Define log format
    log_format = (
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s:%(lineno)d | "
        "%(funcName)s | "
        "%(message)s"
    )

    logger = logging.getLogger(name)

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Output complete log
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Output error log
    fh = logging.FileHandler(err_path)
    fh.setLevel(logging.ERROR)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
