import json
import datetime

from tarball import TarballCreator
from task import Task

class TimingCodeRunner:
    def __init__(self, config, timing_codes):
        self.config = json.loads(config)
        self.timing_codes = timing_codes
        self.tarballc = TarballCreator

    def run_code(self):
        for code in self.timing_codes:
            # Parse the timing code
            month, day, hour = code.split(':')
            # Check if the code should be run based on the current time
            if self.should_run(month, day, hour):
                # Run the code
                self.run()

    def should_run(self, month, day, hour):
        now = datetime.datetime.now()
        if int(month) == now.month and int(day) == now.day and int(hour) == now.hour:
            return True
        return False

    def run(self):
        task = Task(self.config)
        task.create_threads(self.tarballc.create_tarball(self.config["source"], self.config["target"]))
        task.dispatch_threads()
    
        pass
