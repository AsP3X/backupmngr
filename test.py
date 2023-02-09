from assets.task import Task
from assets.tarball import TarGzArchiver


task = {
    "name": "test",
    "source": "test/in/WiresharkPortable64",
    "target": "test/out",
    "timing": ["00:00:00"],
    "type": "tar"
}

tasker = Task(task)
targzarchiver = TarGzArchiver(task)

targzarchiver.create()
targzarchiver.show_progress()