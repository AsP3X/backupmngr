import time

# Import custom modules
from assets.logging import Logger
from assets.configManager import ConfigManager
from assets.timeCalc import TimeCalculator

# Setup Config Manager
configmngr = ConfigManager("configs/config.json")
config = configmngr.readConfig()

# Setup logger
logger = Logger("coreup", "./logs", "log")

# Setup TimeCalculator
timec = TimeCalculator()

# Setting enviroment variables
interval = config["service"]["interval"]

class ContinuousLoop:
    def __init__(self, interval=interval):
        self.interval = interval
        self.tcdata = timec.convert_to_dhms(interval)
        self.days = self.tcdata["days"] if self.tcdata["days"] else 0
        self.hours = self.tcdata["hours"]if self.tcdata["hours"] else 0
        self.minutes = self.tcdata["minutes"] if self.tcdata["minutes"] else 0
        self.seconds = self.tcdata["seconds"] if self.tcdata["seconds"] else 0

        logger.log("Starting backup service")
        logger.info(f"current interval is set to {self.days}d {self.hours}h {self.minutes}m {self.seconds}s")

    def run(self):
        while True:
            self.loop()
            time.sleep(self.interval)

    def loop(self):
        logger.log("Running check...")        
        logger.info(f"Next check in {self.days}d {self.hours}h {self.minutes}m {self.seconds}s")
            
if __name__ == "__main__":
    loop = ContinuousLoop()
    loop.run()