import subprocess


def get_detached_screens():
    screens = []

    process = subprocess.Popen(['screen', '-ls'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)

    returncode = process.wait()

    _screens = process.stdout.read().lower().split('\n')
    _screens = [screen.split('.') for screen in _screens if 'tached' in screen]

    for _screen in _screens:
        if len(_screen) < 3:
            continue

        screens.append({
            'id': _screen[0].replace(' ', '').replace('	', '').\
                    replace('\r', '').replace('\n', ''),
            '_id': _screen[1].replace(' ', ''),
            'user': _screen[2].replace('\t', '').replace('(', '').\
                    replace(')', '').replace('detached', '').\
                    replace('attached', '')
        })

    return screens

def kill_screen(id):
    process = subprocess.Popen(['screen', '-X', '-S', id, 'kill'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)

    returncode = process.wait()
    
    return process.stdout.read()

def run_screen_with_command(command):
    screens = []

    command = ['screen', '-d', '-m', '-S', 'myscreen', 'bash', '-c', "'{}'".format(command)] 
    process = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    
    process.wait()
    print(process.stderr, process.stdout.read())
    #returncode = process.wait()
    print ' '.join(command)

    return process




run_screen_with_command('sleep 10')
