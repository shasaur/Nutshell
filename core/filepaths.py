import sys

def get_filepath(file):
    if sys.platform == "win32":
        return "../../data/new/" + file
    else:
        return "..\\data\\new\\"+ file