import tarfile
import os

class TarballCreator:
    def __init__(self, path, target_dir):
        self.path = path
        self.target_dir = target_dir

    def create_tarball(self):
        # Check if the path exists
        if not os.path.exists(self.path):
            raise Exception("Path does not exist")
        
        # Check if the target directory exists
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
        
        # Create the tar.gz file
        filename = os.path.basename(self.path) + ".tar.gz"
        tar_file = os.path.join(self.target_dir, filename)
        with tarfile.open(tar_file, "w:gz") as tar:
            tar.add(self.path, arcname=os.path.basename(self.path))
        
        return tar_file
