import os

def get_ui_file_path(ui_file):
    os.path.sep.join(ui_file.split('/'))
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, ui_file)) 

    