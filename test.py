import os

from assets.task import Task
from assets.tarball import TarGzArchiver


taskConfig = {
    "name": "xmrig-bckp",
    "source": "/home/vscode/testing/input/Screenshots/",
    "target": "/home/vscode/testing/output",
    "timing": ["00:00:00"],
    "type": "tar"
}

taskConfig2 = {
    "name": "bdx_backup",
    "source": "/home/vscode/testing/input/BDX/",
    "target": "/home/vscode/testing/output",
    "timing": ["00:00:00"],
    "type": "tar"
}

targzarchiver = TarGzArchiver(taskConfig)

task = Task()
task.create(targzarchiver.create)

targzarchiver2 = TarGzArchiver(taskConfig2)
task.create(targzarchiver2.create)

print(task.get_theads())