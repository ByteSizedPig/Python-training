import subprocess

def send_ping():
    target = input("which target would you like to ping?\n")

    result = subprocess.run(f'ping {target}')

    return result.returncode

def send_ping_legacy_method(target):
    subprocess.call('ping {}'.format(target))

if send_ping() == 1:
    print('invalid target')