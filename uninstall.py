import subprocess
import os
from os import listdir
from os.path import isfile, join

# Remove lutris
subprocess.call(['sudo', 'dpkg', '-r', 'lutris'])

# Cleanup existing version file
files = [f for f in listdir('./') if isfile(join('./', f))]
for f in files:
    if "lutris" in f:
        os.remove(f)
