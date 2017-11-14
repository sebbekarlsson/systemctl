# systemctl
> The missing service file manager for `Macos` / `Mac` / `OSX` or any other \*NIX system
> that doesn't come with [systemd](https://en.wikipedia.org/wiki/Systemd).
> _Behind the curtains, it is using [screen](https://www.gnu.org/software/screen/manual/screen.html)_

<p align="center">
  <img src='pottery.gif' />
</p>

## Usage
> The usage is basically the same as with the original systemctl command:

    systemctl <command> <service>

> Available commands:
* start
* status
* stop 

> If not a full path to the service file was given, it will look for it in  
`/etc/systemd/system`

> The directory `/etc/systemd/system` does not exist by default in MacOS.  
> To create it, execute:

    sudo mkdir -p /etc/systemd/system

> Now you can place `.service` files there.
 
## Installation
### Dependencies:
* [screen](https://www.gnu.org/software/screen/manual/screen.html)

> How to install:

    python setup.py install
    
> You're all set! 
