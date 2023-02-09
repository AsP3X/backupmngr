import os
import time
import json

# Import custom modules
from assets.logging import Logger
from assets.configManager import ConfigManager
from assets.timeCalc import TimeCalculator
from assets.timecoderunner import TimingCodeRunner

# Setup Config Manager
configmngr = ConfigManager("configs/config.json")
config = configmngr.readConfig()

# Setup logger
logger = Logger("COREUP", "./logs", "log")

# Setup TimeCalculator
timec = TimeCalculator()

# Setting enviroment variables
interval = config["service"]["interval"]
version = config["coreup"]["version"]
release = config["coreup"]["release"]

def checkFolders(path):
    if os.path.isdir(path):
        logger.log(f"Path ({path}) exist! Skipping...")
    else:
        logger.warning(f"Path ({path}) doesn't exist")
        logger.info(f"Creating directory tree at: {path}")
        os.makedirs(path)

def checkForConfig(path, project):
    if not os.path.isdir(path): return False
    configList = os.listdir(path)
    if f"{project}.json" in configList:
        return True
    else:
        return False

def getBConfig(path):
    if os.path.isdir(path):
        with open(path) as file:
            file_config = json.load(file)
            return file_config

class ContinuousLoop:
    def __init__(self, interval=interval):
        self.script_root = os.getcwd()
        self.backup_configs = f"{self.script_root}/configs/tasks"
        self.interval = interval
        self.tcdata = timec.convert_to_dhms(interval)
        self.days = self.tcdata["days"] if self.tcdata["days"] else 0
        self.hours = self.tcdata["hours"]if self.tcdata["hours"] else 0
        self.minutes = self.tcdata["minutes"] if self.tcdata["minutes"] else 0
        self.seconds = self.tcdata["seconds"] if self.tcdata["seconds"] else 0

        self.tasks = []

        logger.log("Starting backup service")
        logger.log(f"Current Version: {version} from {release}")
        logger.info(f"current interval is set to {self.days}d {self.hours}h {self.minutes}m {self.seconds}s")
        logger.info(f"Script root: {self.script_root}")
        logger.info(f"backup configs: {self.backup_configs}")

        checkFolders("configs/backups")

    def run(self):
        while True:
            self.loop()
            time.sleep(self.interval)

    def loop(self):
        logger.log("Running check...")
        
        if not os.path.isdir(self.backup_configs):
            logger.warning(f"No Tasks found, please create a new Task in: {self.backup_configs}")
            return

        for task in os.listdir(self.backup_configs):
            task_name = task.split('.')[0]
            
            if not task_name in self.tasks:
                self.tasks.append(task_name)



        # if not tasks == []:
        #     logger.info(checkForConfig(self.backup_configs, tasks[0]))
        
        logger.info(f"Next check in {self.days}d {self.hours}h {self.minutes}m {self.seconds}s")
            
if __name__ == "__main__":
    loop = ContinuousLoop()
    loop.run()