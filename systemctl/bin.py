from systemctl.systemdfile import SystemDFile
import sys
import os


def show_usage():
    print('usage: systemctl <command> <service>')


def run():
    if len(sys.argv) < 3:
        show_usage()
        quit()

    command = sys.argv[1]
    service_file = sys.argv[2] + '.service' if '.service' not in sys.argv[2]\
        else sys.argv[2]

    if not os.path.isfile(service_file):
        service_file = '/etc/systemd/system/' + service_file

    if not os.path.isfile(service_file):
        print('No such service')
        quit()

    systemd_file = SystemDFile(service_file)

    if command == 'start':
        systemd_file.start()

    elif command == 'status':
        print('(running)' if systemd_file.is_running() else '(dead)')

    elif command == 'stop':
        systemd_file.stop()
    else:
        print('Command not found')
        show_usage()
