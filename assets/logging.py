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

    def get_path(self):
        return self.logPath

    def log(self, message, sameLine=False):
        self._write_to_console(message, "white", "default", sameLine)
        self._write_to_log_file(message, "default")

    def info(self, message, sameLine=False):
        self._write_to_console(message, "blue", "info", sameLine)
        self._write_to_log_file(message, "info")

    def error(self, message, sameLine=False):
        self._write_to_console(message, "red", "error", sameLine)
        self._write_to_log_file(message, "error")

    def warning(self, message, sameLine=False):
        self._write_to_console(message, "yellow", "warning", sameLine)
        self._write_to_log_file(message, "warning")

    def success(self, message, sameLine=False):
        self._write_to_console(message, "green", "success", sameLine)
        self._write_to_log_file(message, "success")

    def _write_to_console(self, message, color, log_file, sameLine=False):
        if self.logType == "console" or self.logType == "log":
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
            caller = colored(self.caller, "magenta")
            message = colored(message, color)
            if sameLine:
                print(f"[{timestamp}] [{caller}] - {message}", end='\r')
            else:
                print(f"[{timestamp}] [{caller}] - {message}")

    def _write_to_log_file(self, message, log_file):
        if self.logType == "logfile" or self.logType == "log":
            with open(f"{self.logPath}/{log_file}.log", "a") as file:
                timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
                caller = self.caller
                file.write(f"[{timestamp}] [{caller}] - {message}\n")
