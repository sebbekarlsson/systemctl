import ConfigParser
from systemctl.utils import (
    run_screen_with_command,
    is_screen_up,
    get_screens,
    kill_screen
)


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
        return is_screen_up(
            self.filename.replace('/', '_').replace('.service', '')
        )

    def stop(self):
        screens = get_screens()

        for screen in screens:
            if screen['name'] == self.filename.replace('/', '_').\
                    replace('.service', ''):

                print('Trying to kill: {}...'.format(screen['name']))
                return kill_screen(screen['id'])

        return False
