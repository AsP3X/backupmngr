import tarfile
import traceback
import gzip
import os

from .logging import Logger

def to_linux_path(path):
    return path.replace(os.sep, "/")

class TarGzArchiver:
    def __init__(self, config):
        self.logger = Logger("TarGzArchiver", "logs/targzarchiver.log", "log")
        self.source = config["source"]
        self.target = config["target"]
        self.name = config["name"]
        self.tar_filename = f"{self.target}/{self.name}.tar"
        self.tar = None
        self.total_size = 0
        self.compressed_size = 0

    def create(self):
        self.logger.info(f"Compressing '{self.source}' to '{self.target}'...")

        # if the last character of the specified path is a slash, remove it
        if self.source[-1] == os.sep: self.source = self.source[:-1]
        if self.target[-1] == os.sep: self.target = self.target[:-1]

        # Create a .tar file from the source directory
        self.tar = tarfile.open(self.tar_filename, "w")
        files = [os.path.basename(self.source)]
        self.tar.add(self.source, arcname=os.path.basename(self.source))
        self.tar.close()

        # Compute the total size of the .tar file
        self.total_size = os.path.getsize(self.tar_filename)

        # Compress the .tar file to .tar.gz
        with open(self.tar_filename, "rb") as tar_file:
            with open(f"{self.tar_filename}.gz", "wb") as gz_file:
                gz = gzip.GzipFile(fileobj=gz_file, mode="wb")
                for chunk in iter(lambda: tar_file.read(4096), b""):
                    gz.write(chunk)
                    self.compressed_size += len(chunk)
                    self.show_progress(files)
                gz.close()
            tar_file.close()

        # Delete the .tar file
        try:
            os.unlink(self.tar_filename)
        except PermissionError as e:
            self.logger.error(f"PermissionError: {type(e).__name__} - {e}")
            self.logger.error(traceback.format_exc())

    def show_progress(self, files):
        progress = self.compressed_size / self.total_size * 100
        current_file = files[0]
        self.logger.info(f"Compressing file '{current_file}'... {progress:.2f}%", True)
        # print(f"Compressing file '{current_file}'... {progress:.2f}%", end="\r")