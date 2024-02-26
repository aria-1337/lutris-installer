import requests
import subprocess

def call(args):
    subprocess.call(args)

# Update system
call(['sudo', 'apt', 'update'])

# Upgrade your system
call(['sudo', 'apt', 'upgrade'])

# Uninstall any current version of lutris
call(['sudo', 'dpkg', '-r', 'lutris'])

# Get the latest version of lutris
tags = requests.get('https://api.github.com/repos/lutris/lutris/tags')
latest_version = tags.json()[0]['name']
cleaned_version = latest_version[1:]

# Download the deb package
call(['wget', f'https://github.com/lutris/lutris/releases/download/{latest_version}/lutris_{cleaned_version}_all.deb'])

# Install the deb package
call(['sudo', 'dpkg', '-i', f'lutris_{cleaned_version}_all.deb'])

# Update system
call(['sudo', 'apt', 'update'])

# Upgrade your system
call(['sudo', 'apt', 'upgrade'])

# Fix any broken files (This is commonly needed to be done but optional)
all(['sudo', 'apt', '--fix-broken', 'install'])
