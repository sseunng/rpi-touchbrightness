# rpi-touchbrightness
Adjust brightness of Raspberry Pi 7-inch touchscreen on touch and over time.

## Features
- Use **rpi-backlight** to adjust brightness
- Make bright if you touch your screen
- Adjust maximum and minimum brightness over time

## Requirements
- [rpi-backlight](https://github.com/linusg/rpi-backlight)
- Follow the installation instructions of **rpi-backlight**

## Installation
```console
$ git clone https://github.com/sseunng/rpi-touchbrightness
```

## Test
```console
$ python3 brightness.py
```

## Make autostart
```console
$ sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
add following line above the xscreensaver option
```console
@lxterminal -e python3 /home/pi/brightness.py
```
path might be different.
