from threading import Thread
from logging import Logger

class Task:
    def __init__(self, config):
        self.config = config
        self.threads = []
        # self.logger = Logger("COREUP/TASKMNGR", "./logs", "log")
        # self.logger.info("Loaded Successfully")

    def create_threads(self, target, args):
        """
        creates threads and stores them
        """
        new_thread = Thread(target=target, args=args)
        self.threads.append(new_thread)

    def dispatch_threads(self):
        """
        dispatches the thread and removes it when finished
        """
        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()
            self.threads.remove(thread)
