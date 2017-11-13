# systemctl
> The missing service file manager for `Macos` / `Mac` / `OSX`  
> _Behind the curtains, it is using [screen](https://www.gnu.org/software/screen/manual/screen.html)_

## Usage
> The usage is basically the same as with the original systemctl command:

    systemctl <command> <service>

> Available commands:
* start
* status
* stop 

> If not a full path to the service file was given, it will look for it in  
`/etc/systemd/system`
 
## Installation
### Dependencies:
* [screen](https://www.gnu.org/software/screen/manual/screen.html)

> How to install:

    python setup.py install
    
> You're all set! 
