from systemctl.utils import get_screens, run_screen_with_command, kill_screen
from systemctl.systemdfile import SystemDFile
import sys
import os


def run():
    if len(sys.argv) < 3:
        print('usage: systemctl <command> <service>')

    command = sys.argv[1]
    service_file = sys.argv[2]

    systemd_file = SystemDFile(service_file)

    systemd_file.start()
