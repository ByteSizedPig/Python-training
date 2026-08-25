import subprocess

def send_ping():
    return subprocess.call('ping google.com')

send_ping()