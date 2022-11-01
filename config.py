import os
import pathlib

db_path = os.getcwd() + '/resume_scans.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
SQLALCHEMY_TRACK_MODIFICATIONS = False

ALLOWED_FILES_TYPES = ['pdf', 'docx', 'doc', 'html', 'xhtml',
                       'txt']  # based on the file processing functions in the resume scanner .py.

AFFINDA_TOKEN = ''

# a reminder of why this folder is currently needed is in the resume_scanner.py where it's used
TEMP_FOLDER = os.getcwd() + '/temp/'

pathlib.Path(TEMP_FOLDER).mkdir(parents=True, exist_ok=True)  # create folder if doesn't exist
