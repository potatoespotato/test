import os
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

FIRST_HOST = ""
FIRST_HOST_USERNAME = ""
FIRST_HOST_PASSWORD = ""
SECOND_HOST = ""
SECOND_HOST_USERNAME = ""
SECOND_HOST_PASSWORD = ""

'''
Изначально хотел сделать чероез walk, но нашел эту библиотеку
'''

TEMP_DIR_NAME = "temp"
TEMP_DIR = os.path.join(os.path.abspath(os.path.curdir), TEMP_DIR_NAME)


def copy_files_from_first_server_to_second_server():
    try:
        os.mkdir(TEMP_DIR_NAME)
    except FileExistsError:
        pass

    with pysftp.Connection(host=FIRST_HOST, username=FIRST_HOST_USERNAME, password=FIRST_HOST_PASSWORD, cnopts=cnopts) as sftp:
        sftp.get_r(sftp.pwd, TEMP_DIR)

    with pysftp.Connection(host=SECOND_HOST, username=SECOND_HOST_USERNAME, password=SECOND_HOST_PASSWORD, cnopts=cnopts) as sftp:
        sftp.put_r(TEMP_DIR, sftp.pwd)

    try:
        os.rmdir(TEMP_DIR)
    except FileNotFoundError:
        pass


copy_files_from_first_server_to_second_server()

