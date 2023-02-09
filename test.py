import os

from assets.task import Task
from assets.tarball import TarGzArchiver


task = {
    "name": "xmrig-bckp",
    "source": "testing/input/Screenshots/",
    "target": "testing/output",
    "timing": ["00:00:00"],
    "type": "tar"
}

permissions = os.stat(__file__).st_mode
print(permissions)

tasker = Task(task)
targzarchiver = TarGzArchiver(task)

targzarchiver.create()