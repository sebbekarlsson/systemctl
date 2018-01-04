import subprocess
from simple_pipe.methods import pipe


def get_screens():
    screens = []

    process = subprocess.Popen(
        ['screen', '-ls'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    process.wait()

    _screens = process.stdout.read().lower().split('\n')
    _screens = [screen.split('.') for screen in _screens if 'tached' in screen]

    for _screen in _screens:
        if len(_screen) < 3:
            continue

        screens.append({
            'id': pipe(
                _screen[0],
                [
                    lambda x: x.replace(' ', ''),
                    lambda x: x.replace('	', ''),
                    lambda x: x.replace('\r', ''),
                    lambda x: x.replace('\n', '')
                ]
            ),
            'name': _screen[1].replace(' ', ''),
            'user': pipe(
                _screen[2],
                [
                    lambda x: x.replace('\t', ''),
                    lambda x: x.replace('(', ''),
                    lambda x: x.replace(')', ''),
                    lambda x: x.replace('detached', ''),
                    lambda x: x.replace('attached', '')
                ]
            )
        })

    return screens


def is_screen_up(name=None, id=None):
    screens = get_screens()

    for screen in screens:
        if screen['name'] == name or screen['id'] == id:
            return True

    return False


def kill_screen(id):
    process = subprocess.Popen(
        ['screen', '-X', '-S', id, 'kill'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    process.wait()

    process = subprocess.Popen(
        ['screen', '-X', '-S', id, 'quit'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    process.wait()

    return process.stdout.read()


def run_screen_with_command(screen_name='screen', command='ls'):
    command = ['screen', '-d', '-m', '-S', screen_name, 'bash', '-c', command]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    process.wait()

    return process.stdout.read()
