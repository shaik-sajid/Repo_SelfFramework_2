import inspect

import pytest
import logging


@pytest.mark.usefixtures("load")
class BaseClass:
    def test_loggingDemo(self):
        logger_name = inspect.stack()[1][3]
        log = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('C://Users/MY/PycharmProjects/SelfFramework_2/logfile.log')
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

        log.setLevel(logging.DEBUG)
        return log
    pass