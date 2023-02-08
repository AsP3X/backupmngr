import json
import os

class ConfigManager:
    def __init__(self, path):
        self.path = path

    def readConfig(self):
        with open(self.path) as file:
            data = json.load(file)
        return data

    def readBackupConfigs(path):
        config = {}
    
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                file_path = os.path.join(path, filename)
                with open(file_path) as file:
                    file_config = json.load(file)
                    config.update(file_config)
        
        return config