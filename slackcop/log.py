import os
import sys

import logbook


APPLICATION_LOG_NAME = "application.log"
ERROR_LOG_NAME = "error.log"
_logger = logbook.Logger("slackcop")


def setup():
    dirpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs")
    application_log_file_path = os.path.join(dirpath, APPLICATION_LOG_NAME)
    error_log_file_path = os.path.join(dirpath, ERROR_LOG_NAME)

    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    if not os.path.exists(application_log_file_path):
        with open(application_log_file_path, "a"):
            pass

    if not os.path.exists(error_log_file_path):
        with open(application_log_file_path, "a"):
            pass

    logbook.FileHandler(application_log_file_path, level='INFO').push_application()
    logbook.FileHandler(application_log_file_path, level='WARNING').push_application()
    logbook.FileHandler(error_log_file_path, level='ERROR').push_application()
    logbook.StderrHandler(level='CRITICAL').push_application()


def info(message):
    _logger.info(message)


def warn(message):
    _logger.warn(message)


def error(message):
    _logger.error(message)


def critical(message):
    _logger.critical(message)
    sys.exit()
