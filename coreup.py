import time

# Import custom modules
from assets.logging import Logger
from assets.configManager import ConfigManager

# Setup Config Manager
configmngr = ConfigManager("configs/config.json")
config = configmngr.readConfig()

# Setup logger
logger = Logger("coreup", "./logs", "log")


# Setting enviroment variables
interval = config["service"]["interval"]

logger.log("Starting backup service")
logger.info(f"current interval is set to {interval}")

class ContinuousLoop:
    def __init__(self, interval=interval):
        self.interval = interval

    def run(self):
        while True:
            self.loop()
            time.sleep(self.interval)

    def loop(self):
        logger.log(f"Running check, {interval} sek until next check")

if __name__ == "__main__":
    loop = ContinuousLoop()
    loop.run()