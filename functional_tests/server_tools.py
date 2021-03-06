
from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'C:/Python27/Scripts/fab.exe',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
            '-i',
            'C:/Users/Tom/Documents/website_projects/django/key_pair/first-server-open'
        ],
        cwd=THIS_FOLDER
    ).decode().strip()
#This hangs on live pages 319 onwards are broke on windows.
def reset_database(host):
    subprocess.check_call(
        ['C:/Python27/Scripts/fab.exe', 'reset_database', '--host={}'.format(host),
        '-i', 'C:/Users/Tom/Documents/website_projects/django/key_pair/first-server-open'],
        cwd=THIS_FOLDER
    )
