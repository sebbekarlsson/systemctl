import ConfigParser, os
from systemctl.utils import run_screen_with_command, is_screen_up


class SystemDFile(object):

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(filename))
        self.start_command = self.config.get('Service', 'ExecStart')

    def start(self):
        return run_screen_with_command(
                self.filename.replace('/', '_'),
                self.start_command
                )

    def is_running(self):
        return is_screen_up(self.filename.replace('/', '_').\
                replace('.service', ''))
