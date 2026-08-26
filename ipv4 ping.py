import subprocess

def send_ping(target):
    return subprocess.call(f'ping {target}')

def send_ping_legacy_method(target):
    return subprocess.call('ping {}'.format(target))

send_ping(input("which target would you like to ping?\n"))