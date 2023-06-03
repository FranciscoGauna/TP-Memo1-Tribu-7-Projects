from datetime import datetime
from sys import stdout


# Level Codes
class LoggerLevel:
    ERROR = 1
    INFO = 2
    DEBUG = 3

    vals = {
        "ERROR": 1,
        "INFO": 2,
        "DEBUG": 3
    }

class Logger:
    # Singleton
    logger = None

    def __init__(self, out=stdout, level=LoggerLevel.INFO) -> None:
        self._out = out
        self._level = level

    def write(self, msg: str):
        self._out.write(f"{datetime.now().isoformat()}: {msg}\n")

    def error(self, msg: str):
        if self._level >= LoggerLevel.ERROR:
            self.write("ERROR: " + msg)

    def info(self, msg: str):
        if self._level >= LoggerLevel.INFO:
            self.write("INFO: " + msg)

    def debug(self, msg: str):
        if self._level >= LoggerLevel.DEBUG:
            self.write("DEBUG: " + msg)

    def set_level(self, level: str):
        self._level = LoggerLevel.vals[level]


logger = Logger()
