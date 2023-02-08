import os
import time
from termcolor import colored

class Logger:
    def __init__(self, caller, logPath, logType):
        self.caller = caller
        self.logPath = logPath
        self.logType = logType

        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)

    def log(self, message):
        self._write_to_console(message, "white", "default")
        self._write_to_log_file(message, "default")

    def info(self, message):
        self._write_to_console(message, "blue", "info")
        self._write_to_log_file(message, "info")

    def error(self, message):
        self._write_to_console(message, "red", "error")
        self._write_to_log_file(message, "error")

    def warning(self, message):
        self._write_to_console(message, "yellow", "warning")
        self._write_to_log_file(message, "warning")

    def success(self, message):
        self._write_to_console(message, "green", "success")
        self._write_to_log_file(message, "success")

    def _write_to_console(self, message, color, log_file):
        if self.logType == "console" or self.logType == "log":
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
            caller = colored(self.caller, "magenta")
            message = colored(message, color)
            print(f"[{timestamp}] [{caller}] - {message}")

    def _write_to_log_file(self, message, log_file):
        if self.logType == "logfile" or self.logType == "log":
            with open(f"{self.logPath}/{log_file}.log", "a") as file:
                timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
                caller = self.caller
                file.write(f"[{timestamp}] [{caller}] - {message}\n")
