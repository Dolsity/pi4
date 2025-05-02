PI4
---

A PC case for Raspberry Pi 4B, forked from `Pironman <https://github.com/sunfounder/pironman/tree/v2.0>`__ (``v2.0`` branch), with additional modifications and improvements.

.. image:: https://img.shields.io/github/issues/dolsity/pi4?color=0088ff
   :target: https://github.com/dolsity/pi4/issues
   :alt: Issues

.. image:: https://img.shields.io/github/issues-pr/dolsity/pi4?color=0088ff
   :target: https://github.com/dolsity/pi4/pulls
   :alt: GitHub Pull Requests

.. image:: https://img.shields.io/badge/made%20with-python%203.13-blue
   :target: https://www.python.org/downloads/
   :alt: Made with Python 3.13

.. image:: https://img.shields.io/github/license/dolsity/pi4
   :target: ./LICENSE
   :alt: MIT License

Overview
--------
This project is a fork of `Pironman <https://github.com/sunfounder/pironman/tree/v2.0>`__ — a PC case for the Raspberry Pi 4B.
It builds on the original with new features, improvements, and ongoing development.

Improvements:
~~~~~~~~~~~~~
- Added brightness control for the RGB LED strip
- Cleaned up the code structure — more efficient and readable
- **More features and improvements are planned for future releases.**

Installing
----------
For systems that don't have git, python3 and pip pre-installed you need to install them first:

.. code:: sh

    # Update the package list
    sudo apt-get update

    # Install git
    sudo apt-get install git -y

    # Install python3, pip and setuptools
    sudo apt-get install python3 python3-pip python3-setuptools -y

Clone the repository and run the installation script:

.. code:: sh

    cd ~
    git clone https://github.com/dolsity/pi4.git
    cd ~/pi4
    sudo python3 install.py

Usage
-----
.. code:: sh

  Usage:
    pi4 <OPTION> <input>

  Options:
    start                 Start pi4 service
    stop                  Stop pi4 service
    restart               Restart pi4 service
    -h,--help             Show help
    -c,--check            Display all configurations
    -a,--auto             [on/off] Enable or disable auto-start at boot
    -u,--unit             [C/F] Set the unit of temperature (Celsius/Fahrenheit)
    -f,--fan              [temp] Set fan activation temperature (°C, default 35, range 30-80)
    -al,--always_on       [on/true/off/false] Whether the screen is always on (default: false)
    -s,--staty_time       [time] Screen display duration (default: 30 seconds)
    -re,--rgb-enable      [on/true/off/false] Enable/disable RGB strip
    -rb,--led_brightness  [brightness] RGB strip brightness (default: 10, range 0-100)
    -rs,--rgb_style       [style] RGB display style (default: breath)  
                          style: breath, leap, flow, raise_up, colorful
    -rc,--rgb_color       [(HEX)color] Set RGB color (default: 0a1aff)
    -rbs,--rgb_speed      [speed] RGB blink speed (default: 50, range 0-100)
    -pwm,--rgb_pwm        [frequency] RGB signal frequency (default 1000 kHz, 400 ~ 1600)
    -rp,--rgb_pin         [pin] RGB signal pin, could be [10/spi/SPI/12/pwm/PWM] or
                          [21/pcm/PCM], default: 10
    -F,--foreground       Run in foreground

Compatible Systems
------------------
.. list-table::
  :widths: 25 25
  :header-rows: 1

  * - system
    - is compatible?
  * - Raspberry Pi OS - Bullseye (32/64 bit)
    - ✔
  * - Raspberry Pi OS lite - Bullseye (32/64 bit)
    - ✔
  * - Raspberry Pi OS - Buster (32 bit)
    - ✔
  * - Raspberry Pi OS lite - Buster (32 bit)
    - ✔
  * - Ubuntu Desktop 22.04.3 (64 bit)
    - ✔
  * - Ubuntu Server 22.04.3 (32/64 bit)
    - ✔
  * - Ubuntu Server 22.04.5 (32/64 bit)
    - ✔
  * - Ubuntu Server 22.10 (32/64 bit)
    - ✔
  * - Ubuntu Desktop 22.10 (64 bit)
    - ✔
  * - Ubuntu Desktop 23.04 (64 bit)
    - ✔
  * - Ubuntu Server 23.04 (32/64 bit)
    - ✔
  * - Kali Linux (32/64 bit)
    - ✔
  * - DietPi
    - ✔
  * - OSMC
    - ✔
  * - RetroPie
    - ✔
  * - OctoPi
    - ✔
  * - Homebridge
    - ✔
  * - HassOS*
    - ✔
  * - LibreELEC
    - ✘


Contributing
-----------
If you have a solid understanding of python, you can contribute to the project by adding new features, fixing bugs, or improving the code.

License
-------
This project is licensed under the MIT License. See the `LICENSE <./LICENSE>`__ file for details.