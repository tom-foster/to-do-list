
from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['C:/Python27/Scripts/fab.exe', 'reset_database', 'deploy:host={}'.format(host),
        'i C:/Users/Tom/Documents/Documents/website_projects/django/key_pair/first-server-open'],
        cwd=THIS_FOLDER
    )
