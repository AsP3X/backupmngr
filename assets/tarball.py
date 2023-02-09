import tarfile
import os

class TarGzArchiver:
    def __init__(self, config):
        self.source = config["source"]
        self.target = config["target"]
        self.name = config["name"]
        self.tar_filename = f"{self.target}/{self.name}.tar"
        self.tar = None
        self.total_size = 0
        self.compressed_size = 0

    def create(self):
        print(f"Compressing '{self.source}' to '{self.target}'...")

        # Create a .tar file from the source directory
        self.tar = tarfile.open(self.tar_filename, "w")
        self.tar.add(self.source, arcname=os.path.basename(self.source))
        self.tar.close()

        # Compute the total size of the .tar file
        self.total_size = os.path.getsize(self.tar_filename)

        # Compress the .tar file to .tar.gz
        with open(self.tar_filename, "rb") as tar_file:
            with open(f"{self.tar_filename}.tar.gz", "wb") as gz_file:
                import gzip
                gz = gzip.GzipFile(fileobj=gz_file, mode="wb")
                for chunk in iter(lambda: tar_file.read(4096), b""):
                    gz.write(chunk)
                    self.compressed_size += len(chunk)
                    self.show_progress()
                gz.close()

        # Delete the .tar file
        os.remove(self.tar_filename)

    def show_progress(self):
        progress = self.compressed_size / self.total_size * 100
        print(f"Compression progress: {progress:.2f}%", end="\r")
