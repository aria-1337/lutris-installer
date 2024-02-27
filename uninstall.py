import subprocess
import os
import shutil
from os import listdir
from os.path import isfile, join

# Remove lutris
subprocess.call(['sudo', 'dpkg', '-r', 'lutris'])

# Cleanup existing version file
files = [f for f in listdir('./') if isfile(join('./', f))]
for f in files:
    if "lutris" in f:
        os.remove(f)

# cleanup all other files
home_path = os.path.expanduser('~')
shutil.rmtree(os.path.join(home_path, '.cache/lutris'))
shutil.rmtree(os.path.join(home_path, '.local/share/lutris'))
shutil.rmtree(os.path.join(home_path, 'Games'))
