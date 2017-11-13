from systemctl.utils import get_screens, run_screen_with_command, kill_screen
import sys


def run():
    if len(sys.argv) < 3:
        print('usage: systemctl <command> <service>')
