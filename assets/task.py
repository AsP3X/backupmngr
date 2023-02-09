import threading
import time

from .logging import Logger

class Task:
    def __init__(self):
        self.logger = Logger("COREUP/Task", "logs/task", "log")
        self.logger.info("Loaded Successfully")
        self.threads = []
    
    def create(self, function, *args):
        thread = threading.Thread(target=self.__run_function, args=(function, args))
        self.threads.append(thread.getName())
        thread.start()
        
    def __run_function(self, function, args):
        if not callable(function):
            raise TypeError(f'Expected a function, but got {type(function)}')

        self.logger.info(f'Running function {function.__name__} in a new thread')
        function(*args)
        self.logger.info(f'Finished running function {function.__name__} in a new thread')

    def get_theads(self):
        return self.threads