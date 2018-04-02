A very simple implementation of websockets for learning purposes that will be served from a raspberry pi in Access Point mode.

Note: this requires python3, so please create and populate the virtual environment as follows

```
virtualenv -p python3 venv3
pip install -r requirements
```

## Steps followed to configure the Access Point
### Get minibian and burn it onto the sdcard
  delete partitions on sd card with gparted
  dd bs=4M if=image_file.img of=/dev/mmcblk0p conv=fsync
### Expand the partition
    An easier way to do it is install raspi-config [https://minibianpi.wordpress.com/how-to/resize-sd/](here)
### Update to strech
  [link](https://linuxconfig.org/how-to-upgrade-debian-8-jessie-to-debian-9-stretch)
### Setting up access point
    You'll need to install dhcpd and iptables along with dnsmasq and hostapd [see](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

### Need to install git, sudo, pip, python
    install [pip](https://bootstrap.pypa.io/get-pip.py)

    It looks like the connection is not stable with the phone unless ip is static. Proceed as follows:
    * Add this to interfaces
    
    ```
    iface wlan0 inet static 
        address 192.168.4.1 
        netmask 255.255.255.0
    ```
    
    * Then in the terminal:
    
    ```
    sudo ifconfig wlan0 192.168.4.1
    sudo reboot
    ```
    

## Running testing and production server
To run the testing server execute run\_test\_server
To run the production server, run ./start. This will use gunicorn to load the app in daemon mode

Both servers will be be available at local_ip:8080

### Find how to connect raspberry with Arduino so rpi sends orders to arduino
See arduino/test_serial.py and arduino/move_on_serial_read/move_on_serial_read.ino
Raspberry will need to access the serial port by sudo, and this port needs to be activated with raspi-config
[see this](http://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/)
I need to change the port in the pi and find out why it runs but does not move the wheels as before
### NEXT
Check wiring on motors and uncomment lines on move_on_serial_read.ino
