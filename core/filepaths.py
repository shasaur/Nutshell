import sys

def get_filepath(file):
    if not sys.platform == "win32":
        return "../data/" + file
    else:
        return "..\\..\\data\\new\\"+ file
