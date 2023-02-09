import os

from assets.task import Task
from assets.tarball import TarGzArchiver


task = {
    "name": "xmrig-bckp",
    "source": "/home/vscode/testing/input/Screenshots/",
    "target": "/home/vscode/testing/output",
    "timing": ["00:00:00"],
    "type": "tar"
}

tasker = Task(task)
targzarchiver = TarGzArchiver(task)

targzarchiver.create()