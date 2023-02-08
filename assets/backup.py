from tarball import TarballCreator

class Backup:
    def __init__(self, config, path):
        self.config = config
        self.path = path

    def create(self):
        # if self.config[""]

        if self.config["type"] == "tar":
            backup_type = self.config["type"]
            backup_source = self.path
            backup_dir = self.config[""]
            tbc = TarballCreator()