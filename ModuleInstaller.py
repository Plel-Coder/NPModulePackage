import platform as pf
import os

class install(object):
    def init(self, command):
        self.command = command

    def win_install(self, command):
        if pf.system() == "Windows":
            os.system(f"{self.command}")
            pass
        else:
            pass

    def mac_install(self, command):
        if pf.system() == "Darwin":     #Darwin = MacOs
            os.system(f"{self.command}")
            pass
        else:
            pass
    def linux_install(self, command):
        if pf.system() == "Linux":
            os.system(f"{self.command}")
            pass
        else:
            pass

    def pip_install(self, command):
        if pf.system() == "Windows":
            os.system(f"pip install {self.command}")