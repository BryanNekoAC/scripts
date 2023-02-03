import pip
import time
import threading
import os
import sys
import subprocess

def import_or_install(module):
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

import_or_install('random')
import random
