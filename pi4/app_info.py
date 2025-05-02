import os

__app_name__ = 'pi4'
__version__ = '0.1.1' # MAJOR.MINOR.PATCH

try:
    username = os.getlogin()
except:
    username = os.popen("echo ${SUDO_USER:-$(who -m | awk '{ print $1 }')}").readline().strip()

config_file = f'/opt/{__app_name__}/config.txt'
