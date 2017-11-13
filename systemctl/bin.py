from systemctl.utils import get_screens, run_screen_with_command, kill_screen
from systemctl.systemdfile import SystemDFile
import sys
import os


def run():
    if len(sys.argv) < 3:
        print('usage: systemctl <command> <service>')
        quit()

    command = sys.argv[1]
    service_file = sys.argv[2]

    if not os.path.isfile(service_file):
        service_file = '/etc/systemd/system/' + service_file

    if not os.path.isfile(service_file):
        print('No such service')
        quit()

    systemd_file = SystemDFile(service_file)
    
    if command == 'start':
        systemd_file.start()

    if command == 'status':
        print(systemd_file.is_running())
